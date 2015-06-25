import math
from pythonfrp.StaticNumerics import pi, SP2, SP3
from SHPR import SHPR

def sP3toHPR(p):
    return SHPR(math.atan2(p.y, p.x) + pi / 2,
                math.atan2(p.z, abs(SP2(p.x, p.y))),
                0)

def sHPRtoP3(p):
    return SP3(math.sin(p.h) * math.cos(p.p),
               -math.cos(p.h) * math.cos(p.p),
               -math.sin(p.p))
