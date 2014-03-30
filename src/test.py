import PiEngine
import Globals as g
import time as t
from PiObjects import *

ti = t.time()
print ti

ir = input1(1)
output(1,ir,name = 'lights1')

print str(g.worldObjects)

PiEngine.engine(ti)
