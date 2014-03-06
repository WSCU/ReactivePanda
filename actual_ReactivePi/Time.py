# Done

# This implements the main event loop using a panda task.  This is where
# reactive values are sustained.

import g
from copy import copy
from StaticNumerics import *
    
# This carries the system one timestep forward.  The arguments are
# the current time and the table of events that have occured since the
# last heartbeat.  The events value is a dictionary from (internal) event names
# to event values

def heartbeat(t, events):
    g.currentTime  = t 
    # Look for models that were introduced during the previous step
#    print g.newModels
    for newModel in g.newModels:
        newModel.checkSignals(g.currentTime)
        newModel.d.switches = newModel.d.newswitches
        g.models.append(newModel)
    g.newModels = []
    g.thunks = []
    # print "Stepping at " + str(g.currentTime)
    g.events = events
    #pollGUI()   # Read signals from the external GUI
    # Then refresh everything
    g.switched = False
    for m in g.models:
        m.refresh()
        m.d.newswitches = []  # For the next loop
        m.d.undefined = []    # For the next loop
    # Look for switching
    oldModels = copy(g.models)  # In case new models are added
    for m in oldModels:
        m.switch()
    # If any models have switched, reinitialize these new signals
    if g.switched:
       ctxt = g.currentTime
       for m in g.models:
           m.checkSignals(ctxt)
           m.d.switches = m.d.switches + m.d.newswitches # Add in new switchers
    # Force all unevaluated thunks (avoids time leaks)
    for t in g.thunks:
        t.force()

# Start initialize the world object

def initTime():
    g.currentTime = 0
    g.models = []
    g.thunks = []
    g.objectNames = {}
    g.fastEvents = []


# This is used to give unique names to each handle

def uniqueName(baseName):
    if g.objectNames.has_key(baseName):
        n = g.objectNames[baseName]
        n = n + 1
        g.objectNames[baseName] = n
        return baseName + str(n)
    g.objectNames[baseName] = 0
    return baseName

