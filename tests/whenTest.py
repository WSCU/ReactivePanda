from Panda import *

# Test the when1 function.  The panda should move left / right
p = panda(position = p3(time, 0, 0))

def r1(m, v):
    p.position = now(p.position) + p3(localTime,0,0)
    g = getX(p.position) > 2
    when1(p,g, r2)

def r2(m, v):
    p.position = now(p.position) + p3(-localTime,0,0)
    when1(p, getX(p.position) < -1, r1)

react1(p,delay(1), r1)

start()
