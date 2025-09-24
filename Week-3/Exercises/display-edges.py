from expyriment import stimuli, design, control

exp = design.Experiment()

control.initialize(exp)

# Get the monitor's spec
width, height = exp.screen.size

# Calculate the squares' length
square_length = round(0.05 * width, 0)

# Define the square
square = stimuli.Rectangle(
    size = (square_length, square_length),
    line_width = 1
)

# Create a list storing all positions
pos = [(-width // 2 + square_length // 2, -height // 2 + square_length // 2),
       (-width // 2 + square_length // 2, height // 2 - square_length // 2),
       (width // 2 - square_length // 2, height // 2 - square_length // 2),
       (width // 2 - square_length // 2, - height // 2 + square_length // 2)]

# Adjust the square's position and updating
for i in range(4):
    if i == 0:
        square.position = pos[i]
        square.present(update = False, clear = True)

    elif i < 3:
        square.position = pos[i]

        square.present(update = False, clear = False)

    else:
        square.position = pos[i]
        square.present(update = True, clear = False)


exp.keyboard.wait()