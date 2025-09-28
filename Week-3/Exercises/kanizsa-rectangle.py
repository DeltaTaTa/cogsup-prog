"""
Take your existing Kanizsa-square code 
and modify it in a file called kanizsa-rectangle.py 
so that it displays a rectangle instead of a square.

The rectangle should have a given aspect ratio (width over height)
Its size should be controlled by a scaling factor

The inducing circles should also be scaled by their own scaling factor.
Put all of this inside a function. The function should take three arguments:

The aspect ratio of the rectangle.
The scaling factor for the rectangle.
The scaling factor for the circles.
Hint: When initializing the exp object, 
set the background_colour to C_GREY (import it from expyriment.misc.constants).

Experiment with these parameters: 
Does the perceived strength of the illusory contours change depending on them?
"""


from expyriment import control, stimuli, design

def kanizsa(ratio_rectangle = (16, 9), scale_rectangle = 0.25, 
            scale_circle = 0.05):
    # Define the experiment, set the background to grey
    exp = design.Experiment(background_colour = (128, 128, 128))

    # Developement mode
    # control.set_develop_mode(True)

    control.initialise(exp)

    # Get the monitor's spec
    width_screen, height_screen = exp.screen.size

    print("Screen_spec:", width_screen, "*", height_screen)

    # Define the rectangle's scalling factor, by width
    # scale_rectangle = 0.25

    # Define rectangle's aspect ratio
    # ratio_rectangle = (16, 9)

    # Calculate the width and height of the rectangle
    width_rectangle = width_screen * scale_rectangle
    height_rectangle = width_rectangle * (ratio_rectangle[1] / ratio_rectangle[0] )
    size_rectangle = (width_rectangle, height_rectangle)

    print("Rectangle size: ", size_rectangle)

    # Define the circle's scalling factor
    # scale_circle = 0.05

    # Calculate the circle's radius, by multiplying the scalling ratio by monitor width
    circle_radius = round(scale_circle * width_screen, 0)

    # Create the rectangle
    rectangle = stimuli.Rectangle(
        size = size_rectangle,
        position = (0, 0),
        colour = (128, 128, 128)
    )

    # Create the positions for circles, grouped by up/bottom
    circle_pos_up = [
        (- width_rectangle / 2, height_rectangle / 2),
        (width_rectangle / 2, height_rectangle / 2)
    ]

    circle_pos_bottom = [
        (- width_rectangle / 2, - height_rectangle / 2),
        (width_rectangle / 2, - height_rectangle / 2)
    ]

    print(circle_pos_up, circle_pos_bottom)

    # Define the circles
    circles = []

    for p in circle_pos_up:
        i_circle = stimuli.Circle(
            radius = circle_radius,
            position = p,
            colour = (255, 255, 255)    # Up colors are black
        )
        circles.append(i_circle)

    for p in circle_pos_bottom:
        i_circle = stimuli.Circle(
            radius = circle_radius,
            position = p,
            colour = (0, 0, 0)    # Up colors are white
        )
        circles.append(i_circle)

    # Preparation of stimuli completed

    control.start(exp)

    # Clear the screen
    exp.screen.clear()

    # Present the circles
    for i in circles:
        i.present(update = False, clear = False)

    # Present the square
    rectangle.present(update = True, clear = False)

    exp.keyboard.wait()

    control.end(exp)

kanizsa()