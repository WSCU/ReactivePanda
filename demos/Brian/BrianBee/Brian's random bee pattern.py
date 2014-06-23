from Panda import *

volleyBall(position=p3(0,3,0),size=.6)

world.color=darkGreen
ambientLight(color=color(1,1,1))

c=clock(.1, start = 0, end = 10)

def r(m,v):
    bee(position=p3(sin(localTime*pi*1.3*random01()),sin(localTime*pi*random01()),sin(localTime*pi))*random01(),size=.2)

react(c,r)

start()
