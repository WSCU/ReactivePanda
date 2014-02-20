#class Lift0:
  #  def __init__(self, v):
   #     self.now = v
    #def start(self):
     #   return self
    #def refresh(self, dt):
     #   pass
     
class Signal:
	def __init__(self):
		self.type = "Signal"
class Lift(Signal):
    def __init__(self,name, f, args):
    	Signal.__init__(self)
        self.f = f
        self.name = name
        self.args=args
    def now(self):
    	ea = map (lambda a: a.now() , self.args)
    	return self.f(*ea)
    
def lift(f):
	def fn(*args):
		return LiftF(" ",f,args)
	return fn
    
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