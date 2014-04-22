#This creates top level GUI signals and the world and cam objects.
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

 # These methods handle signals from the GUI
  # Cache keypress events so there's no duplication of key events - not
  # sure this is useful but it can't hurt.  Probably not a good idea to
  # have multiple accepts for the same event.

def getEventSignal(ename, val):
        if Globals.events.has_key(ename):
            return Globals.events[ename]
        e = EventMonitor(ename)
        Globals.events[ename] = e
        Globals.directObj.accept(ename, lambda: postEvent(ename))
        return Globals.events[ename]

# This saves event occurances in g.newEvents
def postEvent(ename, val = True):
        Globals.newEvents[ename] = val

lbutton = Globals.lbutton
rbutton = Globals.rbutton
rbuttonPull = Globals.rbuttonPull
lbuttonPull = Globals.lbuttonPull

def key(kname, val = True):
    kname = checkValidKey(kname)
    return getEventSignal(kname, val)

def keyUp(kname, val = True):
    kname = checkValidKey(kname)
    return getEventSignal(kname + "-up", val)

def leftClick(model, val = True):
    return getEventSignal(model.d.model.getTag('rpandaid') + "-leftclick", val)

def rightClick(model, val = True):
    return getEventSignal(model.d.model.getTag('rpandaid') + "-rightclick", val)

allKeyNames = ["escape", "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12",
               "backspace", "insert", "home", 
               "tab",  "delete", "end", "enter", "space"]

keyRenamings = {"upArrow": "arrow_up", "downArrow": "arrow_down",
                "leftArrow": "arrow_left", "rightArrow": "arrow_right",
                "pageUp": "page_up", "pageDown": "page_down", " ": "space"}
                



