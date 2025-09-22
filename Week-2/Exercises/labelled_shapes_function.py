from expyriment import design, control, stimuli
from expyriment.misc import geometry

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "labelled_shapes")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

def regular_polygon_generator(n, len, col, pos):
    shape = stimuli.Shape(
        vertex_list = geometry.vertices_regular_polygon(n, len),
        colour = col,
        position = pos
    )
    return shape


# Define the colors
color_purple = (160, 32, 240)
color_yellow = (255, 222, 33)

triangle = regular_polygon_generator(3, 50, color_purple, (-200, 0))

hexagon = regular_polygon_generator(6, 25, color_yellow, (200, 0))

# Start the experiment
control.start(subject_id = 1)

# Present the two squares
triangle.present(clear = True, update = False)
hexagon.present(clear = False, update = True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()
