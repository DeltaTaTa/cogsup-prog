

from expyriment import design, control, stimuli
from expyriment.misc import geometry

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "labelled_shapes")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Define the colors
color_purple = (160, 32, 240)
color_yellow = (255, 222, 33)

triangle = stimuli.Shape(
    vertex_list = geometry.vertices_regular_polygon(3, 50),
    colour = color_purple,
    position = (-200, 0)
)

hexagon = stimuli.Shape(
    vertex_list = geometry.vertices_regular_polygon(6, 25),
    colour = color_yellow,
    position = (200, 0)
)

# Start the experiment
control.start(subject_id = 1)

# Present the two squares
triangle.present(clear = True, update = False)
hexagon.present(clear = False, update = True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()
