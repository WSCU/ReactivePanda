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

P3       = lift("SP3", SP3, types = [numType, numType, numType], outType = p3Type)
p3 = P3
P2       = lift("SP2", SP2, types = [numType, numType], outType = p2Type)
p2 = P2
HPR      = lift("hpr", SHPR, types = [numType, numType, numType], outType = hprType)
hpr = HPR
P3C       = lift('P3C',SP3C,[numType, numType, numType], outType = p3Type)
p3c = P3C

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
max      = lift("max", max, [numType,numType], numType)
min      = lift("min", min, [numType,numType], numType)
# sections
add      = lift("add", lambda x: lambda y: x+y, [numType], fnType)
sub      = lift("sub", lambda x: lambda y: y-x, [numType], fnType)
times    = lift("times", lambda x: lambda y: x*y, [numType], fnType)
div      = lift("div", lambda x: lambda y: x/y, [numType], fnType)

#dot      = lift(lambda x,y: genDot(x,y), "dot", infer="dot")
const    = lift("const", lambda x: lambda y: x, [anyType], fnType)

color    = lift("rgb color", Color, [numType, numType, numType], colorType)
colora   = lift("rgb color", Color, [numType, numType, numType, numType], colorType)
colorhsl = lift("hsl color", colorHSL, [numType, numType, numType], colorType)

getR     = lift("getR", lambda x: x.r, [colorType], numType)
getG     = lift("getG", lambda x: x.g, [colorType], numType)
getB     = lift("getB", lambda x: x.b, [colorType], numType)

getCH     = lift("getH", lambda x: x.getH(), [colorType], numType)
getCS     = lift("getS", lambda x: x.getS(), [colorType], numType)
getCL     = lift("getL", lambda x: x.getL(), [colorType], numType)

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
