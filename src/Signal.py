import Globals

class Lift0:
    def __init__(self, v):
        self.v = v
    def start(self):
        return self
    def now(self):
        return self.v
     
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
    
def lift(name,f):
	def fn(*args):
		return LiftF(name,f,args)
	return fn

# A State Machine signal
class StateMachine(Signal):
    def __init__(self, s0, i, f):
        Signal.__init__(self)
        self.state = s0
        self.i = i
        self.f = f
    def now(self):
        Globals.thunks.append(lambda: self.f(self)) # adds a deferred computation for the function f
        return self.state

# A state machine like observer signal
class Observer(Signal):
    def __init__(self, f):
        Signal.__init__(self)
        self.f = f
    def now(self):
        return self.f()


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
