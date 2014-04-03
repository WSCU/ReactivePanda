import Globals
class Signal:
	def __init__(self):
		self.type = "Signal"
		
class Lift0(Signal):
    def __init__(self, v):
        self.v = v
    def now(self):
        return self.v
        

		
class Lift(Signal):
    def __init__(self,name, f, args):
    	Signal.__init__(self)
        self.f = f
        self.name = name
        self.args=args
    def now(self):
    	ea = map (lambda a: a.now() , self.args)
    	return self.f(*ea)

# Cached Signal that inherits Signal
# Baisically is just a time stamp
class CachedSignal(Signal):
    def __init__(self, f):
        Signal.__init__(self)
        self.f = f
        self.cachedValue = 0
        self.time = -1
    def now(self):
        if self.time is not g.currentTime:
            self.cachedValue = f() 
        return self.cachedValue


# A State Machine signal
class StateMachine(CachedSignal):
    def __init__(self, s0, i, f):
        CachedSignal.__init__(self, f)
        self.i = i
        self.state = s0
    def __rmul__(self, y):
        y = maybeLift(y)
        return LiftF("mul", lambda x,y: y*x, [self.state, y])

class Observer(CachedSignal):
    def __init__(self, f):
        Signal.__init__(self, f)
