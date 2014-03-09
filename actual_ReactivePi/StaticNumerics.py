# Done

# This is the non-reactive version of the numeric classes.  To get the overloading right,
# we have to go through contortions using radd, rsub, and rmul so that an ordinary
# number doesn't screw up overloading in 1 + signal, 1 - signal, and 1 * signal.
# Not sure why rdiv isn't here.

import g
import math
import random
from Types import *

# This is a where we park signal functions.

pi       = math.pi
twopi    = 2*pi
sCeiling = math.ceil
sFloor = math.floor

def sFraction(x):
    return x - sFloor(x)

def staticLerp(t, x, y):
    return (1-t)*x + t*y

# Note that the destination is never changed.

def staticLerpA(t, x, y):
    x1 = x/twopi
    y1 = y/twopi
    x2 = twopi * (x1 - math.floor(x1))
    y2 = twopi * (y1 - math.floor(y1))
    if x2 < y2:
        if y2 - x2 > pi:
            return staticLerp(t, x2+twopi, y2)
        return staticLerp(t, x2, y2)
    else:
        if x2 - y2 > pi:
            return staticLerp(t, x2-2*pi, y2)
        return staticLerp(t, x2, y2)

# Normalize an angle to the -pi to pi range
def sNormA(a):
    a1 = a/twopi
    a2 = twopi * (a1 - math.floor(a1))
    return a2 if a2 <= pi else a2 - twopi


class Pair:
      def __init__(self, first, second):
          self.first = first
          self.second = second
          self.type = pairType(getPType(first), getPType(second))

def sPair(x,y):
    Pair(x, y)

def sFirst(p):
    p.first

def sSecond(p):
    p.second
    

# Random number stuff - static only!

def randomChoice(choices):
    return random.choice(choices)

def random01():
    return random.random()

def random11():
    return 2*random.random()-1

def randomRange(low, high = None):
    if high is None:
        return low * random01()
    return low + random01()*(high-low)

def randomInt(low, high = None):
    if high is None:
        return random.randint(0, low)
    return random.randint(low, high)

def shuffle(choices):
    c = list(choices)
    random.shuffle(c)
    return c

def sStep(x):
    if (x < 0):
        return 0
    else:
        return 1
    

def sSmoothStep(x):
    if (x < 0):
        return 0
    if (x > 1):
        return 1
    return x*x*(-2*x + 3)

random.seed()
