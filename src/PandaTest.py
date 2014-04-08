#import Engine
#import Globals as g
#from Functions import time
#from PandaModels import *
#from Functions import *
from direct.actor import Actor
import direct.directbase.DirectStart
from panda3d.core import Filename

mFile = Filename("/c/Panda3D-1.8.1/models/panda-model.egg.pz")
print "File Path: " + repr(mFile)
pandaObject = loader.loadModel(mFile)
pandaObject.setScale(0.025)
pandaObject.setPos(.5,0,0)
pandaObject.reparentTo(render)
#pandaObject.setScale(0.25, 0.25, 0.25)

run()
#b = panda(position = P3(time,0,0))

#camera.setPos(0,-10,0)

#Engine.engine(time)
