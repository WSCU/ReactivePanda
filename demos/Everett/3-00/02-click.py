# Create a simple game using click detection.  Use clock to generate objects

from Panda import *

# Place a random panda on the screen.  If clicked, it goes away.
# leftClick is an event that happens when a particular model is clicked on

score = var(0)

text(score)

def getPoints(m, v):
    score.add(1)
    exit(m)

def losePoints(m, v):
    score.sub(1)
    exit(m)

def randomPanda(m, v):
    if (random01() < .7):
        p = panda(position = p3(3*random01(), 0, 2*random01()), size = .2, duration = 2)
        react(p, leftClick(p), losePoints)
    else:
        p = jeep(position = p3(3*random01(), 0, 2*random01()), size = .2, duration = 2)
        react(p, leftClick(p), getPoints)

# Alarm generates an event at a given timestep (step)

c = clock(0.8)
react(c, randomPanda)

start()
