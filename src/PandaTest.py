import Engine
import Globals as g
from Functions import time
from PandaModels import *
from Functions import *


b = panda(position = P3(time,0,0))

camera.setPos(0,-10,0)

Engine.engine(time)
