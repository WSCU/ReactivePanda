import PandaEngine
import Globals as g
from Functions import time
from PandaModels import *
from Light import *
from Functions import *
from PandaStaticNumerics import cos, sin, pi
from direct.actor import Actor
import direct.directbase.DirectStart
from panda3d.core import Filename

#"Sanity check" testing scenarios will go here

#place panda on the screen 
#b = panda(position = P3(2,0,2), hpr = HPR(0,-.75,time), size = .5)
#b = panda(position = P3(0,0,0))

#p = panda(position = P3(integral(1), integral(1), integral(1)))
#a = ambientLight(color24(100,100,100))
p = pointLight(color24(100,100,100))
PandaEngine.engine(0)
