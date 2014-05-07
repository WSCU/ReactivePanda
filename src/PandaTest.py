from panda import *

#mFile = Filename("/c/Panda3D-1.8.1/models/panda-model.egg.pz")
#print "File Path: " + repr(mFile)
"""
pandaObject = loader.loadModel(mFile)
pandaObject.setScale(0.05)
pandaObject.setPos(0,200,0)
pandaObject.reparentTo(render)
#pandaObject.setScale(0.25, 0.25, 0.25)
"""
#camera.setPos(100,0,0)
a = panda(size = 0.05, hpr = hpr(-1,0,1), position = P3(sin(integral(2)),5,cos(integral(2))))
#b = panda(size = 0.05, hpr = HPR(integral(2),-.75,0), position = P3(1,10,-.1*integral(2)))
#c = panda(position = P3(sin(integral(.2)),5+integral(10),cos(integral(.2))), hpr = HPR(integral(1),integral(.5),integral(1)))
#d = boy(position = P3(1,1,integral(2)), hpr = HPR(1,0,0))
#bee = bee()
#run()
#t = text(text = "We're like testing texting and stuff")
#camera.setPos(0,-10,0)

a = panda(size = 0.05, position = P3(-5 + integral(1), 0, 0))
b = panda(size = 0.05, position = P3(5 - integral(1), 0, 0))
hit(a, b)

start()
