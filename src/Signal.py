import Globals

class Lift0:
    def __init__(self, v):
        self.now = v
    def start(self):
        return self
    def refresh(self, dt):
        pass
     
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
        self.current = initV
    def now(self):
        #n = self.s.now() #n is current value 
        s, output = self.f(self.s.current, self.state) 
        self.state = s
        self.current = output
        
class Clock(Signal):
    def __init__(self):
        Signal.__init__(self)
    def now(self):
        Globals.currentTime = Globals.currentTime + Globals.dt
        return Globals.currentTime
        
        
    
    """def typecheck(self, etype):
        return EventNumType"""
    def siginit(self, context):
        if needInit(self, context):
            self.active = Clock(self.start, self.step, self.end, self.useLocal)
            self.active.done = False
            self.context = context
            self.active.initialTime = context
            self.active.nextEvent = self.start
        return self.active
