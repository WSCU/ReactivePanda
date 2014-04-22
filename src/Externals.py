import Globals
from Factory import *
from Signal import *
from direct.actor import Actor
from direct.showbase import DirectObject
"""
class ExternalF(SFact):
    def __init__(self, fn):
        SFact.__init__(self)
        self.fn = fn
    def start(self):
        return ExternalS(fn)

class ExternalS(Signal):
    def __init__(self, fn):
        Signal.__init__(self)
    def now(self):
       fn(Globals.currentTime) 
"""

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
        e = eventObserver(ename)
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
Globals.directObj = DirectObject.DirectObject()
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
def initEvents():
    lbp()
    rbp()
    lbr()
    rbr()
    """
    key()
    keyUp()
    
    leftClick()
    rightClick()"""
    