import sched, time
from StateMachine import *
from Signal import *
def integral(x):
    def integralFN(i, s, dt):
        c = s + i * dt
        print str(i) + " " + str(s)
        return c, c
    
    return StateMachineF(0, integralFN, maybeLift(x), 0)
def engine(s):
    s = maybeLift(s)
    rs = s.start()
    for t in range(5):
        print "Time is: " + str(t) + " Value is " + str(rs.now)
        rs.refresh(1)
    
def maybeLift(x):
    t = type(x)
    if t is type(1):
        return Lift0(x)
    if t is type(1.0):
        return Lift0(x)
    return x
i1 = integral(1)
i2 = integral(i1)
#engine(i1)
engine(i2)
"""
Notes:
init is state
get rid of alive
maybe make signal abstract

change the refresh
   state transition function
    input signal in the constructor
    
"""
