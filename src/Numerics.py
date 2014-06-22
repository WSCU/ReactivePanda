import Interp
from StaticNumerics import *
from Factory import *
from Types import *
import math
from SHPR import *
from Color import Color, colorHSL
from Interp import interpolateStatic
from Interp import repeat

pi       = math.pi
twopi    = 2*pi

p3       = lift("p3", SP3, types = [numType, numType, numType], outType = p3Type)
P3 = p3  # For backwards compatibility
p3C       = lift("P3C", SP3C, [numType, numType, numType], outType = p3Type)
P3C = p3C

p2       = lift("p2", SP2, types = [numType, numType], outType = p2Type)
P2 = p2
hpr      = lift("hpr", SHPR, types = [numType, numType, numType], outType = hprType)
HPR = hpr

getX     = lift("getX", lambda v:v.x, [hasXYType], numType)
getY     = lift("getY", lambda v:v.y, [hasXYType], numType)
getZ     = lift("getZ", lambda v:v.z, [p3Type], numType)

getH     = lift("getH", lambda v:v.h, [hprType], numType)
getP     = lift("getP", lambda v:v.p, [hprType], numType)
getR     = lift("getR", lambda v:v.r, [hprType], numType)

getUp    = lift("getUp", lambda hpr:getUpHPR(hpr), [hprType], p3Type)

radians  = lift("radians", math.radians, [numType], numType)
# Delete this from elsewhere, use math.degrees in update functions
degrees  = lift("degrees", math.degrees, [numType], numType)
sin      = lift("sin", math.sin, [numType], numType)
cos      = lift("cos", math.cos, [numType], numType)
tan      = lift("tan", math.tan, [numType], numType)
atan2    = lift("atan2", math.atan2, [numType, numType], numType)
sqrt     = lift("sqrt", math.sqrt, [numType], numType)
exp      = lift("exp", math.exp, [numType], numType)
pow      = lift("pow", math.pow, [numType,numType], numType)
log      = lift("log", math.log, [numType], numType)

ceiling  = lift("ceiling", sCeiling, [numType], numType)
floor    = lift("floor", sFloor, [numType], numType)
fraction = lift("fraction", sFraction, [numType], numType)
# sections
add      = lift("add", lambda x: lambda y: x+y, [numType], fnType)
sub      = lift("sub", lambda x: lambda y: y-x, [numType], fnType)
times    = lift("times", lambda x: lambda y: x*y, [numType], fnType)
div      = lift("div", lambda x: lambda y: x/y, [numType], fnType)

interpolate = lift("interpolate", interpolateStatic, [numType, numType], anyType)
forever = lift("forever", lambda i: repeat(-1, i), [numType], fnType)

#dot      = lift(lambda x,y: genDot(x,y), "dot", infer="dot")
const    = lift("const", lambda x: lambda y: x, [anyType], fnType)

color    = lift("rgb color", Color, [numType, numType, numType], colorType)
colora   = lift("rgb color", Color, [numType, numType, numType, numType], colorType)
colorhsl = lift("hsl color", colorHSL, [numType, numType, numType], colorType)

string   = lift("string", str, [anyType], stringType)

#norm      = lift(normP3, 'norm', [P3Type], P3Type)


P3toHPR = lift("P3toHPR", sP3toHPR, [p3Type], hprType)
p3ToHpr = P3toHPR

HPRtoP3 = lift("HPRtoP3", sHPRtoP3, [hprType], p3Type)
hprToP3 = HPRtoP3

normA = lift("normA", sNormA, [numType], numType)

def dist(x,y):
    return abs(x-y)


format    = lift("format", lambda str, *a: str % a)

# Lifted conditional

def staticIf(test, x, y):
    if test:
        return x
    return y

choose = lift("choose", staticIf)

# Interpolation functions

lerp = lift("lerp", Interp.lerpStatic)
interpolate = lift("interpolate", Interp.interpolateStatic)


def encodeNums(*n):
    s = ""
    r = ""
    for num in n:
        r = r + s + str(num)
        s = ","
    return r

def decodeNums(s, f):
    nums = s.split(",")
    return f(*map(lambda x: float(x.strip()), nums))

p3Type.encoder = lambda p: encodeNums(p.x, p.y, p.z)
p3Type.decoder = lambda s: decodeNums(s, p3)

p2Type.encoder = lambda p: encodeNums(p.x, p.y)
p2Type.decoder = lambda s: decodeNums(s, p2)

hprType.encoder = lambda p: encodeNums(p.h, p.p, p.r)
hprType.decoder = lambda s: decodeNums(s, hpr)