
# These are random utility functions that don't seem to be 
# appropriate elsewhere

from Numerics import *
from World import *
from FRP import *


def itime(i):
    return interpolate(time, i)

def itimef(i):
    return interpolate(time, forever(i + reverse(i)))

