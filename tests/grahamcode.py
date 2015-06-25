from ReactivePanda.Panda import *

world.color = red
b = spiderman(position = p3(0,30,-1))
s = sound("DOIT.wav")

def timeToStart(m,v):
    b.play("DOIT!")
    atTime(now(time)+3.5, s.play)

react(lbp(),timeToStart)

start()
