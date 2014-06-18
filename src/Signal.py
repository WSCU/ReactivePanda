import Globals
from Types import signalType

class Signal:
	def __init__(self):
		self._type = signalType

class Lift0(Signal):
    def __init__(self, v):
        Signal.__init__(self)
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
        if self.time is not Globals.currentTime:
            self.cachedValue = self.now1()
        return self.cachedValue


# A State Machine signal
class StateMachine(CachedSignal):
    def __init__(self, s0, i, f):
        CachedSignal.__init__(self, f)
        self.i = i
        self.state = s0
        self.time = -1
    def now(self):
        if self.time is not Globals.currentTime:
            self.state = self.f(self)
            self.time = Globals.currentTime
        return self.state
    def __rmul__(self, y):
        y = maybeLift(y)
        return LiftF("mul", lambda x,y: y*x, [self.state, y])

class Observer(CachedSignal):
    def __init__(self, f):
        CachedSignal.__init__(self, f)
    def now1(self):
        return self.f()

class RVar(CachedSignal): #Defines reactive variables like on-screen text
    def __init__(self, initValue, type = signalType):
        CachedSignal.__init__(self, type)
        self.value = initValue
        self.type = type
    def refresh(self):
        return self.value
    def typecheck(self, etype):
        return self.type
    def siginit(self, context):
        return self   #  This should never happen!
    def get(self):    #  Used inside reaction code
        return self.value
    def set(self, val):
        self.value = val
    def add(self, val):
        self.value = self.value + val;
    def sub(self, val):
        self.value = self.value - val;
    def times(self, val):
        self.value = self.value * val
    def now(self):
        return self.value


def var(init): #Actual variable signal
    return RVar(init, type(init))
