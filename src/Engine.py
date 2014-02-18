import unittest
import sched, time
from StateMachine import *
from Signal import *

def integral(x):
    def integralFN(i, s, dt): #Euler method for integration
    # state s is the previous value of the integral
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




class Lift(Signal):
    def __init__(self, f, args):
    	Signal.__init__(self)
        self.f = f
        self.args=args
    def now(self):
    	ea = map (lambda a: a.now() , self.args)
    	return self.f(*ea)
    
# Signal Factory Class
# Base Signal Factory class
# extends to StateMachineF, LiftF, and Lift0F
class SFact:
	def __init__(self):
		self.type = "factory"
	def __add__(self,x,y):
		y=maybeLift(y)
		return LiftF(lambda x,y:x+y, [x,y])
	
class LiftF(SFact):
	def __init__(self,f, args):	
		SFact.__init__(self)
		self.f=f 
		self.args = args
	def start(self):
		return Lift(f,map(lambda x: x.start(), args))

def lift(f):
	def fn(*args):
		return LiftF(f,args)
	return fn	

class StateMachineF:
    def __init__ (self, initState, f, s, initV):
        self.state = initState
        self.f = f
        self.s = s
        self.initV = initV
    def start(self):
        return StateMachine(self.state, self.f, self.s.start(), self.initV)


#Base signal class
class Signal:
	def __init__(self):
		self.type = "Signal"
		
class StateMachine(Signal):
    def __init__ (self, initState, f, s, initV):
        Signal.__init__(self)
        self.state = initState
        self.f = f
        self.s = s
        print repr(s)
        self.now = initV
    def now(self):
        n = self.s.now()
        s, output = self.f(self.s.now, self.state, dt) 
        self.state = s
        self.now = output
        #print "refresh state machine"
	



####################  Testing ################################
# Here's our "unit".

def IntegralTest1():
    count = 0 
    a = [0,1,2,3,4,5]
    s = integral(1)
    rs = s.start()
    for t in a:
        if t!=rs.now:
            return False
        rs.refresh(1)
    return True

def IntegralTest2():
    count = 0 
    a = [0,1,3,6,10]
    s1 = integral(1)
    s2 = integral(s1)
    rs = s2.start()
    for t in a:
        if t!=rs.now:
            return False
        rs.refresh(1)
    return True



class TestEngine(unittest.TestCase):

    def test_Integral1(self):
        self.failUnless(IntegralTest1())
        
    def test_Integral2(self):
        self.failUnless(IntegralTest2())
        

engineTestSuite = unittest.TestSuite()
engineTestSuite = unittest.TestLoader().loadTestsFromTestCase(TestEngine)
#unittest.TextTestRunner(verbosity=2).run(engineTestSuite)
