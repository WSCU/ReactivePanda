import Engine
import Globals as g
from Functions import time
from PandaModels import *
from Functions import *
from direct.actor import Actor
import direct.directbase.DirectStart
from panda3d.core import Filename

mFile = Filename("/c/Panda3D-1.8.1/models/panda-model.egg.pz")
print "File Path: " + repr(mFile)
"""
pandaObject = loader.loadModel(mFile)
pandaObject.setScale(0.05)
pandaObject.setPos(0,200,0)
pandaObject.reparentTo(render)
#pandaObject.setScale(0.25, 0.25, 0.25)
"""
#camera.setPos(100,0,0)
#b = panda(position = P3(1,1,integral(2)), hpr = HPR(0,-.75,0))
c = panda(position = P3(1,5+integral(5),1), hpr = HPR(integral(1),integral(.5),integral(1)))
#d = boy(position = P3(1,1,integral(2)), hpr = HPR(1,0,0))
#run()


#camera.setPos(0,-10,0)

Engine.engine(0)
