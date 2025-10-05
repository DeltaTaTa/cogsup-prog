from expyriment import design, control, stimuli
import random

def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(stims):
    t0 = exp.clock.time

    exp.screen.clear()
    for stim in stims:
        stim.present(clear = False, update = False)

    exp.screen.update()

    return exp.clock.time - t0
    # return the time it took to draw

# Draw and keep stimuli on-screen for time t in ms (be mindful of edge cases!)
def present_for(stims, t=1000):
    # Clear the screen
    exp.screen.clear()

    for stim in stims:
        stim.present(clear = False, update = False) #Draw stimuli in the buffer

    t0 = exp.control.clock
    # Update the screen
    exp.screen.update()
    dt = exp.clock.time - t0
    exp.clock.wait(1000 - dt)




""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemneted correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()