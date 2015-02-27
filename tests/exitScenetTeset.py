from ReactivePanda.Panda import *

panda()
dragon()


def newGame():
    bee(hpr = hpr(time,0,0))
def fn():
    resetWorld(newGame)


atTime(3, fn)

def shoot(m,v):
    soccerball(position = p3(localTime,0,0))

react(clock(.5), shoot)

start()