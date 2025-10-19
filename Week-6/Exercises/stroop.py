from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_j, K_f
import random

""" Constants """
KEYS = [K_j, K_f]
TRIAL_TYPES = ["match", "mismatch"] # Define trial types
COLORS = ["red", "blue", "green", "orange"]

N_BLOCKS = 2
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

stims = stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

""" Experiment """
def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stims[word][color]
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(KEYS)
    # J = match, F = mismatch
    correct = (trial_type == "match" and key == K_j) or (trial_type == "mismatch" and key == K_f)
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1000)

control.start(subject_id=1)

present_instructions(INSTR_START)
for block_id in range(1, N_BLOCKS + 1):
    for trial_id in range(1, N_TRIALS_IN_BLOCK + 1):
        # select trial type and stimuli
        trial_type = random.choice(TRIAL_TYPES)
        word = random.choice(COLORS)
        if trial_type == "match":
            color = word
        else:
            # choose a different color for mismatch
            other_colors = [c for c in COLORS if c != word]
            color = random.choice(other_colors)
        run_trial(block_id, trial_id, trial_type, word, color)
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)
present_instructions(INSTR_END)

control.end()