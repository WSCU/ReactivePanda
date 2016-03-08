from PandaSRC.Panda import *
# Tests reactive time step for clock
s = slider(min = .1, max = 2, init = .5)
text(s)

def shoot(m,v):
    panda(position = integral(p3(-1,sin(time),0), p3(cos(time),0,sin(time))),hpr=hpr(1,sin(time),-2))

react(clock(s), shoot)
start()
