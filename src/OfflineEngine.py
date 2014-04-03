import unittest
import time
import Globals
from Signal import *
from Functions import *
from Proxy import *

def heartBeat(ct, events, verbose = False):
    #print "objects " + str(len(Globals.worldObjects))
    Globals.dt = ct - Globals.currentTime
    Globals.currentTime = ct
    Globals.events = events
    Globals.thunks = []
    for worldObject in Globals.worldObjects:
        if verbose:
            print("Updating object: " + repr(worldObject))
        Globals.thunks.extend(worldObject.update())
    for f in Globals.thunks:
        f()
    for obj in Globals.newObjects:
        if verbose:
            print("Adding object: " + repr(obj))
        Globals.worldObjects.append(obj)
    Globals.newObjects = []
    for obj in Globals.worldObjects:
        if verbose:
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

def engine(tSteps, verbose = False):
    #Initialize all signals (signalF.start)
    #set the time to 0
    #get events and clear thunks
    Globals.currentTime = 0
    steps = 0
    while steps < tSteps:
        heartBeat(steps, Globals.newEvents, verbose=verbose)
        steps+=1
#one reactive objects, reactive attributes, print all the attributes
#controlled while loop, dont use time.time(), step time by one.
#Like the really old engine

class ReactiveTestObject(Proxy):
    def __init__(self, name, updater):
        Proxy.__init__(self, name, updater)
        self.i1 = integral(1)
        
def update(self):
    for k, v in self._signals.items():
        print v.state

def test(name, updater):
    return ReactiveTestObject(name, updater)

t = test("test", update)

engine(50, verbose = True)
