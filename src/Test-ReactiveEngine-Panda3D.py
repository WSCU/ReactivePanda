import Engine
import Globals as g
from Functions import time
from PandaModels import *
from Functions import *
from StaticNumerics import cos, sin, pi
from direct.actor import Actor
import direct.directbase.DirectStart
from panda3d.core import Filename

#"Sanity check" testing scenarios will go here

#place panda on the screen 
b = panda(position = P3(2,0,2), hpr = HPR(0,-.75,0))

Engine.engine(0)
