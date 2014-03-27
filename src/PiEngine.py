# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import sched, time
import piface.pfio as piface
from Signal import *
from Functions import *
from Globals import *


def engine(ct, *args):
    #Initialize all signals (signalF.start)
    #set the time to 0
    #get events and clear thunks
    Globals.currentTime = ct
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
        for obj in Globals.Objects:
            obj.init()
    #make an initialize method that clears out all the variables and resets the clock
    def initialize(ct):
        Globals.thunks = []
        Globals.currentTime = 0 #Not sure if this should be 0 or CT
        Globals.newModels = []
        Globals.worldObjects = {}
        Globals.events = []
    
