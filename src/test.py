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
ir2 = input1(2) #get rid of these 

f = lift("lift", lambda b: 0 if b else 1) #turns signal from ir into 0 or 1 whether person is there or not
count = f(ir0)*.6 + f(ir1)*.6 + f(ir2)*.6 + .3 #the rate at which the lights change, fastest flash would be all numbers added up 
r = integral(count) #turn the rate at which the lights are moving into a current light position, turns rate into a value
s = integerize(r % 7) #every time the r goes up by 1 the lights move. Every time we get to 7 we start back over again
for i in range(6):
    output(pin = i, on =(s <= i), name = "light " + str(i)) #add +2 when rewire
PiEngine.engine(ti)
