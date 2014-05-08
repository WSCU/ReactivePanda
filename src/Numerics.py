from StaticNumerics import *
from Factory import *
from Types import *
import math
from SHPR import *
from Color import Color, colorHSL
from Interp import interpolateStatic

pi       = maybeLift(math.pi)
twopi    = maybeLift(2*pi)
ceiling  = lift("ceiling",math.ceil)
floor    = lift("floor",math.floor)
cos      = lift("cos",math.cos)
sin      = lift("sin", math.sin)

P3       = lift("SP3", SP3, types = [numType, numType, numType], outType = p3Type)
p3 = P3
P2       = lift("SP2", SP2, types = [numType, numType], outType = p2Type)
p2 = P2
HPR      = lift("hpr", SHPR)
hpr = HPR

gravity  = P3(0,0,-1)

getX     = lift("getX", lambda v:v.x, [hasXYType], numType)
getY     = lift("getY", lambda v:v.y, [hasXYType], numType)
getZ     = lift("getZ", lambda v:v.z, [p3Type], numType)

getH     = lift("getH", lambda v:v.h, [hprType], numType)
getP     = lift("getP", lambda v:v.p, [hprType], numType)
getR     = lift("getR", lambda v:v.r, [hprType], numType)

getUp    = lift("getUp", lambda hpr:getUpHPR(hpr), [hprType], p3Type)

radians  = lift("radians", math.radians, [numType], numType)
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

interpolate = lift("interpolate", interpolateStatic, [numType], anyType)

#dot      = lift(lambda x,y: genDot(x,y), "dot", infer="dot")
const    = lift("const", lambda x: lambda y: x, [anyType], fnType)

color    = lift("rgb color", Color, [numType, numType, numType], colorType)
colora   = lift("rgb color", Color, [numType, numType, numType, numType], colorType)
colorhsl = lift("hsl color", colorHSL, [numType, numType, numType], colorHSLType)

string   = lift("string", str, [anyType], stringType)
