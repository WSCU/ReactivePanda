import unittest
import sched, time
#from StateMachine import *
from Signal import *
from Functions import *
from Globals import *

clock = Clock()
   
def engine():
    while Globals.currentTime < 1000:
        for s in sl:
            print(repr(s))            
            s.now()
        clock.now()
        #Globals.currentTime = Globals.currentTime + 1
        print(str(Globals.currentTime))
        print(str(s.now()))
    
    
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
sl.append(i2.start())
engine()



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
