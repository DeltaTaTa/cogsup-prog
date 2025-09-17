# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Circle")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

square = stimuli.Rectangle(size  = (50, 50), colour = (0, 0, 255))

# Start running the experiment
control.start(subject_id=1)

# Present the square
square.present(clear = True, update = False)

# Present the superimposed fixation
fixation.present(clear = False, update = True)

# Wait for 500 ms
exp.clock.wait(500)

# Present the superimposed fixation cross
square.present(clear=True, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()