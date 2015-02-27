from ReactivePanda.Panda import *

grassScene()
p = panda()
heading = integral(getX(mouse))
vel = p3C(1, heading, 0)
p.position = integral(vel)
pointForward(p)
flatRod(camera, p)
start()
