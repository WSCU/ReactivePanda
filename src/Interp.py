from Signal import *
from StaticNumerics import *
from Types import *
import math

"""
Bug: repeating a "to" doesn't work since it assumes that the value is
always the same at the start of the to.

at p c = \p0 t -> c p t
to p i c = \p0 t -> if t < i then t/i * p0 + (1-t/i) * p else c p (t-i)
hold = \p0 t -> p0
Need something to tag interpolants so that we can interpolate
more than one thing at a time - this is probably needed elsewhere
"""

infiniteDur = 1000000

class Interp:
    """
    Base Interpolation Class
    """
    def __init__(self):
        self.interpolant = None
    def __add__(self, x):
        return InterpNext(self, x)

class InterpNext(Interp):
    """
    Adds two Interp together to construct a path tree 
    """
    def __init__(self, i1, i2):
        """
        constructor
        """
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
        """
        returns running interpolant
        """
        return RInterpNext(prev, self.i1, self.i2)

class InterpAt(Interp):
    """
    Start point for a Interp path
    """
    def __init__(self, p):
        """
        Constructor
        """
        Interp.__init__(self)
        self.p = p
        ty = getPType(p)
        checkInterpableType(ty)
        self.type = interpType(ty)
        
    def getInterpolant(self, prev):
        """
        gets the running interpolant
        """
        return RInterpAt(prev, self.p)

class InterpTo(Interp):
    """
    Describes a point along the interpolation path and a duration to that point.
    """
    def __init__(self, dur, p):
        """
        Constructor
        """
        Interp.__init__(self)
        self.dur = float(dur)
        self.p = p
        ty = getPType(p)
        checkInterpableType(ty)
        self.type = interpType(ty)
        
    def getInterpolant(self, prev):
        """
        returns the running interpolant
        """
        return RInterpTo(prev, self.dur, self.p, False)

class InterpMove(Interp):
    """
    Decribes an Interp with an absolute path
    """
    def __init__(self, dur, p):
        """
        constructor
        """
        Interp.__init__(self)
        self.dur = float(dur)
        self.p = p
        ty = getPType(p)
        checkInterpableType(ty)
        self.type = interpType(ty)

    def getInterpolant(self, prev):
        """
        returns running interpolant
        """
        return RInterpTo(prev, self.dur, self.p, True)

class InterpCycle(Interp):
    """
    don't know yet
    """
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
    """
    An Interp that goes backwards along path
    """
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
    """
    returns the interpolant of i
    """
    if i.interpolant is None:
        i.interpolant = i.getInterpolant(None)
        i.interpolant.type = i.type
    return i.interpolant

#  Classes for running interpolants:


class RInterpNext:
    """
    Running version of the InterpNext. this actually follows the path
    """
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
        """
        Return the current interp point recursively of whichever path we are currently on
        """
        if t < self.i1.dur:
            return self.i1.interp(t)
        else:
            return self.i2.interp(t - self.i1.dur)

class RInterpAt:
    """
    Running version of InterpAt
    """
    def __init__(self, prev, p):
        self.p = p
        self.first = p
        self.last = p
        self.dur = 0
        self.delta = None

    def interp(self, t):
        """
        returns the point of the interpolant
	"""
        return self.p

class RInterpTo:
    """
    Running  version of InterpTo
    """
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
        """
        Retutns the path location between two Interp s based on time
        """
        return lerpStatic(t/self.dur, self.first, self.last)

class RInterpCycle:
    """
    The running version of we don't know
    """
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
        """ 
        has something to do with delta
        """
        f = math.floor(t/self.i.dur)
        t1 = t - f*self.i.dur
        r = self.i.interp(t1)
        if self.delta != None:
            r = r + self.i.delta * f
        return r

class RInterpRev:
    """
    Running version of a reverse path Interp
    """
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
        """
        Returns current path location along reverse Interp recursive
        """
        return self.i.interp(self.i.dur - t)


def toS(d, p):
    """
    Front End version of a InterpTo object
    """
    return InterpTo(d, p)

# Reverse an interpolation
def reverseS(i):
    """
    Front End version of a InterpRev object    
    """
    return InterpRev(i)

def moveS(d, p):
    """
    Front End version of a InterpMove object
    """
    return InterpMove(d, p)

def atS(p):
    """
    Front End version of a InterpAt object
    """
    return InterpAt(p)

def repeatS(n, i):
    """
    Front End version of a InterpCycle object
    (not sure what this does)
    """
    return InterpCycle(n, i)

def lerpStatic(t, v1, v2):
    """
    Return the actual location along the current path (used as base case in RInterpTo)
    """
    ty1 = getPType(v1)
    if ty1 is numType:   # Could resolve this in Signal.py
        return (1-t) * v1 + t * v2
    return v1.interp(t, v2)

# two interpolants:
#  lerp(t, v1, v2) - linear interpolation
#  interpolate(t, i) - use interpolation class



def interpolateStatic(t, i):
    """
    Returns the current point along the Interp i
    """
    i1 = getInterpolant(i)
    if t < 0:
        return i1.first
    if t >= i1.dur:
        return i1.last
    result = i1.interp(t)
    #print result
    return result


