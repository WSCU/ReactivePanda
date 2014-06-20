import Errors
import Globals
import sys
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Signal Factory Class
# Base Signal Factory class
# extends to StateMachineF, LiftF, and Lift0F

from Signal import *
from Types import *

def maybeLift(x):
    t = type(x)
    if t is type(1):
        return Lift0F(x, numType)
    if t is type(1.0):
        return Lift0F(x, numType)
    if t is type(" "):
        return Lift0F(x, stringType)
    if t is type(True):
        return Lift0F(x, boolType)
    t = x._type

    if t is signalFactoryType:
        #print "if this is not happening we are in trouble: "+str(t)+" and: " +str(x.name)
        return x
    if t is p3Type:
        return Lift0F(x, t)
    #print "Lifting: "+str(x)+" :: " +str(t)
    return Lift0F(x,t)
    #return x
def lift(name, f, types = [], outType = anyType):
    def fn(*args):
        #print str(len(types)) + " " + str(len(args))
        Errors.checkNumArgs(len(types), len(args), "ProxyObject", name)
        for arg in args:
            # print("lift: " + str(arg))
            if isinstance(arg, SFact):
                return LiftF(name,f,args,types = types, outType = outType)
        if len(types) is not 0:
            for i in range(len(args)):
                #print "checking " + repr(args[i])
                checkType("ProxyObject", name, args[i], types[i])
        return f(*args)
    return fn

class SFact:
    def __init__(self):
    	self._type = signalFactoryType
    def __add__(self,y):
        y = maybeLift(y)
        return LiftF("add",lambda x,y:x+y, [self,y], types = [self.outType, y.outType], outType = self.outType)
    def __radd__(self,y):
        y = maybeLift(y)
        return LiftF("add",lambda x,y:x+y, [self,y], types = [self.outType, y.outType], outType = self.outType)
    def __sub__(self,y):
        y = maybeLift(y)
        return LiftF("subtract",lambda x,y:x-y, [self,y], types = [self.outType, y.outType], outType = self.outType)
    def __rsub__(self,y):
        y = maybeLift(y)
        return LiftF("subtract",lambda x,y:y-x, [self,y], types = [self.outType, y.outType], outType = self.outType)
    def __mul__(self,y):
        y = maybeLift(y)
        return LiftF("multiply",lambda x,y:x*y, [self,y])
    def __rmul__(self,y):
        y = maybeLift(y)
        return LiftF("multiply",lambda x,y:x*y, [self,y])
    def __div__(self, y):
        y = maybeLift(y)
        return LiftF("div", lambda x,y: x/y, [self, y])
    def __rdiv__(self, y):
        y = maybeLift(y)
        return LiftF("div", lambda x,y: y/x, [self, y])
    def __lt__(self, y):
        y = maybeLift(y)
        return LiftF("less than", lambda x,y: x < y, [self, y])
    def __le__(self, y):
        y = maybeLift(y)
        return LiftF("less than or equal to", lambda x,y: x <= y, [self, y])
    def __eq__(self, y):
        y = maybeLift(y)
        return LiftF("equal", lambda x,y: x == y, [self, y])
    def __ne__(self, y):
        y = maybeLift(y)
        return LiftF("not equal", lambda x,y: x != y, [self, y])
    def __gt__(self, y):
        y = maybeLift(y)
        return LiftF("greater than", lambda x,y: x > y, [self, y])
    def __ge__(self, y):
        y = maybeLift(y)
        return LiftF("greater than or equal", lambda x, y: x >= y, [self, y])
    def __mod__(self, y):
        y = maybeLift(y)
        return LiftF("mod", lambda x, y: x % y, [self, y])
    def __int__(self):
        return self // 1
    def __abs__(self):
        return LiftF("abs", lambda x: abs(x), [self])
    def __and__(self, y):
        y = maybeLift(y)
        return LiftF("and", lambda x, y: x & y, [self, y])
    def __or__(self, y):
        y = maybeLift(y)
        return LiftF("and", lambda x, y: x | y, [self, y])
        
#Creates a Lift Factory
class LiftF(SFact):
    def __init__(self,name,f, args, types = [], outType = anyType):
        SFact.__init__(self)
        self.f=f
        self.types = types
        self.outType = outType
        self.name=name
        self.args = args


    def __str__(self):
        return "{0} - args: {1} - types: {2} - outType: {3}".format(str(self.name), map(str, self.args), map(str, self.types), str(self.outType))

    def start(self, expectedType = anyType, obj = "ProxyObject"):
        #print self.name
        #for arg in self.args:
            #print " " + repr(arg)
        # Type Checking
        # List contains arg types with the last type in the list represents the expected return type
        #print self.outType
        #print expectedType
        self.args = list(self.args)
        argsLen = len(self.args)
        addCheck(self)
        checkType(obj, self, self.outType, expectedType)
        Errors.checkNumArgs(len(self.types), argsLen, obj, self)
        for i in range(len(self.types)):
            self.args[i] = maybeLift(self.args[i])
            checkType(obj, self, self.types[i],self.args[i].outType) # individual argument type check
        ea = map(lambda x: maybeLift(x).start()[0], self.args)
        return Lift(self.name,self.f, ea), self.outType

class Lift0F(SFact):
      def __init__(self, v, t):
          SFact.__init__(self)
          self.outType = t
          self.name = "Lift0"
          self.v = v
      def start(self, expectedType = anyType):
          if expectedType.includes(self.outType):
              return Lift0(self.v), self.outType
          else:
              Globals.error += "\n in Factory line 130, expected to be " + str(expectedType) + " but is a " + str(self.outType)
              print Globals.error
          Globals.error = ""

#Creates a CachedValue factory
class CachedValueF(SFact):
    def __init__(self, i):
        SFact.__init__(self)
        self.outType = anyType
        self.i = i
    def start(self, expectedType = anyType):
        return CachedValue(maybeLift(self.i)), self.outType

#Creates a State Machine Factory
class StateMachineF(SFact):
    def __init__(self, s0, i, f):
        SFact.__init__(self)
        self.state = s0
        self.outType = anyType
        self.i = i
        self.name = "State Machine Factory"
        self.f = f
    def start(self, expectedType = anyType):
        #print "initilizing state Machine " + repr(self.i)
        input = self.i.start(expectedType = anyType)[0]
        #print "state machine input: " + repr(input)
        return StateMachine(self.state, input, self.f), self.outType

#Creates a Observer Factory
class ObserverF(SFact):
    def __init__(self, f, type = anyType):
        SFact.__init__(self)
        self.f = f
        self.outType = type
        self.name = "ObserverF"
    def start(self, expectedType = anyType):
       # print "starting observer"
        ro =  Observer(self.f)
        ro.startTime = Globals.currentTime
        return ro , self.outType
    def get(self):
        return self.f(self)

def eventObserver(eName, eVal = None):
    def getEvent(ename):
#        print "Observing " + eName
        if Globals.events.has_key(ename):
#            print "Event found:" + str(Globals.events[ename])
            return EventValue(Globals.events[ename]) if eVal is None else EventValue(eVal)
#        print "No: " + str(noEvent)
        return noEvent
    return ObserverF(lambda x: getEvent(eName))
