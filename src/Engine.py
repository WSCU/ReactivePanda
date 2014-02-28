import unittest
import sched, time
#from StateMachine import *
from Signal import *
from Functions import *
from Globals import *

   
def engine(signals, events, steps=10):
    #Initialize all signals (signalF.start)
    #set the time to 0
    #get events and clear thunks
    runningSignals = {}
    for k,v in signals.iteritems():
        runningSignals[k] = maybeLift(v).start()
    Globals.currentTime = 0
    Globals.dt = 1
    while Globals.currentTime < steps:
        #Globals.thunks = []
        if (events and Globals.currentTime >= events[0][0]):
            print ("An event was popped " + str(events[0][1]))
            Globals.events.append(events.pop(0))
        for k,v in runningSignals.iteritems(): #k = key, v = value in the dictionary
            print(str(k)+ " = "+str(v.now()))
        for f in thunks:
            f()
            
        Globals.thunks = [] 
        print("reactive engine time = "+ str(Globals.currentTime))    
        Globals.currentTime = Globals.currentTime+ Globals.dt
    

e = [(5, simkey("x", 7))]

#h = {"sk" : hold(key("x", 2), 0)}

i1 = integral(1)
i2 = integral(i1)
#engine(i1)
signals = {}
signals["i2"]=i2
signals["sk"] = hold(key("x", 2), 0)
engine(signals, e)


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
