# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Signal Factory Class
# Base Signal Factory class
# extends to StateMachineF, LiftF, and Lift0F
class SFact:
	def __init__(self):
		self.type = "factory"
	def __add__(self,x,y):
		y=maybeLift(y)
		return LiftF("add",lambda x,y:x+y, [x,y])
	def __radd__(self,x,y):
		x=maybeLift(x)
		return LiftF("add",lambda x,y:x+y, [x,y])
	def __sub__(self,x,y):
		y=maybeLift(y)
		return LiftF("subtract",lambda x,y:x-y, [x,y])
	def __rsub__(self,x,y):
		x=maybeLift(x)
		return LiftF("subtract",lambda x,y:x-y, [x,y])
	def __mul__(self,x,y):
		y=maybeLift(y)
		return LiftF("multiply",lambda x,y:x*y, [x,y])
	def __rmul__(self,x,y):
		x=maybeLift(x)
		return LiftF("multiply",lambda x,y:x*y, [x,y])
#Creates a Lift Factory	
class LiftF(SFact):
	def __init__(self,name,f, args):	
		SFact.__init__(self)
		self.f=f 
		self.name=name
		self.args = args
	def start(self):
		return Lift(name,f,map(lambda x: x.start(), args))
#Creates a State Machine Factory
class StateMachineF:
    def __init__ (self, initState, f, s, initV):
        self.state = initState
        self.f = f
        self.s = s
        self.initV = initV
    def start(self):
        return StateMachine(self.state, self.f, self.s.start(), self.initV)

#Creates a Lift0 Factory which turns a constant into a running signal	
class Lift0F(SFact):
	def __init__(self,name,f, args):	
		SFact.__init__(self)
		self.f=f 
		self.name=name
		self.args = args
	def start(self):
		return Lift0(name,f,map(lambda x: x.start(), args))