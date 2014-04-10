import unittest
import time
import Globals
import sys
from Signal import *
from Functions import *
from Proxy import *

def heartBeat(ct, events, verbose = False, test = False):
    #print "objects " + str(len(Globals.worldObjects))
    Globals.dt = ct - Globals.currentTime
    Globals.currentTime = ct
    Globals.events = events
    Globals.thunks = []
    for worldObject in Globals.worldObjects:
        if verbose and not test:
            print("Updating object: " + repr(worldObject))
        Globals.thunks.extend(worldObject.update())
    for f in Globals.thunks:
        f()
    for obj in Globals.newObjects:
        if verbose and not test:
            print("Adding object: " + repr(obj))
        Globals.worldObjects.append(obj)
    Globals.newObjects = []
    for obj in Globals.worldObjects:
        if verbose and not test:
            print("Initializing object: " + repr(obj))
        obj.initialize()
#will need to check the proxy module to find the right name for this initialize method
#make an initialize method that clears out all the variables and resets the clock
def initialize(ct):
    Globals.thunks = []
    Globals.currentTime = 0 #Not sure if this should be 0 or CT
    Globals.newModels = []
    Globals.worldObjects = {}
    Globals.events = []

def engine(tSteps, simevents = [], verbose = False, test = None):
    #Initialize all signals (signalF.start)
    #set the time to 0
    #get events and clear thunks
    Globals.currentTime = 0
    steps = 0
    while steps < tSteps:
        events = []
        for e in simevents:
            if e[0] <= steps:
                events.append(e)
        heartBeat(steps, events, verbose=verbose)
        steps+=1
#one reactive objects, reactive attributes, print all the attributes
#controlled while loop, dont use time.time(), step time by one.
#Like the really old engine
class Printer(Proxy):
    def __init__(self, name, args):
        Proxy.__init__(self, name, printUpdate)
        for k, v in args.items():
            self.k = v

def printer(name = "test object", **kwargs):
    return Printer(name, kwargs)

def printUpdate(self):
    for k, v in self._signals.items():
        print v.state

p = printer(name = "integral", i = integral(1))
q = printer(name = "integral 2", i = integral(p.i))
def main():
       engine(50, verbose = True) 
if __name__ == "__main__":
    main()
