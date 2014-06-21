from Panda import *

grassScene()
boyBalloon(position = p3(0,0,sin(time)/3-1))
dragon(position = p3(-3,5,-2), hpr=hpr(-5,0,0), size=4)
bee(position = p3(1.1*sin((time)-pi) , -1.1*cos((time)-pi), -0.88), hpr = hpr((time),0,0), color= cyan, size = .5)
panda(position = p3(0,0,-1), hpr = hpr((time),10,0), color=pink)
fireish(position = p3(0,0,-1.5), size = .15)

start()