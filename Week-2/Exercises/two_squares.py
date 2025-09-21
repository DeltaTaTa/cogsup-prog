"""

## Exercise 2: Side-by-side objects
Open `two_squares.py`. Write a script that displays two squares side by side, the left one red, the right one green. Leave the fixation cross out. The two squares should be separated by 200 pixels but centered as a whole. Present them on-screen until a key is pressed.

Hints: 
- By default, stimuli are presented at the center of the screen, so you need to modify this via the ```position``` attribute of shapes
- Shape size can be set when initializing the shape (e.g., ```stimuli.Rectangle(..., position = (x, y))```), or afterward (e.g., ```square_1.position = (x, y)``` or ```square_1.reposition(x, y)```)
- The position of the shape corresponds to the coordinates at the shape's center
- Expyriment takes (0, 0) to be the center of the screen and measures space in pixel units

"""


from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "two_squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

color_red = (255, 0, 0)
color_green = (0, 255, 0)

# Specify the size of each square
shape_size = (200, 200)

square_left = stimuli.Rectangle(
    colour = color_red,
    size = shape_size,
    position = (-200, 0)
)

square_right = stimuli.Rectangle(
    colour = color_green,
    size = shape_size,
    position = (200, 0)
)

# Start the experiment
control.start(subject_id = 1)

# Present the two squares
square_left.present(clear = True, update = False)
square_right.present(clear = False, update = True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()