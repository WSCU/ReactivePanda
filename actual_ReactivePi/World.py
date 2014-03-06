# World.py

# Done

# This creates top level GUI signals and the world and cam objects.


from Time import *
from Signal import *
from Numerics import *
from Types import *
from Switchers import *
from copy import copy
from Handle import *
from FRP import tag, hold, typedVar, timeIs, localTimeIs
import sys,os
from random import *
from g import * # Global names



class World(Handle):
# This initialization code sets up global variables in g as well as the
# world object internals
  def __init__(self):
     g.world = self
     Handle.__init__(self, isWorld = True, name = "World")

  def refresh(self):
    Handle.refresh(self)
    # Check all world-level events
    for w in g.reactEvents:
        w.check()

  def kill(self):
       print "World object received a kill signal"
       exit()

def initializeGlobals():
     g.eventSignals = {}
     g.newEvents = {}
     g.events = {}
     g.reactEvents = []
     g.newModels = []
     g.tccontext = None
     g.world = world



# Initialize the environment
initTime()     #  Sets current time to 0

# Exported vocabulary
world = World()
initializeGlobals()
# The underlying Panda3D system uses the name "camera" so we'll use "cam" instead
# Bring the GUI behaviors / events to the user namespace

def react(event, handler):
    world.react(event, handler)

def react1(event, handler):
    world.react1(event, handler)

def when(event, handler):
    world.when(event, handler)

def when1(event, handler):
    world.when1(event, handler)

def atTime(n, r):
    react(timeIs(n), lambda m,v: r())

def atLocalTime(n, r):
    react(localTimeIs(n), lambda m, v: r())

