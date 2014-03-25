# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import sched, time
from Signal import *
from Functions import *
from Globals import *

def engine(signals, events, clock):
    #Initialize all signals (signalF.start)
    #set the time to 0
    #get events and clear thunks
    runningSignals = {}
    for k,v in signals.iteritems(): #should be a list of proxy objects
        Globals.sl[k] = maybeLift(v).start()
    Globals.currentTime = 0
    Globals.dt = 1
    #Make a heartbeat method
    def heartBeat(ct, events):
        Globals.dt = ct - Globals.currentTime
        Globals.currentTime = ct
        Globals.newModels = []
        Globals.events = events
        Globals.thunks = []
        for worldObjects in Globals.worldObjects:
            Globals.thunks.append(worldObjects.update())
        for f in thunks:
            f()
        for objects in Globals.newModels:
            Globals.worldObjects.append(objects).initialize(ct) #will need to check the proxy module to find the right name for this initialize method
        
    #make an initialize method that clears out all the variables and resets the clock
    def initialize(ct):
        Globals.thunks = []
        Globals.currentTime = 0 #Not sure if this should be 0 or CT
        Globals.newModels = []
        Globals.worldObjects = {}
        Globals.events = []
    
