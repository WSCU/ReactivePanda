

# This handles the typing of signal functions

# Every built-in type has a python-defined type
# User defined types have a type attribute.  This enables initialization time typechecking

# The only polymorphic type here is the event type.  Note that with implicit lifting,
# there is no distinction between Behavior t and t.

# It isn't clear that this is worth all of the effort!

class ptype:
    def __init__(self, tname, subtypes = [], innerTypes = []):
        self.tname = tname
        self.subtypes = subtypes
        self.innerTypes = innerTypes
    def implies(self, t2):
        if self is anyType:
            return True
        if t2 is anyType:  # Found with forward reference
            return True
        if self is EventAnyType:
            return t2.tname == 'Event'
        if t2 is EventAnyType:
            return self.tname == 'Event'
        if t2 is self:
            return True
        return t2 in self.subtypes
    def __str__(self):
        r = self.tname
        if self.innerTypes != []:
            r = r + " <"
            for ty in self.innerTypes:
                r = r + str(ty) + " "
            r = r + ">"
        return r

def eventType(t):
    return ptype("Event", innerTypes = [t])

def pairType(t1, t2):
    return ptype("Pair", innerTypes = [t1, t2])

def anEventType(t):
    return t.tname == "Event"



def anInterpType(t):
    return t.tname == "Interp"

# Should be in errors but there's a circular import problem
def checkInterpType(t):
    if not anInterpType(t):
        print 'Not an interpolation: ' + str(t)
        exit()

def checkSameInterp(ty1, ty2):
    if ty1.innerTypes != ty2.innerTypes:
        print 'Mismatched types ' + str(ty1) + ' and ' + str(ty2) + ' in interpolation'
        exit()

#  Predefined types used elsewhere

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
noneEType = ptype('Event', innerTypes = [anyType])
noneType  = ptype('None')
numType1 = [numType]
numType2 = [numType, numType]
numType3 = [numType, numType, numType]
hasXYType = ptype("2-D / 3-D Point", subtypes = [P2Type, P3Type])
ColorType = ptype('Color')
scalableType = ptype("scalable", subtypes = [numType, P2Type, P3Type, HPRType])
interpableType = ptype("interp", subtypes = [numType, P2Type, P3Type, ColorType, controlType, HPRType])
addableType = ptype("addable", subtypes = [numType, P2Type, P3Type, stringType, controlType, HPRType])
NeverType = ptype("Never")
EventBoolType = ptype("Event", innerTypes = [boolType])
EventNumType = ptype("Event", innerTypes = [numType])
EventAnyType = ptype("Event", innerTypes = [anyType])
SoundType = ptype("Sound")
TupleType = ptype("Tuple")
SoundEventType = eventType(SoundType)
StaticType = ptype("Static")

numType.zero = 0

# Check if the type can be interped?
def interpableType(t):
    return t is P2Type or t is P3Type or t is HPRType or t is ColorType or \
           t is numType or t is controlType

def interpType(t):
    r = ptype("Interp", innerTypes = [t])
    return r

def checkInterpableType(t):
    if not interpType(t):
        print "Can't interpolate type " + str(t)
        exit()

# return the type of an object - either stored in a Panda object or using
# the primitive python type function.

def getPType(x):
    if hasattr(x,'type'):  # Panda types all have a pType slot
        return x.type
    if x is None:
        return noneType
    t = type(x)
    if t is type(1):
        return numType
    if t is type(1.0):
        return numType
    if t is type(True):
        return boolType
    if t is type('abc'):
        return stringType
    if t is type((1,2)):
        return TupleType

    return ptype("Unknown: " + str(t))


