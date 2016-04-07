from PandaSRC.Panda import *


ambientLight(color = color (.5,.5,.5))
directionalLight(color = orange, hpr = hpr(0,3,0))

def throwButt(m, v):
    tex = randomChoice(["butt.png", "buttORANGE.png", "buttMEH.png", "buttBLUEE.png"])
    s = pandaModel("Butt.egg", animation = {"fly":"Butt-Fly.egg"},
    texture = tex,position = integral(p3(random01()*-3,random01()*2,0), p3(random11()*5, random11()*4, -1)), size = .1,duration = 5,
    hpr=hpr(random11()*3,0,0))
    loopAnim(s)
    
react(clock(2), throwButt)

world.color = lightBlue
volcano(position = p3(0,0,-2.2), size = 1.5)
d = -2.3
rectangle(p3(-25,-25,d), p3(-25, 25, d), p3(25, -25, d), texture = "grass")
neck = p3(0,0,.4)

def erupt(m,v):
    h = randomRange(0,2*pi)
    p = randomRange(degrees(35), degrees(50))
    s = sphere(color = orange, size=randomRange(.07,.3))
    launch(s, neck, hprToP3(hpr(h,p,0))*3)
    when(s, getZ(s.position) <= -2, flower1)

world.gravity = p3(0,0,-1)

def flower1(m,v):
    exit(m)
    fp = now(m.position)
    path = at(now(m.position)+p3(0,0,-1)) + to(1, now(m.position))
    pandaModel("flower#3", texture="flowerPurple.png", position = interpolate(localTime, path))
    if random01() < .3:
        ep = p3(random11()*25, random11()*25, 6)
        bpath = at(fp + p3(0,0,2))  + to(1.5, fp+p3(0,0,.7)) + to(6, ep)
        tex = randomChoice(["butt.png", "buttORANGE.png", "buttMEH.png", "buttBLUEE.png"])
        s = pandaModel("Butt.egg", animation = {"fly":"Butt-Fly.egg"},
           texture = tex,
           position = interpolate(localTime, bpath),
           size = .1,duration = 7.5,
           hpr=hpr(random11()*3,0,0))
        loopAnim(s)




react(clock(.2), erupt)
h=time/4
camera.position = p3c(25,h,1)
camera.hpr = hpr(h + pi/2,0,0)

start()