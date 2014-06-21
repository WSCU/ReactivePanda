import Globals
from Panda import *
# Prints a message when the two models touch

b = soccerBall(position = p3(-2, 0, 0))

b1 = panda(position = p3(3*getX(mouse),0,3*getY(mouse)))

def r(m,v):
    print str(m) + " hits " + str(v) + " at " + str(Globals.currentTime)
hit(b, b1, r)
start()
