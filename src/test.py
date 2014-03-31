import PiEngine
import Globals as g
import time as t
from PiObjects import *
from Functions import *
ti = t.time()
print ti
"""
ir0 = input1(0)
output(0, ir0, name = 'lights0')
output(1,ir0,name = 'lights1')

ir1 = input1(1)
output(2, ir1, name = 'lights2')
output(3,ir1,name = 'lights3')

ir2 = input1(2)
output(4, ir2, name = 'lights4')
output(5,ir2,name = 'lights5')
#print repr(o) """

#print str(g.worldObjects)
ir0 = input1(0)
ir1 = input1(1)
ir2 = input1(2)

f = lift("lift", lambda b: 1 if b else 0)
count = f(ir0) + f(ir1) + f(ir2)
r = integral(count)
s = int((r / .1) % 6)
for i in range(6):
    output(pin = i, on = s == i, name = "light " + i)
PiEngine.engine(ti)
