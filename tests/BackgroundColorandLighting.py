from Panda import *

world.color = cyan
panda()
ambientLight(color = color(.3,.3,.3))
directionalLight(color = white, hpr = hpr(time, 0, 0))
#pointLight(position = p3(0,0,0))

start()