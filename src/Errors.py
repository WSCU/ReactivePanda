import sys
import Signal
from Types import *

def checkEvent(evt, context):
    if not isinstance(evt, Signal.EventValue):
        print "Error: " + str(evt) + " is not an event value in " + context
        sys.exit()
    return

def badKeyName(n):
    print str(n) + " is not a valid key name"
    sys.exit()