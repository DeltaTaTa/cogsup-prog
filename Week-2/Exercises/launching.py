"""
3A: Michottean launching
Check out the first video at this link, under Launching and simple non-causal events. Duplicatetwo_squares.py in the same Assignments/Week-2/Exercises subfolder and rename it to launching.py. Modify the code as follows:

Present the two squares side by side for 1 second but modify their positions such that:
the red square starts on the left side, 400 pixels left from the center
the green square starts at the center
Using the position attribute or the move method, animate the left square to move to the left until it reaches the green square. Adjust the speed to approximately match the one in the video.
Once the red square reaches the green square, the green square should move to the right, at the same speed and for the same amount of time as the red square.
Show this display for 1 second.
Add explanatory comments at each step in the script.
Do you get the impression that the red square causes the green square to move?

Things to consider:

How do I move a square to the left at a given speed?
How do I encode the collision moment between the two squares?

"""

from expyriment import design, control, stimuli

# Create an Experiment object
exp = design.Experiment(name="launching")
control.initialize(exp)

# Define colours and size
color_red = (255, 0, 0)
color_green = (0, 255, 0)
shape_size = (50, 50)

# Create squares
# Red starts 500 px left of center
square_left = stimuli.Rectangle(colour=color_red, 
                                size=shape_size, 
                                position=(-400, 0))

# Green starts at the center
square_right = stimuli.Rectangle(colour=color_green, 
                                 size=shape_size, 
                                 position=(0, 0))

# Start experiment
control.start(subject_id=1)

# Set presentation duration
exp.clock.wait(1000)

# Distance to travel = Initial distance between objects
displacement_x = 400

# Set speed
step_size = 10 # pixels per update


# Move left square until collision
while square_right.position[0] - square_left.position[0] > 50:
    square_left.move((step_size, 0)) # (move-x, move-y)
    square_left.present(clear = True, update = False)
    square_right.present(clear = False, update = True)
# Don't forget to update the screen!
# Move right square the same amount

# Move right square after collision
while square_right.position[0] < displacement_x:
    square_right.move((step_size, 0))
    square_right.present(clear = True, update = False)
    square_left.present(clear = False, update = True)
    