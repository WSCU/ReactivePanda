from PandaSRC.Panda import *

camera.position=p3(0,-10+localTime/6,0)

directionalLight(hpr=hpr(0,time/pi/2,0),color=tan)
ambientLight(color=color(sin(time/pi),sin(time/pi),sin(time/pi)))

def tank(**a):
    p = pandaModel("Brian Blender Tank.egg", **a)
    p.texture = "tex.jpg"
    return p

tank(position = p3(0,0,-.1), hpr = hpr(time/2, 0,0))


rectangle(p3(-15,-15,-1), p3(15,-15,-1), p3(-15,15,-.05), texture=("Dirt-image.jpg"))

sphere(size=-100,texture=("tex"),hpr=hpr(0,time/pi/2,0))


start()
