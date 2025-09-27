from expyriment import control, stimuli, design

# Define the experiment, set the background to grey
exp = design.Experiment(background_colour = (128, 128, 128))

# control.set_develop_mode(True)

control.initialise(exp)

# Get the monitor's spec
width, height = exp.screen.size

# Calculate the squares' length
square_length = round(0.25 * width, 0)
vertex_abs = square_length // 2

# Calculate the circle's radius
circle_radius = round(0.05 * width, 0)

# Create the square
square = stimuli.Rectangle(
    size = (square_length, square_length),
    position = (0, 0),
    colour = (128, 128, 128)
)

# Create the positions for circles, grouped by up/bottom
pos_up = [
    (- vertex_abs, vertex_abs),
    (vertex_abs, vertex_abs)
]

pos_bottom = [
    (- vertex_abs, - vertex_abs),
    (vertex_abs, - vertex_abs)
]

# Define the circles
circles = []

for p in pos_up:
    i_circle = stimuli.Circle(
        radius = circle_radius,
        position = p,
        colour = (255, 255, 255)    # Up colors are black
    )
    circles.append(i_circle)

for p in pos_bottom:
    i_circle = stimuli.Circle(
        radius = circle_radius,
        position = p,
        colour = (0, 0, 0)    # Up colors are white
    )
    circles.append(i_circle)

# Preparation of stimuli completed


# Clear the screen
exp.screen.clear()

# Present the circles
for i in circles:
    i.present(update = False, clear = False)

# Present the square
square.present(update = True, clear = False)

exp.keyboard.wait()