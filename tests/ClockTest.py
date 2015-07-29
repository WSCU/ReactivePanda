from ReactivePanda.Panda import *
# Tests reactive time step for clock

s = slider(min = .1, max = 2, init = .5)
text(s)

def shoot(m,v):
    panda(position = integral(p3(1,0,0), p3(-2,0,0)))

react(clock(s), shoot)
start()
