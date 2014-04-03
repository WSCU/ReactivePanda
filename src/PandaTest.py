import Engine
import Globals as g
import time as t
from PandaModels import *
from Functions import *


ti = t.time()
print ti
x0=0
dx = 1.00
y0 = 0
dy = 1.00
z0 = 0
dz = 1.00

def f(k):
    return P3(x0+dx*k, y0+dy*k, z0+dz*k)

b = panda(position = f(ti))

camera.setPos(0,-10,0)

Engine.engine(ti)
