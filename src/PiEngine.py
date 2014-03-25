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
    for k,v in signals.iteritems():
        Globals.sl[k] = maybeLift(v).start()
    Globals.currentTime = 0
    Globals.dt = 1
    
    print sl.viewkeys()
    while Globals.currentTime < clock.now():
        #Globals.thunks = []
        if (events and Globals.currentTime >= events[0][0]):
            print ("An event was popped " + str(events[0][1]))
            Globals.events.append(events.pop(0))
        for k,v in sl.iteritems(): #k = key, v = value in the dictionary
            print(str(k)+ " = "+str(v.now()))
        for f in thunks:
            f()
            
        Globals.thunks = [] 
        print("reactive engine time = "+ str(Globals.currentTime))    
        Globals.currentTime = Globals.currentTime+ Globals.dt
        clock.now()
    
