from Panda import *

world.color = black
panda()
#ambientLight(color = color(.3,.3,.3))
#directionalLight(color = white, hpr = hpr(time, 0, 0))
pointLight(position = sliderP3(min = -3, max = 3))

start()