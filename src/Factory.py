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
        return Lift0(x)
    if t is type(1.0):
        return Lift0(x)
    return x
    
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
		x=maybeLift(x)
		return LiftF("add",lambda x,y:x+y, [self,y])
	def __sub__(self,y):
		y=maybeLift(y)
		return LiftF("subtract",lambda x,y:x-y, [self,y])
	def __rsub__(self,y):
		x=maybeLift(x)
		return LiftF("subtract",lambda x,y:y-x, [self,y])
	def __mul__(self,y):
		y=maybeLift(y)
		return LiftF("multiply",lambda x,y:x*y, [self,y])
	def __rmul__(self,y):
		x=maybeLift(x)
		return LiftF("multiply",lambda x,y:x*y, [self,y])
#Creates a Lift Factory	
class LiftF(SFact):
	def __init__(self,name,f, args):	
		SFact.__init__(self)
		self.f=f 
		self.name=name
		self.args = args
	def start(self):
		ea = map(lambda x: maybeLift(x).start(), self.args)
		return Lift(self.name,self.f, ea)

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
class Lift0F(SFact):
	def __init__(self,name,f, args):	
		SFact.__init__(self)
		self.f=f 
		self.name=name
		self.args = args
	def start(self):
		return Lift0(name,f,map(lambda x: x.start(), args))
		
	
		
		
