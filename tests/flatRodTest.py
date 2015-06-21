from ReactivePanda.Panda import *

grassScene()
p = panda()
heading = integral(getX(mouse),0)
vel = p3c(1, heading, 0)
p.position = integral(vel,0)
pointForward(p)
flatRod(camera, p)
start()
