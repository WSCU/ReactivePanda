
# Lots of undocumented code here!!!

# This lifts operations up to the signal world

from Color import *
from Errors import *
from StaticNumerics import *
from Time import *
from Types import *
from Interp import *
import g

# These are defined outside of the Signal class and can be used from the
# lifted numerics.  Note that the inheritance of Python is a problem here -
# if you add a P3 and a Signal, you may get into either of these classes
# depending on the 1st argument type.  So the radd trick doesn't buy you
# anything in this case.  By placing these here classes like P3 can handle
# an add in which the 2nd arg is a Signal.

# I can't remember why div isn't also here.  Bug?  Me being lazy?

def sigadd(s, y):
    f1 = lift(lambda x, y:x + y, "+", infer="add")
    return f1(s, y)

def sigsub(s, y):
    f1 = lift(lambda x, y:x-y, "-", infer="sub")
    return f1(s, y)


def sigmul(s, y):
    f1 = lift(lambda x, y:x * y, "*", infer="times")
    return f1(s, y)

def sigabs(s):
    f1 = lift(lambda x:abs(x), "abs", infer="abs")
    return f1(s)

def myNot(x):
    if x:
        return False
    return True

# This is an object which defines the start time of a signal.  This is used
# in signal caching - if the same signal is started in the same context you can
# share.  However, if the contexts differ you need two different signals.
# Switching creates new contexts.

# This could be just the time but I have an object here in case I want to
# add more information later.  Probably should have an equality method here.

class Context:
    def __init__(self, t):
        self.initialTime = t

# These arithmetic operations all lift arguments

class Signal:
    def __add__(self, y):
        return sigadd(self, y)
    def __radd__(self, y):
        return sigadd(y, self)
    def __sub__(self, y):
        return sigsub(self, y)
    def __rsub__(self, y):
        return sigsub(y, self)
    def __mul__(self, y):
        return sigmul(self, y)
    __rmul__ = __mul__
    def __div__(self, y):
        f1 = lift(lambda x, y:x / y, "/", numType2, numType)
        return f1(self, y)
    def __rdiv__(self, y):
        f1 = lift(lambda x, y:y / x, "/", numType2, numType)
        return f1(self, y)
    def __eq__ (self, y):  #  Need to null check signals
        if y == None:
            return False
        f1 = lift(lambda x, y:x == y, '==', infer="sameb")
        return f1(self, y)
    def __ne__ (self, y):
        if y == None:    # Need to null check signals
            return True
        f1 = lift(lambda x, y:x != y, '!=', infer="sameb")
        return f1(self, y)
    def __gt__ (self, y):
        f1 = lift(lambda x, y:x > y, '>', numType2, boolType)
        return f1(self, y)
    def __ge__ (self, y):
        f1 = lift(lambda x, y:x >= y, '>=', numType2, boolType)
        return f1(self, y)
    def __lt__ (self, y):
        f1 = lift(lambda x, y:x < y, '<', numType2, boolType)
        return f1(self, y)
    def __le__ (self, y):
        f1 = lift(lambda x, y:x <= y, '<=', numType2, boolType)
        return f1(self, y)
    def __abs__ (self):
        return sigabs(self)
    def __neg__(self):
        return sigmul(-1, self)
    def __and__(self, y):  # This is "&", not "and"
        f1 = lift(lambda x, y: x & y, 'and', [boolType, boolType], boolType)
        return f1(self, y)
    def __or__(self, y):  # This is "|", not "or"
        f1 = lift(lambda x, y: x | y, 'or', [boolType, boolType], boolType)
        return f1(self, y)
    def __invert__(self):  # This is "~", not "not"
        f1 = lift(myNot, '~', [boolType], boolType)
        return f1(self)


    # This default can't be used for signals that have
    # sub-signals or need to reinit

    def siginit(self, context):
        return self

    def reduce(self):   # Where is this used?
        return self

# This handles a shared signal - it prevents re-evaluation at a given time.
# Use t (rather than the context) to determine whether the cache is valid.
# Also do blackholing here - detect circular evaluation.

class CachedSignal(Signal):
    def __init__(self):
        self.v = None
        self.t = -1
        self.evaluating = False

    def siginit(self, context):
        return self

    def now(self):
        if(self.evaluating):
            raise NameError, 'Evaluation Loop'   #  Poor error message!
        if(self.t == g.currentTime):  # Cache hit
            return self.v
        self.evaluating = True    # Cache miss
        self.v = self.refresh()
        self.t = g.currentTime
        self.evaluating = False
        return self.v

# Lift a constant - this can be freely reinitialized since it doesn't change
# over time

class Lift0(Signal):  # Uses the default init
    def __init__(self, v):
        self.v = v
        self.ptype = getPType(v)

    def typecheck(self, expected):
        return self.ptype

    def now(self):
        return self.v

    def signit(self, context):
#        print "Initializing " + str(v)
        return self

# The event type has a lifted "+" that does an asymetric merge.

class Event(CachedSignal):
    def __init__(self):
        CachedSignal.__init__(self)

    def __add__(self, x):
        f1 = liftE(mergeE1, 2, "Event +")
        return f1(self, x)

def mergeE1(e1, e2):
    ## Make this symmetric by creating lists.
    #   if e1 != None or e2 != None:
    #       print "Merge: ", e1, e2
        if e1 == None:
            return e2
        return e1

# This is tricky - a few things:
#   When we initialize a behavior we need to replicate the ref
#   so that circular stuff works OK
#   Type checking sees this as a leaf

class SignalRefData:
    pass

# This is for (potentially) circular signal graphs.  If a signal is local to a
# handle, this is used to create a signal for undefined refs.  So if you refer to
# handle.foo, the handle object notes that there is no foo in the table and creates
# a signal ref for it.  Unfortunately, we can't tell what type of value the signal
# will hold.  Probably best to punt for now (ty = ANY).  I can't remember what the
# slot thing is!

# You fill in a ref by assigning to signal field.  I would think that you need
# to check that the signal isn't already initialized in setBehavior.

# This is here to place an identity in each ref

class SignalRef(Signal):
    def __init__(self, slot, parent, ty, handle, control):
        self.__dict__['signal'] = None
        d = SignalRefData()
        self.d = d
        d.sigtype = ty
        d.slot = slot
        d.active = None
        d.parent = parent
        d.context = None
        d.handle = handle
        d.default = None
        d.control = control
        d.refnum = g.nextSignalRef  # used for identity
        g.nextSignalRef = g.nextSignalRef + 1
    def setBehavior(self, b):  # Implicit lifting
        if isinstance(b, Signal):
            self.__dict__['signal'] = b
        else:
            self.__dict__['signal'] = Lift0(b)
    def __setattr__(self, name, val):
        if name == 'd':
            self.__dict__['d'] = val
        elif name == 'signal':
            self.setBehavior(val)
        else:
            unKnownMethod(self.name, name)
    # These are for use as a model.  I'm not sure why refresh descends to
    # the signal level!

    def refresh(self):
        pass
    def sname(self):
        return self.d.handle.name + "." + self.d.slot
    def typecheck(self, expected):
#       print "Type of " + self.sname() + " is " + self.d.sigtype.tname
        return self.d.sigtype;
    
    def typecheckandinit(self, ctxt):
#        print "Type checking " + self.sname()
#        print self.signal
#        print "Required type: " + self.d.sigtype.tname
        sigType = self.signal.typecheck(self.d.sigtype)
    #        print "Inferred type " + sigType.tname
        if not self.d.sigtype.implies(sigType):
            signalTypeError(self.d.slot, self.d.handle.name, self.d.sigtype, sigType)
        self.d.active = self.signal.siginit(ctxt)
    def siginit(self, context):
        return self
# Two cases here:
    #   a) no enclosing handle - just refer to the active signal
    #   b) this is a component of a named object.  Go to the object
    #      and find the signalref in the appropriate slot.  This
    #      allows for switching since the signalref may change during
    #      the program execution
    #   Note that we need to have chains of pointers to make this work.  If you say
    #   obj1.x = obj2.y, then obj1 has a signal reference whose value is the signal
    #    reference in obj2.
    def now(self):
#            print "Eval of " + self.sname()
# Basic idea: the "Control" field overrides signals
# in the model.
        if self.d.control is not None:
            c = self.d.control.now()
            if (c is not None):
                if (c.dict.has_key(self.d.slot)):
                    # Do we need to sustain the active signal?
                    return c.dict[self.d.slot]
        return self.d.active.now()

# Not sure why the siginit happens
    def checkSignals(self, context):
        if self.signal is None:
            undefinedSignal(self, 'signal')
        self.siginit(context)
    # Apply a defaulting strategy
    def default(self):
        if undefinedRef(self):
            if self.d.default is None:
                undefinedSignal(self.d.handle, self.d.slot)
            self.setBehavior(maybeLift(self.d.default))
#             print "Typing " + sname(sig)

def undefinedRef(x):
    return x.signal is None

def containsRef(l, r):
    n = r.d.refnum
    for ref in l:
        if ref.d.refnum == n:
            return True
    return False

# This signal is used only for global time.  Most methods are picked up in the superclass.

class GlobalTime(Signal):
    def now(self):
        # print "Getting time at " + str(g.currentTime)
        return g.currentTime
    def typecheck(self, e):
        return numType

class LocalTime(Signal):
    def now(self):
        return g.currentTime - self.startTime
    def siginit(self, context):
        res = LocalTime()
        res.startTime = context
        return res
    def typecheck(self, e):
        return numType

# Should also have a switch time here ...

class SliderValue(Signal):
    def __init__(self, slider):
        self.slider = slider
    def now(self):
        res = self.slider.d.svalue
        return res
    def typecheck(self, r):
        return numType

# An event monitor is an object that returns the current event value
# from the global event list.  The event name is the key into the dicationary
# g.events
class EventMonitor(Event):
    def __init__(self, ename):
        Event.__init__(self)
        self.ename = ename
    # Return None if the event hasn't been posted
    def refresh(self):
        if type(self.ename).__name__=='list':  # allow event monitors to check a list of events
           for e in self.ename:
               if g.events.has_key(e):
                   return g.events[e]
           return None
        if g.events.has_key(self.ename):
            return g.events[self.ename]
        return None
    # These events don't have an associated type (yet)
    def typecheck(self, expected):
        return EventAnyType

# An event monitor is an object that returns the current event value
# from the global event list.  The event name is the key into the dicationary
# g.events
class EventStream(Event):
    def __init__(self, timings, offset):
        Event.__init__(self)
        self.timings = timings
        self.offset = offset
        self.lastTime = -0.000001
    # Return None if the event hasn't been posted
    def refresh(self):
        lastTime = self.lastTime
        self.lastTime = g.currentTime
        for (t, v) in self.timings:
#            print t, v, lastTime, g.currentTime
            if t-self.offset > lastTime and t-self.offset <= g.currentTime:
                return v
        return None
    # These events don't have an associated type (yet)
    def typecheck(self, expected):
        return EventAnyType

def events(timings, offset = 0):
    return EventStream(timings, offset)

def liftE(f, n, s):
    def fn ( * args):
        b = False
        for a in args:
            if isinstance(a, Signal):
                b = True
        if b:
            return GLiftE(f, args)
        else:
            return f( * args)
    return fn

# This needs more methods (siginit, typecheck)
class GLiftE(Event):
    def __init__(self, f, args):

        Event.__init__(self)
        self.f = f
        self.args = map(maybeLift, args)
        self.context = None
    def refresh(self):
        newArgs = map (lambda a: a.now(), self.args)
        return self.f( * newArgs)
    def siginit(self, context):
        if needInit(self, context):
            res = GLiftE(self.f, self.args)
            self.context = context
            res.args = map (lambda a: a.siginit(context), res.args)
            self.active = res
        return self.active
    def typecheck(self, etype):
        return etype

# Generalized lifting.   Note that this returns a function

# Type inference is a serious problem - untyped signals return "anyType"
# for their type - we work around this by assuming that each argument has
# the same type.  If t1 is anyType, then we set it to the type of t2.
# Adding two signals that are both untyped won't work.

# The following code is a poor excuse for Hindley-Milner - please be kind!

def lift(f, fname, argtypes=None, restype=None, infer=None):
    def fn ( * args):
        b = False
        for a in args:
            if isinstance(a, Signal) or hasattr(a, 'reactive'):
                b = True
        if b:
            # print "Reactive argument to " + fname
            res = GLift(f, args, fname, argtypes, restype, infer)
            return res
        else:
            # This is where static overloading gets resolved.
#            print "Static call to " + fname
            if infer == 'add':
                t1 = getPType(args[0])
                t2 = getPType(args[1])
                # print "Static " + str(t1) + " + " + str(t2)
                if t1 == anyType:
                    t1 = t2
                if t2 == anyType:
                    t2 = t1
                if t1 is numType and t2 is numType or t1 == stringType and t2 == stringType:
                    return args[0] + args[1]
                if t1 is P2Type and t2 is P2Type:
                    return addP2(args[0], args[1])
                if t1 is P3Type and t2 is P3Type:
                    return addP3(args[0], args[1])
                if t1 is HPRType and t2 is HPRType:
                    return addHPR(args[0], args[1])
                if t1 is controlType and t2 is controlType:
                    return args[0] + args[1] # ??
                if anInterpType(t1) and anInterpType(t2):
                    return t1 + t2
                mismatchedNumerics("+", t1, t2)
            # Cut and paste!  Should be generalized to use above code
            if infer == 'sub':
                t1 = getPType(args[0])
                t2 = getPType(args[1])
                if t1 == anyType:
                    t1 = t2
                if t2 == anyType:
                    t2 = t1
                if t1 == numType and t2 == numType:
                    return args[0] - args[1]
                if t1 == P2Type and t2 == P2Type:
                    return subP2(args[0], args[1])
                if t1 == P3Type and t2 == P3Type:
                    return subP3(args[0], args[1])
                if t1 is HPRType and t2 is HPRType:
                    return subHPR(args[0], args[1])
                mismatchedNumerics("-", t1, t2)
            if infer == 'times':
                t1 = getPType(args[0])
                t2 = getPType(args[1])
                # Deal with anytype here
                if t1 is numType and t2 is numType:
                    return args[0] * args[1]
                if t1 is numType and t2 is P2Type:
                    return scaleP2(args[0], args[1])
                if t2 is numType and t1 is P2Type:
                    return scaleP2(args[1], args[0])
                if t1 is numType and t2 is P3Type:
                    return scaleP3(args[0], args[1])
                if t2 is numType and t1 is P3Type:
                    return scaleP3(args[1], args[0])
                if t1 is numType and t2 is HPRType:
                    return scaleHPR(args[0], args[1])
                if t2 is numType and t1 is HPRType:
                    return scaleHPR(args[1], args[0])
                mismatchedNumerics("*", t1, t2)
            if infer == 'abs':
                t = getPType(args[0])
                if t is numType:
                    return abs(args[0])
                if t is P2Type:
                    return absP2(args[0])
                if t is P3Type:
                    return absP3(args[0])
                badArgToAbs(t)

            if infer == 'interpolate':
                return interpolantInferStatic(fname, args)
            # print "Calling " + fname
            return f(*args)
    return fn

# Note sure where I use maybeLift ...
def maybeLift(x):
    if isinstance(x, Signal):
        return x
    elif hasattr(x, 'maybeLift'):  # Doesn't seem to be used anywhere
        return x.maybeLift()
    else:
        return Lift0(x)

# Generalized lifting.  This is the nasty part of the system!

class GLift(CachedSignal):
    def __init__(self, fn, args, fname, argtypes, restype, infer):
        CachedSignal.__init__(self)
        self.fn = fn
        self.args = map(maybeLift, args)
        self.fname = fname
        self.argtypes = argtypes
        self.restype = restype
        self.infer = infer
        self.context = None
    def __str__(self):
        return "[Lifted " + self.fname + "]"
    # Note this is strict!
    def refresh(self):
        newArgs = map (lambda a: a.now(), self.args)
        # print "Glift Refresh",self.fname, str(newArgs)
        res = self.fn( * newArgs)
        return res
    # Bug: The following can't handle recursion
    def siginit(self, context):
        # print "Initializing lifted " + self.fname
        if needInit(self, context):
            res = GLift(self.fn, self.args, self.fname, self.argtypes, self.restype, self.infer)
            self.context = context
            self.active = res
            res.args = map (lambda a: a.siginit(context), res.args)
        return self.active
    def typecheck(self, etype):
        # This is truely awful code - read at your own risk!
        # print "typeCheck " , self.fname
        if self.infer is None:
            if (len(self.args) != len(self.argtypes)):
                wrongNumberOfArguments(self.fname)
            for a, t, n in zip(self.args, self.argtypes, range(6)):
                argType = a.typecheck(t)
                if not t.implies(argType):
                    argTypeError(self.fname, argType, t, n)
            return self.restype
        if self.infer == 'add':
            if len(self.args) != 2:
                wrongNumberOfArguments(self.fname)
            arg1 = self.args[0].typecheck(addableType)
            arg2 = self.args[1].typecheck(addableType)
            if arg1 == anyType:
                    arg1 = arg2
            if arg2 == anyType:
                    arg2 = arg1
            if arg1 != arg2:
                argTypeError(self.fname, arg1, arg2, 2)
            if not (addableType.implies(arg1)):
                argTypeError(self.fname, arg1, addableType, 1)
            if arg1 is P2Type:
                self.fn = addP2
            if arg1 is P3Type:
                self.fn = addP3
            if arg1 is HPRType:
                self.fn = addHPR
            if arg1.tname == "Event":
                self.fn = addEvents

            # Need to check for interpolants here?
# This is where the signal / P3 overload would be detected
            return arg1
        if self.infer == 'sub':
            if len(self.args) != 2:
                wrongNumberOfArguments(self.fname)
            arg1 = self.args[0].typecheck(scalableType)
            arg2 = self.args[1].typecheck(scalableType)
            if arg1 != arg2:
                argTypeError(self.fname, arg1, arg2, 2)
            if not (scalableType.implies(arg1)):
                argTypeError(self.fname, arg1, scalableType, 1)
            if arg1 is P2Type:
                self.fn = subP2
            if arg1 is P3Type:
                self.fn = subP3
            if arg1 is HPRType:
                self.fn = subHPR
            return arg1
        if self.infer == 'dot':
            if len(self.args) != 2:
                wrongNumberOfArguments(self.fname)
            arg1 = self.args[0].typecheck(scalableType)
            arg2 = self.args[1].typecheck(scalableType)
            if arg1 != arg2:
                argTypeError(self.fname, arg1, arg2, 2)
            if not (scalableType.implies(arg1)):
                argTypeError(self.fname, arg1, scalableType, 1)
            return arg1
        if self.infer == 'times':
            if len(self.args) != 2:
                wrongNumberOfArguments(self.fname)
            arg1 = self.args[0].typecheck(anyType)
            arg2 = self.args[1].typecheck(anyType)
            if arg1 is numType and scalableType.implies(arg2):
                if arg2 is P2Type:
                    self.fn = scaleP2
                if arg2 is P3Type:
                    self.fn = scaleP3
                if arg2 is HPRType:
                    self.fn = scaleHPR
                return arg2
            if arg2 == numType and scalableType.implies(arg1):
                if arg1 == P2Type:
                    self.fn = lambda x, y: scaleP2(y, x)
                if arg1 == P3Type:
                    self.fn = lambda x, y: scaleP3(y, x)
                return arg1
            if not addableType.implies(arg1):
                argTypeError(self.fname, arg1, addableType, 1)
            else:
                argTypeError(self.fname, arg2, addableType, 2)
        if self.infer == 'same' or self.infer == 'sameb':
            if len(self.args) != 2:
                wrongNumberOfArguments(self.fname)
            arg1 = self.args[0].typecheck(anyType)
            arg2 = self.args[1].typecheck(anyType)
            if arg1 != arg2:
                argTypeError(self.fname, arg1, arg2, 1)
            if self.infer == 'same':
                return arg1
            else:
                return boolType

        if self.infer == 'abs':
            if len(self.args) != 1:
                wrongNumberOfArguments(self.fname)
            arg1 = self.args[0].typecheck(scalableType)
            if arg1 == P2Type:
                self.fn = absP2
            if arg1 == P3Type:
                self.fn = absP3
            return numType
        if self.infer == 'format':
            if len(self.args) == 0:
                wrongNumberOfArgs(self)
            arg1 = self.args[0].typecheck(stringType)
            return stringType
        if self.infer == 'interpolate':
            return interpolantInferSignal(self, self.fname, self.args)
        if self.infer == 'choose':
            if len(self.args) != 3:
                wrongNumberOfArguments(self.fname)
            arg1 = self.args[0].typecheck(boolType)
            arg2 = self.args[1].typecheck(anyType)
            arg3 = self.args[1].typecheck(anyType)
            if arg2 != arg3:
                typesMustMatch('choose', arg2, arg3)
            return arg2
        else:
            print "Unknown type scheme: "
            print self.infer
            return anyType

# The never occuring event

class Never1(Signal):
    def now(self):
        return None
    def type(self):
        return NeverType
    def typecheck(self, etype):
        return NeverType


Never = Never1()

# Note that the attachment to the world model list makes sure that these signals are
# sustained.  I'm not sure we need this at all anymore since we have local signals.

def signal(name, ty):
    r = SignalRef(name, name, ty, None)
    g.models.append(r)
    return r

def needInit(obj, context):
    return obj.context != context

# Type inference for interpolants

def interpolantInferStatic(fname, args):
    if fname == "lerp":
        if len(args) != 3:
            wrongNumberOfArguments(fname)
        t1 = getPType(args[0])
        t2 = getPType(args[1])
        t3 = getPType(args[2])
        if t1 is not numType:
            argTypeError(fname, t1, numType, 1)
        if t2 != t3:
            interpTypeError(t2, t3)
        if not interpableType.implies(t2):
            interpTypeError(t2, t3)
        if t2 is numType:
            return lerpNum(args[0], args[1], args[2])
        return args[1].interp(args[0], args[2])
    if fname == "interpolate":
        if len(args) != 2:
            wrongNumberOfArguments(fname)
        t1 = getPType(args[0])
        t2 = getPType(args[1])
        if t1 is not numType:
            argTypeError(fname, t1, numType, 1)
        if not anInterpType(t2):
            argTypeError(fname, t2, interpType, 2)
        return interpolateStatic(args[0], args[1])
    # Do further arg type checking in the static calls
    if fname == "to":
        return toS(args[0], args[1])
    if fname == "at":
        return atS(args[0])
    if fname == "move":
        return moveS(args[0], args[1])
    if fname == "reverse":
        return reverseS(args[0])
    if fname == "repeat":
        return repeatS(args[0], args[1])
    if fname == "forever":
        return repeatS(-1, args[0])
    print "Unknown interpolation function: " + fname
    exit()


def interpolantInferSignal(fn, fname, args):
    if fname == "lerp":
        if len(args) != 3:
            wrongNumberOfArguments(fname)
        t1 = args[0].typecheck(numType)
        t2 = args[1].typecheck(anyType)
        t3 = args[2].typecheck(t2)
        if t1 is not numType:
            argTypeError(fname, t1, numType, 1)
        if not interpableType(t2):
            interpTypeError(t2)
        if t2 != t3:
            typesMustMatch(fname, t2, t3)
        return t2
    if fname == "interpolate":
        if len(args) != 2:
            wrongNumberOfArguments(fname)
        t1 = args[0].typecheck(numType)
        t2 = args[1].typecheck(anyType)
        #print "interpolate inference ", t1, t2
        if t1 is not numType:
            argTypeError(fname, t1, numType, 1)
        if not anInterpType(t2):
            argTypeError(fname, t2, theInterpType, 2)
        #print "typecheck done"
        return t2.innerTypes[0]
    if fname == "at":
        if len(args) != 1:
            wrongNumberOfArguments(fname)
        ty = args[0].typecheck(anyType)
        if not interpableType(ty):
            argTypeError(fname, ty, theInterpType, 1)
        # print "In Signal inferring " + fname
        return interpType(ty)
    if fname == "to" or fname == "move" or fname == "repeat":
        if len(args) != 2:
            wrongNumberOfArguments(fname)
        t1 = args[0].typecheck(numType)
        t2 = args[1].typecheck(anyType)
        if t1 is not numType:
            argTypeError(fname, t1, numType, 1)
        if not interpableType(t2):
            argTypeError(fname, t2, theInterpType, 2)
        # print "In Signal inferring " + fname
        return interpType(t2)
    if fname == "forever" or fname == "reverse":
        if len(args) != 1:
            wrongNumberOfArguments(fname)
        t = args[0].typecheck(numType)
        if not anInterpType(t):
            argTypeError(fname, t, theInterpType, 1)
        return t
    print "Unknown interpolation function: " + fname
    exit()
# Need a clock and some other event stuff

time = GlobalTime()
localTime = LocalTime()

g.add = sigadd
g.sub = sigsub
g.mul = sigmul
g.abs = sigabs

class Static:
    def __init__(self, v):
        self.v = v
        self.type = StaticType
def static(x):
    return Static(x)
