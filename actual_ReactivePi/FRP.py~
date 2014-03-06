import g
# Done?

# This is the basic implementation of signals and FRP
import g
from Signal import *
from Time import *

# Some things we still need:
#   Clocks
#   Event filtering
#   Switching
#   Dynamic collections
#   Type-specific initialization of integral

# Todos:

# Local time as a method on an object
# Time since last switch
# Extra signals in an object
# Switching on an event within an object:

# This prevents reinitialization (a "runningin" sort of thing.  Probably the same thing
# we need to keep object references up to date.

def keep(s):
    return Keep(s)

class Keep(CachedSignal):
    def __init__(self, s):
        CachedSignal.__init__(self)
        self.s = maybeLift(s)
        self.active = None
    def refresh(self):
        return self.s.now()
    def typecheck(self, etype):
        st = self.s.typecheck(etype)
        return st
    # This resets the integrator when reinitialized.
    def siginit(self, context):
        if self.active is not None:
            self.active = self.s.siginit(context)
        return self.active

def maybeAddModelToResult(res, m1, m2):
    for (m3, m4) in res:
        if m4 is m1 and m3 is m2:
            return res
    return [(m1, m2)] + res

class Hit(Event):
    def __init__(self, m1, m2, trace):
        Event.__init__(self)
 #       print "Hit object created: " + repr(m1) + " " + repr(m2)
        self.m1 = m1
        self.m2 = m2
        self.trace = trace
        if trace:
            print repr(m1)
            print repr(m2)

    def refresh(self):
        res = []
        l1 = self.m1.allModels()
        l2 = self.m2.allModels()
        if self.trace:
                print repr(l1)
                print repr(l2)
        for m1 in l1:
            if m1.d.initialized:
                for m2 in l2:
                    if not (m1 is m2) and m2.d.initialized and not m1.d.zombie and not m2.d.zombie:
                        if m1.touches(m2, self.trace):
                            res = maybeAddModelToResult(res, m1, m2)
        if res == []:
            return None
        else:
            return res
    def typecheck(self, etype):
        return anyType  # Really a pair of models
    # This resets the integrator when reinitialized.
    def siginit(self, context):
        return self
    
def hit(m1, m2, trace = False):   # Should check types of m1 and m2 to see if they are models or collections.
    return Hit(m1, m2, trace)

class Happen(Event):
    def __init__(self, s):
        Event.__init__(self)
        self.s = maybeLift(s)
        self.context = None

    def refresh(self):
        sval = self.s.now()
        if sval:
            return True
        else:
            return None
    def typecheck(self, etype):
        self.s.typecheck(boolType)
        return EventBoolType
    def siginit(self, context):
        if needInit(self, context):
            newsig = self.s.siginit(context)
            newHap = Happen(newsig)
            self.active = newHap
        return self.active
    
def happen(boolsig, val = True):
    return tag(val, Happen(boolsig))
    
def integral(s, min = None, max = None):
    res = Integrator(min, max)
    res.s = maybeLift(s)
    return res

class Integrator(CachedSignal):
    def __init__(self, min = None, max = None):
        CachedSignal.__init__(self)
        self.lastTime = None
        self.context = None
        self.imax = max
        self.imin = min
 #        print "Created an integrator"
    def refresh(self):
        g.thunks.append(self)
        return self.val
    def force(self):
        v = self.s.now()
 #       print "Integrating", v
        t = g.currentTime
        if self.lastTime is not None:
            deltaT = t - self.lastTime
            self.val = self.val + v * deltaT
            if self.imin is not None:
                self.val = max(self.val, self.imin)
            if self.imax is not None:
                self.val = min(self.val, self.imax)
        self.lastTime = t
    def typecheck(self, etype):
#        print "Type checking integrator"
        st = self.s.typecheck(addableType)
#        print "Integrator argument type: " + st.tname + " Zero: " + str(st.zero)
        if not(addableType.implies(st)):
            argTypeError("integral",st, addableType, 1)
        self.zero = st.zero
        return st
    # This resets the integrator when reinitialized.
    def siginit(self, context):
        if needInit(self, context):
#            print "Initializing an integrator"
            newsig = self.s.siginit(context)
            newint = Integrator()
            newint.s = newsig
            newint.val = self.zero
            newint.imax = self.imax
            newint.imin = self.imin
            self.active = newint
        return self.active



def deriv(s, init = None):
    return DerivSignal(s, init)

class DerivSignal(CachedSignal):
    def __init__(self, s, init):
        CachedSignal.__init__(self)
        self.s = maybeLift(s)
        self.init = init
        self.lastTime = None
        self.context = None
    def refresh(self):
        v = self.s.now()
        t = g.currentTime
        if self.lastTime is None:
            self.lastTime = t
            self.lastVal = v
            return self.init
        deltaT = t - self.lastTime
        deltaV = v - self.lastVal
        self.lastTime = t
        self.lastVal = v
        return deltaV * (1/deltaT)
    def typecheck(self, etype):
        sigType = self.s.typecheck(addableType)
        if not addableType.implies(sigType):
            argTypeError("deriv", sigType, addableType, 2)
        if self.init is None:
            self.init = sigType.zero
        return sigType
    def siginit(self, context):
        if needInit(self, context):
            self.active = DerivSignal(self.s.siginit(context), self.init)
            self.context = context
        return self.active

def tracker(f, s0, s, resType):
    res = StateMachine(s0, f, resType)
    res.s = maybeLift(s)
    return res
# This should replace deriv someday
# f :: State -> SignalValue -> (State, SignalValue)
class StateMachine(CachedSignal):
    def __init__(self, initState, f, resType):
        CachedSignal.__init__(self)
        self.init = initState
        self.f = f
        self.resType = resType
        self.context = None
    def refresh(self):
        v = self.s.now()
        (newState, output) = self.f(self.state, v)
        self.state = newState
        return output
    def typecheck(self, etype):
        self.s.typecheck(anyType)
        return self.resType
    def siginit(self, context):
        if needInit(self, context):
            self.active = StateMachine(self.init, self.f, self.resType)    # Shouldn't need type stuff
            self.active.s = self.s.siginit(context)
            self.active.state = self.init
            self.context = context
        return self.active

def delay(iv, v, ty = P3Type):
    return tracker(lambda st, v:  (v, st), iv, v, ty)
# Maybe reverse these arguments ...

def tag(v, s):
    return TagSignal(lambda i,v1: v, s)

def tags(v, s):
    return TagSignal(lambda i, v1: v[i % len(v)], s)

def mapE(fn, s):
    return TagSignal(lambda i, v1: fn(v1), s)
#  Replace the value of each happening by a constant value

class TagSignal(Event):
    def __init__(self, fn, s):
        Event.__init__(self)
        self.s = maybeLift(s)
        self.fn = fn
        self.i = 0
        self.context = None
    def refresh(self):
        eventVal = self.s.now()
        if eventVal is None:
            return None
        res = self.fn(self.i, eventVal)
        self.i = self.i + 1
        return res
    def typecheck(self, etype):
        return EventAnyType
    def siginit(self, context):
        if needInit(self, context):
            self.active = TagSignal(self.fn, self.s.siginit(context))
            self.context = context
        return self.active

def hold(i, s):
    return HoldSignal(i, s)

class HoldSignal(CachedSignal):
    def __init__(self, i, s):
        CachedSignal.__init__(self)
        self.s = maybeLift(s)
        self.i = i
        self.context = None
    def refresh(self):
        v = self.s.now()
        if v != None:
#            print "Storing " + str(v) + " in hold at " + str(g.currentTime)
            self.i = v
        return self.i
    def typecheck(self, etype):
        initType = getPType(self.i)
        etype = self.s.typecheck(anyType)
        # Check the event type someday but not now ...
        return initType
    def siginit(self, context):
        if needInit(self, context):
            self.active = HoldSignal(self.i, self.s.siginit(context))
            self.context = context
        return self.active

def accum(v0, s):
    return AccumSignal(v0, s)

class AccumSignal(CachedSignal):
    def __init__(self, v0, s):
        CachedSignal.__init__(self)
        self.s = maybeLift(s)
        self.v0 = v0
        self.context = None
    def refresh(self):
        v = self.s.now()
        if v is None:
            return self.v0
        self.v0 = v(self.v0)
        return self.v0
    def typecheck(self, etype):
        initType = getPType(self.v0)
        # Check the event type someday but not now ...
        # Add a wrapper to check fn types maybe
        return initType
    def siginit(self, context):
        if needInit(self, context):
            self.active = AccumSignal(self.v0, self.s.siginit(context))
            self.context = context
        return self.active


mergeE = liftE(mergeE1, 2, "MergeE")

class Clock(CachedSignal):
    def __init__(self, start, step, end, useLocal):
        CachedSignal.__init__(self)
        self.start = start
        self.step = step
        self.end = end
        self.useLocal = useLocal
        self.context = None
        self.n = 0
    def refresh(self):
        if self.done:
            return None
        t = g.currentTime
        if self.useLocal:
            t = t - self.initialTime
        if t < self.nextEvent:
            return None
        res = self.n
        self.n = self.n = 1
        if self.step is None:
            self.done = True
        else:
            if self.end is not None and t > self.end:
                self.done = True
            self.nextEvent = self.nextEvent + self.step
        return res
    
    def typecheck(self, etype):
        return EventNumType
    def siginit(self, context):
        if needInit(self, context):
            self.active = Clock(self.start, self.step, self.end, self.useLocal)
            self.active.done = False
            self.context = context
            self.active.initialTime = context
            self.active.nextEvent = self.start
        return self.active

def now(x):
    return x.now()

def timeIs(t, val = True):
    return tag(val, Clock(t,None,t,False))

def alarm(start = 0, end = None, step = None):
    return Clock(start, step, end, True)

def localTimeIs(t, val = True):
    return tag(val, Clock(t,None,t, True))

def localAlarm(start = 0, end = None, step = None):
    return Clock(start, step, end, True)

# This is to handle "reactive" variables

class RVar(CachedSignal):
    def __init__(self, initValue, type):
        CachedSignal.__init__(self)
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
        self.value = self.value * val;


def var(init):
    return RVar(init, getPType(init))

def typedVar(init, ty):
    return RVar(init, ty)

class RArr(CachedSignal):#I have no idea if this should work...
    def __init__(self, initValue, type):
        CachedSignal.__init__(self)
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
        for i in self.value:
            i = i + val;
    def sub(self, val):
        for i in self.value:
            i = i - val;
    def times(self, val):
        for i in self.value:
            i = i * val;
def arr(init):
    return RArr(init, getPType(init))
def typedArr(init, ty):
    return RArr(init, ty)

