"""
The program should have customizable grid parameters 
controlling 
1. the size and color of the squares, 
2. the space between them, 
3. the number of rows and number of columns, and
4. the screen background color.
"""

from expyriment import control, stimuli, design

def hermann_grid(size = (50, 50), 
                 square_color = (255, 255, 255), 
                 space = 10, 
                 n_row = 10, 
                 n_col = 10, 
                 bg_color = (0, 0, 0)):

    # Create experiment, set background color parameter
    exp = design.Experiment(background_colour = bg_color)

    # Set development mode
    control.set_develop_mode(False)

    control.initialise(exp)

    # Calculate the overall width and height of the whole picture
    width_overall = n_col * size[0] +  (n_col - 1) * space
    height_overall = n_row * size[1] + (n_row - 1) * space

    # Based on the overall width and height, calculate each x coordinates of each columns of squares

    # Calculate x coordinates
    left_edge = - (width_overall / 2)
    x_coords = []
    width_square = size[0]
    for i in range(n_col):
        current_x = left_edge + width_square * 0.5 + i * (width_square + space)
        x_coords.append(current_x)
    print(x_coords)

    # Calculate y coordinates
    bottom_edge = -(height_overall / 2)
    y_coords = []
    height_square = size[1]
    for i in range(n_row):
        current_y = bottom_edge + height_square * 0.5 + i * (height_square + space)
        y_coords.append(current_y)
    print(y_coords)

    # Define the square
    square = stimuli.Rectangle(
        size = size,
        colour = square_color
    )

    # Clear the screen
    exp.screen.clear()

    for x in x_coords:
        for y in y_coords:
            pos = (x, y)
            print(pos)
            square.position = pos
            square.present(clear = False, update = False)

    # Update the screen
    exp.screen.update()

    # End the experiment after keyboard press
    exp.keyboard.wait()

    control.end(exp)

hermann_grid()