from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode(False)
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0), size):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

def make_instruction(pos = (0,0)):
    text = stimuli.TextScreen(
        text="Please mask one of your eyes, and fixate the other to the fixation."
    )
    make_instruction.preload()
    return text

""" Experiment """
# Modify run_trial so it takes a side as input (L/R) 
# and runs the procedure for the left or right eye of the subject

def run_trial():
    fixation = stimuli.FixCross(size=(15,  15), line_width=10, position=[300, 0])
    fixation.preload()

    radius = 75
    circle = make_circle(radius)

    fixation.present(True, False)
    circle.present(False, True)

    exp.keyboard.wait()

control.start(subject_id=1)

run_trial()
    
control.end()