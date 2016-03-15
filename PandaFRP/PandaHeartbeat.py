from direct.task import Task
import pythonfrp.Globals as frpGlobals
from PandaFRP import PandaWorld
from PandaSRC.Externals import initEvents, pollGUI
from ReactivePanda.PandaSRC import Camera
from pythonfrp.Functions import *
from pythonfrp.Engine import heartbeat

def engine(ct):
    #Initialize all signals (signalF.start)
    #set the time to 0
    #get events and clear thunks
    frpGlobals.currentTime = ct
    initEvents()
    taskMgr.add(stepTask, 'PandaClock')
    run()

def stepTask(task):
    heartbeat(task.time, frpGlobals.newEvents) # The task contains the elapsed time
    pollGUI()
    return Task.cont

