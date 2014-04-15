# This creates top level GUI signals and the world and cam objects.
import direct.directbase.DirectStart          # start panda
from direct.showbase import DirectObject      # for event handling
from direct.actor import Actor                # allow use of actor
from direct.gui.DirectGui import *
from Signal import *
from Numerics import *
from Proxy import *
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import OnscreenText
import Globals

class Camera(Proxy):
  def __init__(self):
     Globals.cam = self
     Proxy.__init__(self, name = "camera", updater =None)
     self._signals['position'] = P3(0, -10, 0)
     self._signals['hpr'] = HPR(0, 0, 0)
     
class World(Proxy):
# This initialization code sets up global variables in g as well as the
# world object internals
  def __init__(self):
     Globals.world = self
     Proxy.__init__(self, name = "World", )
     # Signals native to the world object - note that all have defaults
     self._signals['color']   = None

  def refresh(self):
    self.update(self)
    # Check all world-level events
    

  def kill(self):
       print "World object received a kill signal"
       exit()
#User level button pushes?
def lbp(e = True): 
    return getEventSignal("mouse1", e)

def rbp(e = True):
    return getEventSignal("mouse3", e)

def lbr(e = True):
    return getEventSignal("mouse1-up", e)

def rbr(e = True):
    return getEventSignal("mouse3-up", e)

