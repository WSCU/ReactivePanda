from Signal import *
from StaticNumerics import *
from Interp import *
import math
#from Color import Color
#from Control import *
import random

# Basic constructors

radians   = lift(math.radians, "radians", numType1, numType)
degrees   = lift(math.degrees, "degrees", numType1, numType)
sin       = lift(math.sin, "sin", numType1, numType)
cos       = lift(math.cos, "cos", numType1, numType)
tan       = lift(math.tan, "tan", numType1, numType)
atan2     = lift(math.atan2, 'atan2', numType2, numType)
sqrt      = lift(math.sqrt, 'sqrt', numType1, numType)
exp       = lift(math.exp, "exp", numType1, numType)
pow       = lift(math.pow, "pow", numType2, numType)
log       = lift(math.log, "log", numType1, numType)

ceiling   = lift(sCeiling, "ceiling", numType1, numType)
floor     = lift(sFloor, "floor", numType1, numType)
fraction  = lift(sFraction, "fraction", numType1, numType)
# sections
add       = lift(lambda x: lambda y: x+y, "add", numType1, fnType)
sub       = lift(lambda x: lambda y: y-x, "sub", numType1, fnType)
times     = lift(lambda x: lambda y: x*y, "times", numType1, fnType)
div       = lift(lambda x: lambda y: x/y, "div", numType1, fnType)

dot       = lift(lambda x,y: genDot(x,y), "dot", infer="dot")
const     = lift(lambda x: lambda y: x, "const", [anyType], fnType)

string    = lift(str, 'string', [anyType], stringType)

# Interpolation stuff

lerp = lift(lerpStatic, "lerp", infer='interpolate')
interpolate = lift(interpolateStatic, "interpolate", [numType,anyType], anyType)
to = lift(toS, "to", infer = "interpolate")
at = lift(atS, "at", infer = "interpolate")
move = lift(moveS, "move", infer = "interpolate")
repeat = lift(repeatS, "repeat", infer = "interpolate")
reverse = lift(reverseS, "reverse", infer = "interpolate")
forever = lift(lambda i: repeatS(-1, i), "forever", infer = "interpolate")
    


format    = lift(lambda str, *a: str % a, "format", infer = 'format')

# Lifted conditional

def staticIf(test, x, y):
    if test:
        return x
    return y

choose = lift(staticIf, "choose", infer = "choose")

def rand(i = None):
    if i is None:
        return random.random()
    if type(i) is type([]):
        return random.choice(i)
    return random.randint(0, i)


step = lift(sStep, "step", numType1, numType)
smoothStep = lift(sSmoothStep, "step", numType1, numType)
