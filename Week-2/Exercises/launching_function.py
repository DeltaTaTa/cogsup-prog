from expyriment import design, control, stimuli

def launching(gap_temp, gap_spac, triggering):

    

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
    step_size_left = 10 # pixels per update

    if triggering == True:
        step_size_right = 30
    else:
        step_size_right = step_size_left


    if gap_spac == True:
        spatial_gap = 50
    else:
        pass


    # Move left square until collision
    while square_right.position[0] - square_left.position[0] > 50 + spatial_gap:
        square_left.move((step_size_left, 0)) # (move-x, move-y)
        square_left.present(clear = True, update = False)
        square_right.present(clear = False, update = True)
    
    if gap_temp == True:
        exp.clock.wait(2000)
    else:
        pass

    # Move right square after collision
    while square_right.position[0] < displacement_x:
        square_right.move((step_size_right, 0))
        square_right.present(clear = True, update = False)
        square_left.present(clear = False, update = True)
        