"""
This handles the typing of signal functions

Composite types such as P2, P3, and HPR are serialized as numbers separated by commas.
This parses those numbers.
"""

from types import *

# Every built-in type has a python-defined type
# User defined types have a type attribute.  This enables initialization time typechecking

class Ptype:
    def __init__(self, tname, parent, addable = False, encoder = None, decoder = None):
        self.tname = tname
        self.addable = addable
        self.encoder = encoder
        self.decoder = decoder
        if parent is None:
            self.parent = self
        else:
            self.parent = parent

    def includes(self, itype):
        if itype is self or self is anyType:
            return True
        elif self.parent.includes(itype):
            return True
        else:
            return False

    def encode(self, x):
        if self.encoder is None:
            print "No encoder for type " + str(self)
            return None
        return self.encoder(x)

    def decode(self, x):
        if self.decoder is None:
            print "No decoder for type " + str(self)
            return None
        return self.decoder(x)

    def __str__(self):
        r = self.tname
        return r

def expectedArgCount(args, n):
    return len(args) is n

def addCheck(self):
    if self.name is "add" or self.name is "subtract":
        if self.outType.addable:
            if expectedArgCount(self.args, 2) and self.types[0].includes(self.types[1]):
                return True
            else:
                print "Tried to add/subtract incompatible types" 
        else:
            print "Non Addable Type: " + str(self.outType)
        return False
    return True
    
def getPtype(self):
    return self._type
    
def checkType(self, value, ptype):
    if value._type is ptype:
        return True
    return False

#  Predefined types used elsewhere
anyType = Ptype("Any", None, addable = True)
signalType = Ptype("Signal", anyType)
signalFactoryType = Ptype("Signal Factory", anyType)
proxyType = Ptype("Proxy", anyType)
numType = Ptype("Num", anyType, addable = True, encoder = lambda x: str(x), decoder = lambda x: float(x.strip()))
hasXYType = Ptype("hasXY", numType, addable = True)
p2Type = Ptype("P2", hasXYType, addable = True)
p3Type = Ptype("P3", hasXYType, addable = True)
hprType = Ptype("HPR", numType, addable = True)
boolType = Ptype("Boolean", anyType, encoder = lambda x: "T" if x else "F", decoder = lambda s: True if s.equals("T") else False)
stringType = Ptype("String", anyType)
eventType = Ptype("Event", anyType)
fnType = Ptype("Function", anyType)
colorType = Ptype("Color", numType)
colorHSLType = Ptype("HSL Color", numType)
interpableType = Ptype("Interp", anyType)
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
