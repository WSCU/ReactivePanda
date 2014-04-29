from StaticNumerics import *
from Factory import *
from Types import *
import math
from SHPR import *

pi       = maybeLift(math.pi)
twopi    = maybeLift(2*pi)
ceiling = lift("ceiling",math.ceil)
floor   = lift("floor",math.floor)
cos = lift("cos",math.cos)
sin = lift("sin", math.sin)

P3 = lift("SP3", SP3, types = [numType, numType, numType], outType = p3Type)
p3 = P3
P2 = lift("SP2", SP2, types = [numType, numType], outType = p2Type)
p2 = P2
HPR = lift("hpr", SHPR)
hpr = HPR
