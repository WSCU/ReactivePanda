from ReactivePanda.Panda import *

world.color = green
b = spiderman(position = p3(0,30,-1))
pose(b,"DOIT!",frame=0)
s = sound("DOIT.wav")

def resetPose():
    pose(b,"DOIT!",frame=0)

def timeToStart(m,v):
    playAnim(b,"DOIT!")
    atTime(now(time)+3.5, s.play)
    atTime(now(time)+6,resetPose)

react(lbp(),timeToStart)

start()
