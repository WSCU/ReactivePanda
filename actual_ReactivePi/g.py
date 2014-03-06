
# Globals are defined here.  Every module should have an
#  import g

# need platform to check os
from __future__ import division  # Prevent integer division
import platform



# Many of these duplicate top level names ("world", "cam") but the top level
# name shouldn't be used with the library to avoid initialization problems

currentTime = 0      # The current global time
world = None         # The world object, exported to the user variable world
objectNames = None   # Hands out unique name to every panda object
eventSignals = {}
events = {}          # This is a dictionary of all events posted in the previous tick interval
reactEvents = []     # Reactions that are not part of an object
eventSignals = None  # This is a dictionary of event values received since the last tick
newModels = []       # The new list of active models assembled at every tick
thunks = []
tccontext = None
nextModelId = 0
startTime = 0
fastEVents = []
pwmTicks = 10

# Math functions

add = None
sub = None
mul = None
abs = None

# Used to identify signals

nextSignalRef = 0


