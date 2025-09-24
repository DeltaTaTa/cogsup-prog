from expyriment import control, stimuli, design

exp = design.Experiment(background_colour = (128, 128, 128))

control.initialise(exp)

# Get the monitor's spec
width, height = exp.screen.size

# Calculate the squares' length
square_length = round(0.25 * width, 0)

# Calculate the circle's radius
circle_radius = round(0.05 * width, 0)

# Create the square
square = stimuli.Rectangle(
    size = (square_length, square_length),
)

# Createthe positions
pos = []
for w in (square_length // 2, -square_length // 2):
    for h in (square_length // 2, -square_length // 2):
        pos.append((w,h))

# Define the circles
circles = []
for p in pos:
    i_circle = stimuli.Circle(
        radius = circle_radius,
        position = p
    )
    circles.append(i_circle)

for 