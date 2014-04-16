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
        return Lift0F(x)
    if t is type(1.0):
        return Lift0F(x)    
    return x
    
def lift(name, f, types = [], outType = anyType):
	def fn(*args):
		return LiftF(name,f,args,types = types, outType = outType)
	return fn
	

class SFact:
    def __init__(self):
    	self._type = signalFactoryType
    def __add__(self,y):
        y = maybeLift(y)
        atype = y.outType
        stype = self.outType
        if stype.addable:
            if stype.infer(atype):
                return LiftF("add",lambda x,y:x+y, [self,y])
            else:
                print "Tried adding non-matching types: " + self.name + ", Type: " + str(stype) + " and " + str(atype)
        else:
            print self.name + "does not have an addable type. Type: " + str(stype)
    def __radd__(self,y):
        y = maybeLift(y)
        atype = y.outType
        stype = self.outType
        if stype.addable:
            if stype.infer(atype):
                return LiftF("add",lambda x,y:x+y, [self,y])
            else:
                print "Tried adding non-matching types: " + self.name + ", Type: " + str(stype) + " and " + str(atype)
        else:
            print self.name + "does not have an addable type. Type: " + str(stype)
    def __sub__(self,y):
        y = maybeLift(y)
        atype = y.outType
        stype = self.outType
        if stype.addable:
            if stype.infer(atype):
                return LiftF("subtract",lambda x,y:x-y, [self,y])
            else:
                print "Tried subtracting non-matching types: " + self.name + ", Type: " + str(stype) + " and " + str(atype)
        else:
            print self.name + "does not have an addable type. Type: " + str(stype)
    def __rsub__(self,y):
        y = maybeLift(y)
        atype = y.outType
        stype = self.outType
        if stype.addable:
            if stype.infer(atype):
                return LiftF("subtract",lambda x,y:y-x, [self,y])
            else:
                print "Tried subtracting non-matching types: " + self.name + ", Type: " + str(stype) + " and " + str(atype)
        else:
            print self.name + "does not have an addable type. Type: " + str(stype)
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
#Creates a Lift Factory	
class LiftF(SFact):
    def __init__(self,name,f, args, types = [], outType = anyType):
        SFact.__init__(self)
        self.f=f
        self.types = types
        self.outType = outType
        self.name=name
        self.args = args

    def start(self, expectedType = anyType):
        #print self.name 
        #for arg in self.args:
            #print " " + repr(arg)
        # Type Checking
        # List contains arg types with the last type in the list represents the expected return type
        #print self.outType
        #print expectedType
        self.args = list(self.args)
        if  expectedType.infer(self.outType): # Return type check
            if len(self.types) is 0 or len(self.args) is len(self.types): # number of arguments check
                failed = False
                for i in range(len(self.types)):
                    self.args[i] = maybeLift(self.args[i])
                    if not self.types[i].infer(self.args[i].outType): # individual argument type check
                        failed = True
                        print "Argument in " + self.name + " expects to be " + str(self.types[i]) + " but is a " + str(self.args[i].outType)
                if not failed:
                    ea = map(lambda x: maybeLift(x).start(), self.args)
                    return Lift(self.name,self.f, ea), self.outType
            else:
                print "Incorrect number of arguments in " + self.name
        else:
            print "Expected " + str(expectedType) + " in " + self.name + ", recieved " + str(self.outType)

class Lift0F(SFact):
      def __init__(self, v):
          SFact.__init__(self)
          self.outType = type(v)
          self.name = "Bendicks"
          self.v = v
      def start(self, expectedType = anyType):
          if expectedType.infer(self.outType):
              return Lift0(self.v), self.outType
          else:
              print "Expected " + str(expectedType) + " in " + self.name + ", recieved " + str(self.outType)

#Creates a CachedValue factory
class CachedValueF(SFact):
    def __init__(self, i):
        SFact.__init__(self)
        self.outType = anyType
        self.i = i
    def start(self, expectedType = anyType):
        return CachedValue(maybeLift(self.i)), self.outType

#Creates a State Machine Factory
class StateMachineF(CachedValueF):
    def __init__(self, s0, i, f):
        SFact.__init__(self)
        self.state = s0
        self.outType = anyType
        self.i = i
        self.f = f
    def start(self, expectedType):
        return StateMachine(self.state, self.i.start(anyType), self.f), self.outType

#Creates a Observer Factory
class ObserverF(CachedValueF):
    def __init__(self, f):
        SFact.__init__(self)
        self.f = f
        self.outType = anyType
    def start(self, expectedType = anyType):
        return Observer(self.f), self.outType
    
def eventObserver(eName, eVal = None):
    def getEvent():
        if Globals.events.has_key(ename):
            return events[ename] if eVal is None else eVal
        return None
    return ObserverF(lambda: getEvent(eName))
