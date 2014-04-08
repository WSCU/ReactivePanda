"""
This handles the typing of signal functions

Composite types such as P2, P3, and HPR are serialized as numbers separated by commas.
This parses those numbers.
"""

# Every built-in type has a python-defined type
# User defined types have a type attribute.  This enables initialization time typechecking

class Ptype:
    def __init__(self, tname, subtypes = []):
        self.tname = tname
        self.subtypes = subtypes # list of Ptypes
    def __str__(self):
        r = self.tname
        return r
    


#  Predefined types used elsewhere
SignalType = Ptype("Signal")
SignalFactory = Ptype("SignalFactory")
'''  Keeping just in case
numType = ptype("Number")
fnType = ptype("Function")
boolType = ptype("Boolean")
stringType = ptype("String")
noneType = ptype("None")
P3Type = ptype("3-D Point")
HPRType = ptype("HPR")
P2Type = ptype("2-D Point")
controlType = ptype("A control signal")
anyType = ptype('Any type')
noneEType = ptype('Event')
numType1 = [numType]
numType2 = [numType, numType]
numType3 = [numType, numType, numType]
ColorType = ptype('Color')
ColorHSLType = ptype('ColorHSL')
NeverType = ptype("Never")
SoundType = ptype("Sound")
TupleType = ptype("Tuple")
SoundEventType = eventType(SoundType)
StaticType = ptype("Static")
EventBoolType = ptype("Event")
EventNumType = ptype("Event")
EventAnyType = ptype("Event")
hasXYType = ptype("2-D / 3-D Point", subtypes = [P2Type, P3Type])
scalableType = ptype("scalable", subtypes = [numType, P2Type, P3Type, HPRType])
interpableType = ptype("interp", subtypes = [numType, P2Type, P3Type, ColorType, controlType, HPRType])
addableType = ptype("addable", subtypes = [numType, P2Type, P3Type, stringType, controlType, HPRType])
StringListType = ptype("String Pair List")
zeroType = ptype("Zero")
zero.type = zeroType
numType.zero = 0
'''


def getPType(x):
    if hasattr(x,'type'):  # Panda types all have a pType slot
        return x.type
    if x is None:
        return noneType
    t = type(x)
    return Ptype("Unknown: " + str(t))



