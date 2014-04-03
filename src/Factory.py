# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Signal Factory Class
# Base Signal Factory class
# extends to StateMachineF, LiftF, and Lift0F

from Signal import * 

def maybeLift(x):
    t = type(x)
    if t is type(1):
        return Lift0F(x)
    if t is type(1.0):
        return Lift0F(x)
    
    return lift(x)
    
def lift(name,f):
	def fn(*args):
		return LiftF(name,f,args)
	return fn
	

class SFact:
    def __init__(self):
    	self.type = "factory"
    def __add__(self,y):
        y=maybeLift(y)
        return LiftF("add",lambda x,y:x+y, [self,y])
    def __radd__(self,y):
        y=maybeLift(y)
        return LiftF("add",lambda x,y:x+y, [self,y])
    def __sub__(self,y):
        y=maybeLift(y)
        return LiftF("subtract",lambda x,y:x-y, [self,y])
    def __rsub__(self,y):
        y=maybeLift(y)
        return LiftF("subtract",lambda x,y:y-x, [self,y])
    def __mul__(self,y):
        y=maybeLift(y)
        return LiftF("multiply",lambda x,y:x*y, [self,y])
    def __rmul__(self,y):
        y=maybeLift(y)
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
    def __init__(self,name,f, args):
        SFact.__init__(self)
        self.f=f
        self.name=name
        self.args = args

    def start(self):
        #print self.name
        #for arg in self.args:
            #print " " + repr(arg)
        ea = map(lambda x: maybeLift(x).start(), self.args)
        return Lift(self.name,self.f, ea)

class Lift0F(SFact):
      def __init__(self, v):
          SFact.__init__(self)
          self.v = v
      def start(self):
          return Lift0(self.v)

#Creates a CachedValue factory
class CachedValueF(SFact):
    def __init__(self, i):
        SFact.__init__(self)
        self.i = i
    def start(self):
        return CachedValue(maybeLift(self.i))

#Creates a State Machine Factory
class StateMachineF(SFact):
    def __init__(self, s0, i, f):
        SFact.__init__(self)
        self.state = s0
        self.i = i
        self.f = f
    def start(self):
        return StateMachine(self.state, self.i.start(), self.f)

#Creates a Observer Factory
class ObserverF(SFact):
    def __init__(self, f):
        SFact.__init__(self)
        self.f = f
    def start(self):
        return Observer(self.f)

#Creates a Lift0 Factory which turns a constant into a running signal
"""
class Lift0F(SFact):
	def __init__(self,name,f, args):	
		SFact.__init__(self)
		self.f=f 
		self.name=name
		self.args = args
	def start(self):
		return Lift0(name,f,map(lambda x: x.start(), args))
"""		
	
		
		
