from Signal import *
from StaticNumerics import *
from Types import *
import math

# Bug: repeating a "to" doesn't work since it assumes that the value is
# always the same at the start of the to.

# at p c = \p0 t -> c p t
# to p i c = \p0 t -> if t < i then t/i * p0 + (1-t/i) * p else c p (t-i)
# hold = \p0 t -> p0
# Need something to tag interpolants so that we can interpolate
# more than one thing at a time - this is probably needed elsewhere

infiniteDur = 1000000

class Interp:
    def __init__(self):
        self.interpolant = None
    def __add__(self, x):
        return InterpNext(self, x)


class InterpNext(Interp):
    def __init__(self, i1, i2):
        Interp.__init__(self)
        self.i1 = i1
        self.i2 = i2
        ty1 = getPType(i1)
        ty2 = getPType(i2)
        checkInterpableType(ty1)
        checkInterpableType(ty2)
        checkSameInterp(ty1, ty2)
        self.type = ty1
    def getInterpolant(self, prev):
        return RInterpNext(prev, self.i1, self.i2)

class InterpAt(Interp):
    def __init__(self, p):
        Interp.__init__(self)
        self.p = p
        ty = getPType(p)
        checkInterpableType(ty)
        self.type = interpType(ty)
        
    def getInterpolant(self, prev):
        return RInterpAt(prev, self.p)

class InterpTo(Interp):
    def __init__(self, dur, p):
        Interp.__init__(self)
        self.dur = float(dur)
        self.p = p
        ty = getPType(p)
        checkInterpableType(ty)
        self.type = interpType(ty)
        
    def getInterpolant(self, prev):
        return RInterpTo(prev, self.dur, self.p, False)

class InterpMove(Interp):
    def __init__(self, dur, p):
        Interp.__init__(self)
        self.dur = float(dur)
        self.p = p
        ty = getPType(p)
        checkInterpableType(ty)
        self.type = interpType(ty)

    def getInterpolant(self, prev):
        return RInterpTo(prev, self.dur, self.p, True)

class InterpCycle(Interp):
    def __init__(self, n, i):
        Interp.__init__(self)
        self.n = n
        self.i = i
        ty = getPType(i)
        checkInterpType(ty)
        self.type = ty
    def getInterpolant(self, prev):
        return RInterpCycle(prev, self.n, self.i)

class InterpRev(Interp):
    def __init__(self, i):
        Interp.__init__(self)
        self.i = i
        ty = getPType(i)
        checkInterpType(ty)
        self.type = ty
    def getInterpolant(self, prev):
        return RInterpRev(prev, self.i)

# Interpolant caching:

def getInterpolant(i):
    if i.interpolant is None:
        i.interpolant = i.getInterpolant(None)
        i.interpolant.type = i.type
    return i.interpolant

#  Classes for running interpolants:


class RInterpNext:
    def __init__(self, prev, i1, i2):
        self.i1 = i1.getInterpolant(prev)
        self.i2 = i2.getInterpolant(self.i1)
        self.first = self.i1.first
        self.last = self.i2.last
        if self.i1.delta == None or self.i2.delta == None:
            self.delta = None
        else:
            self.delta = self.i1.delta + self.i2.delta
        self.dur = self.i1.dur + self.i2.dur

    def interp(self, t):
        if t < self.i1.dur:
            return self.i1.interp(t)
        else:
            return self.i2.interp(t - self.i1.dur)

class RInterpAt:
    def __init__(self, prev, p):
        self.p = p
        self.first = p
        self.last = p
        self.dur = 0
        self.delta = None

    def interp(self, t):
        return self.p

class RInterpTo:
    def __init__(self, prev, dur, p, relative):
        if (prev is None):
            interpMissingAt()
        if relative:
            self.delta = p
            p = p + prev.last
        else:
            self.delta = None
        self.last = p
        self.dur = dur
        self.first = prev.last

    def interp(self, t):
        return lerpStatic(t/self.dur, self.first, self.last)

class RInterpCycle:
    def __init__(self, prev, n, i):
        self.i = i.getInterpolant(prev)
        if n == -1:
            self.dur = infiniteDur
        else:
            self.dur = n * self.i.dur
        self.first = self.i.first
        if self.i.delta == None:
            self.delta = None
            self.last = self.i.last
        else:
            self.delta = self.i.delta * n
            self.last = self.i.first + self.delta

    def interp(self, t):
        f = math.floor(t/self.i.dur)
        t1 = t - f*self.i.dur
        r = self.i.interp(t1)
        if self.delta != None:
            r = r + self.i.delta * f
        return r

class RInterpRev:
    def __init__(self, prev, i):
        self.i = i.getInterpolant(prev)
        if self.i.delta is not None:
            print "Cannot reverse an interpolant of moves"
            exit()
        self.first = self.i.last
        self.last = self.i.first
        self.dur = self.i.dur
        self.delta = None

    def interp(self, t):
        return self.i.interp(self.i.dur - t)



def toS(d, p):
    return InterpTo(d, p)

# Reverse an interpolation
def reverseS(i):
    return InterpRev(i)

def moveS(d, p):
    return InterpMove(d, p)

def atS(p):
    return InterpAt(p)

def repeatS(n, i):
    return InterpCycle(n, i)

def interpArr(a):
    return InterpArr(a)

def lerpStatic(t, v1, v2):
    ty1 = getPType(v1)
    if ty1 is numType:   # Could resolve this in Signal.py
        return (1-t) * v1 + t * v2
    return v1.interp(t, v2)

# two interpolants:
#  lerp(t, v1, v2) - linear interpolation
#  interpolate(t, i) - use interpolation class

class InterpArr(Interp):
    def __init__(self, arr):
        Interp.__init__(self)
        self.arr = arr
        v, d = arr[0]
        self.type = getPType(v)

    def getInterpolant(self, prev):
        return RInterpArr(prev, self.arr)

class RInterpArr:
    def __init__(self, prev, arr):
        self.arr = arr
        f, t = arr[0]
        l, t1 = arr[len(arr)-1]
        totalTime = 0
        for v, t in arr:
            totalTime = totalTime + t
        self.first = f
        self.last = l
        self.dur = totalTime
        self.delta = None
    def interp(self, t):
        l = None
        for v, t1 in self.arr:
            if t <= t1:
                return v
            t = t - t1
            l = v
        return l # Shouldn't happen

def interpArr(a):
    return InterpArr(a)


def interpolateStatic(t, i):
    i1 = getInterpolant(i)
    if t < 0:
        return i1.first
    if t >= i1.dur:
        return i1.last
    result = i1.interp(t)
    #print result
    return result


