"""
    This is temporary, quick hack to get everything working.

    jp is not pleased!  This should all be in pythonfrp
"""
from pythonfrp.Signal import *
from pythonfrp.Functions import *
import pythonfrp.Globals as frpGlobals
from . import Camera
from . import World
from . Externals import initEvents, pollGUI
from direct.task import Task


def heartBeat(ct, events):
    #print "objects " + str(len(frpGlobals.worldObjects))
    frpGlobals.dt = ct - frpGlobals.currentTime
    frpGlobals.currentTime = ct
    frpGlobals.events = events
    frpGlobals.newEvents = {}
    frpGlobals.thunks = []

    pollGUI()

    #print "time steps: "+repr(ct)
    #for event in events:
        #print "Events: "+repr(event)
    reactions = []
    for worldObject in frpGlobals.worldObjects:
        #print("Updating object: " + repr(worldObject))
        #print repr(worldObject)
        reactions.extend(worldObject._update())
    for thunk in frpGlobals.thunks:
        thunk()
    for reaction in reactions:
        reaction.react()
    for obj in frpGlobals.newObjects:
        #print("Adding object: " + repr(obj))
        frpGlobals.worldObjects.append(obj)
    frpGlobals.newObjects = []
    for obj in frpGlobals.worldObjects:
        #print("Initializing object: " + repr(obj))
        obj._initialize()
    if frpGlobals.resetFlag is not None:
        for m in frpGlobals.worldObjects:
            if m is not World.world and m is not Camera.camera:
                exit(m)
        frpGlobals.nextNE2dY = .95 # Positioning for 2-D controls - old controls should be gone
        frpGlobals.nextNW2dY = .95
        Proxy.clearReactions(World.world)
        Proxy.clearReactions(Camera.camera)
        frpGlobals.worldObjects.append(World.world)
        frpGlobals.worldObjects.append(Camera.camera) # Keep these in the update list
        frpGlobals.resetFlag()
        frpGlobals.currentTime = 0
        frpGlobals.resetFlag = None
#will need to check the proxy module to find the right name for this initialize method
#make an initialize method that clears out all the variables and resets the clock
def initialize(ct):
    frpGlobals.thunks = []
    frpGlobals.currentTime = 0 #Not sure if this should be 0 or CT
    frpGlobals.newModels = []
    frpGlobals.worldObjects = {}
    frpGlobals.events = []
    Camera.panda3dCamera = Camera.camera #Panda3-D built in camera
    frpGlobals.world = world

def engine(ct):
    #Initialize all signals (signalF.start)
    #set the time to 0
    #get events and clear thunks
    frpGlobals.currentTime = ct
    initEvents()
    taskMgr.add(stepTask, 'PandaClock')
    run()

def stepTask(task):
    heartBeat(task.time, frpGlobals.newEvents) # The task contains the elapsed time
    return Task.cont

