import Engine
import Globals as g
from Functions import time
from PandaModels import *
from Light import *
from Functions import *
from StaticNumerics import cos, sin, pi
from direct.actor import Actor
import direct.directbase.DirectStart
from panda3d.core import Filename

#"Sanity check" testing scenarios will go here

#place panda on the screen 
#b = panda(position = P3(2,0,2), hpr = HPR(0,-.75,integral(1)), size = .5)

#p = panda(position = P3(integral(1), integral(1), integral(1)))
#a = ambientLight(color24(100,100,100))
d = directionalLight(color24(100,100,100), hpr = HPR(0,-1,0))
Engine.engine(0)
