from PandaSRC.Panda import *
sphere(size=-500,texture='nebula.jpg', hpr=hpr(time-2,time-2,time-2))

pandaX = 0
pandaY = -(time/20)+10
pandaZ = 0
pandaH = 40
pandaP = 0
pandaR = 0

p = photoWheel(["Nametag1.jpg","Nametag2.jpg","Nametag3.jpg","Nametag4.jpg","Nametag5.jpg"])
p.texture='earthlights.jpg'
p.hpr = hpr(time, time+1, time-1)

def randomPanda(m, v):
 if (random01()<.2):
  p0=p3((randomRange(-2,2)),(randomRange(-2,2)),(randomRange(-2,2)))
  v=p3((randomRange(-2.5,2.5)*localTime),(randomRange(-2.5,2.5)*localTime),(randomRange(-2.5,2.5)*localTime))

  p=photoWheel(["Avatar realistic me.png","Avatar realistic me.png"],\
    position =p0+integral(v), size =randomRange(.3,.75), duration = 1.5)

  p.color=color(sin(time*time*3),cos(time*random01()),cos(time))
  p.hpr = hpr(time/time*random01(), 6*random01(), -4.5*time*random01())
c = alarm(.08)
react(c, randomPanda)
start()