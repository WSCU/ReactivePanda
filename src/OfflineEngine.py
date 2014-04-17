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
            print("Updating object: " + str(worldObject))
        Globals.thunks.extend(worldObject.update())
    for e in Globals.events:
        if verbose and not test:
            print("Event " + str(e) + " is firing")
    for f in Globals.thunks:
        f()
    for obj in Globals.newObjects:
        if verbose and not test:
            print("Adding object: " + str(obj))
        Globals.worldObjects.append(obj)
    Globals.newObjects = []
    for obj in Globals.worldObjects:
        if verbose and not test:
            print("Initializing object: " + str(obj))
        obj.initialize()

#will need to check the proxy module to find the right name for this initialize method
#make an initialize method that clears out all the variables and resets the clock
def initialize(ct):
    Globals.thunks = []
    Globals.currentTime = 0 #Not sure if this should be 0 or CT
    Globals.newModels = []
    Globals.worldObjects = {}
    Globals.events = []

#simevents is a list of tuples, time and signal
def engine(tSteps, verbose = False, test = None):
    #Initialize all signals (signalF.start)
    #set the time to 0
    #get events and clear thunks
    #Split event list into seperate lists
    eventLists = {}
    for i in Globals.simEvents:
        if type(i) is str:
            k = i
            if k not in eventLists:
                eventLists[k] = []
        elif type(i) is not str:
            eventLists[k].append(i)

    Globals.currentTime = 0
    steps = 0
    while steps < tSteps:
        if verbose and test is None:
            print("\nThe time is now: " + str(steps))
        events = {}
        for k, v in eventLists.items():
            for i in v:
                if i[0] == steps:
                    events[k] = i[1]
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

def printUpdate(proxy):
    for k, v in proxy._signals.items():
        print (k + ": " + str(v.state))

def leftMouseEvents(l):
    e = []
    for i in l:
        e.append((i, True))
    Globals.simEvents.extend(["LBP"] + e)
    
def rightMouseEvents(l):
    e = []
    for i in l:
        e.append((i, True))
    Globals.simEvents.extend(["RBP"] + e)

p = printer(name = "integral", i = integral(1))
#q = printer(name = "integral 2", i = integral(p.i))
leftMouseEvents([1, 2, 3, 7, 19, 32])
rightMouseEvents([1, 2, 4, 5])
def main():
       engine(50, verbose = True) 
if __name__ == "__main__":
    main()

