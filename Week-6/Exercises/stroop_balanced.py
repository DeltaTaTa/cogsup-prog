from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_j, K_f
import random
import itertools

""" Constants """
KEYS = [K_j, K_f]
TRIAL_TYPES = ["match", "mismatch"] # Define trial types
COLORS = ["red", "blue", "green", "orange"]

N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16

INSTR_START = """
In this task, you have to indicate whether the meaning of a word and the color of its font match.
Press J if they do, F if they don't.
Press SPACE to continue.
"""
INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """ """
FEEDBACK_INCORRECT = """ """
FEEDBACK_CORRECT = ""
FEEDBACK_INCORRECT = ";("

""" Helper functions """
def load(stims):    # Preload stimuli
    for stim in stims:
        stim.preload()

def timed_draw(*stims): # Present and time the stimuli
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims) # Take time_draw() function
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

# Dictionary of TextLine stims: stims[word][color]
stims = stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

""" Experiment """
def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stims[word][color]
    present_for(fixation, t=500)
    # Present word in color
    stim.present()
    key, rt = exp.keyboard.wait(KEYS)   # returns (key, rt)
    # J = match, F = mismatch
    correct = (trial_type == "match" and key == K_j) or (trial_type == "mismatch" and key == K_f)
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1000)

# Derangement helper ---------
def derangements(lst):
    """Return list of permutations (tuples) where no element is in its original position."""

    ders = []
    for perm in itertools.permutations(lst):
        if all(original != perm[idx] for idx, original in enumerate(lst)):
            ders.append(perm)
    return ders
# COLORS = ["red", "blue", "green", "orange"]
PERMS = derangements(COLORS)
# rint(PERMS)

# ------Trial list generator per subject
# A list of dictionaries for the base trials
def generate_subject_trials(subject_id):
    # pick a derangement for this subject (wrap-around)
    perm = PERMS[(subject_id - 1) % len(PERMS)]

    # base = all match trials + mismatch trials defined by the derangement
    base = (
        [{"trial_type": "match", "word": c, "color": c} for c in COLORS] +
        [{"trial_type": "mismatch", "word": w, "color": c} for w, c in zip(COLORS, perm)]
    )
    # Sanity: base length should be 8 (4 match + 4 mismatch)
    assert len(base) == 8

    # how many times to repeat base inside one block to reach N_TRIALS_IN_BLOCK
    block_reps = N_TRIALS_IN_BLOCK // len(base)
    if N_TRIALS_IN_BLOCK % len(base) != 0:
        raise ValueError("N_TRIALS_IN_BLOCK must be divisible by len(base) (8)")

    trials = []
    for b_index in range(1, N_BLOCKS + 1):
        block = base * block_reps
        random.shuffle(block)
        for t_index, trial in enumerate(block, start=1):
            trials.append({
                "subject_id": subject_id,
                "block_id": b_index,
                "trial_id": t_index,
                "trial_type": trial["trial_type"],
                "word": trial["word"],
                "color": trial["color"]
            })
    return trials


subject_id = 1
control.start(subject_id=subject_id)

present_instructions(INSTR_START)

trials = generate_subject_trials(subject_id)

# iterate blocks and trials; show mid-instruction after half of blocks
for b_id in range(1, N_BLOCKS + 1):
    # get trials for this block
    block_trials = [t for t in trials if t["block_id"] == b_id]
    for t in block_trials:
        run_trial(t["block_id"], t["trial_id"], t["trial_type"], t["word"], t["color"])

    # show halfway message after half the blocks (i.e., after block 4)
    if b_id == N_BLOCKS // 2:
        present_instructions(INSTR_MID)

present_instructions(INSTR_END)

control.end()