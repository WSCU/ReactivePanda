import sys
import Signal
from Types import *

def checkEvent(evt, context):
    if not isinstance(evt, Signal.EventValue):
        print("Error: " + str(evt) + " is not an event value in " + context)
        sys.exit()
    return

def badKeyName(n):
    print(str(n) + " is not a valid key name")
    sys.exit()

def errorOnStaticTypes(func, correct, y):
    print(func + " of " + correct + " bad argument: " + repr(y))
    sys.exit()

def typeError(expected, got, name, attr):
    print("in " + str(name) + ", attribute " + str(attr) + ", expected: " + str(expected) + ", but recieved: " + str(got))
    sys.exit()