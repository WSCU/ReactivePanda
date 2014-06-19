
import Globals
from Factory import *
from Signal import *
from direct.actor import Actor
from direct.showbase.DirectObject import DirectObject
import Errors

def lbp(e = True): 
    return eventObserver("mouse1", e)

def rbp(e = True):
    return eventObserver("mouse3", e)

def lbr(e = True):
    return eventObserver("mouse1-up", e)

def rbr(e = True):
    return eventObserver("mouse3-up", e)

 # These methods handle signals from the GUI
  # Cache keypress events so there's no duplication of key events - not
  # sure this is useful but it can't hurt.  Probably not a good idea to
  # have multiple accepts for the same event.

# This saves event occurances in g.newEvents
def postEvent(ename, val = True):
    print "posting " + ename
    Globals.newEvents[ename] = val

lbutton = Globals.lbutton
rbutton = Globals.rbutton
rbuttonPull = Globals.rbuttonPull
lbuttonPull = Globals.lbuttonPull

def key(kname, val = True):
    kname = checkValidKey(kname)
    return eventObserver(kname, val)

def keyUp(kname, val = True):
    kname = checkValidKey(kname)
    return eventObserver(kname + "-up", val)

def leftClick(model, val = True):
    return getEventSignal(model.d.model.getTag('rpandaid') + "-leftclick", val)

def rightClick(model, val = True):
    return getEventSignal(model.d.model.getTag('rpandaid') + "-rightclick", val)

allKeyNames = ["escape", "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12"]

keyRenamings = {"upArrow": "arrow_up", "downArrow": "arrow_down",
                "leftArrow": "arrow_left", "rightArrow": "arrow_right"}
def checkValidKey(s):
    if s in keyRenamings:
        return keyRenamings[s]
    if type(s) is type("s"):
        if len(s) == 1 or s in allKeyNames:
            return s
    Errors.badKeyName(s)
    
def initEvents():
    directObj = DirectObject()
    directObj.accept("mouse1", lambda: postEvent("mouse1"))
    directObj.accept("mouse1-up", lambda: postEvent("mouse1-up"))
    directObj.accept("mouse3", lambda: postEvent("mouse1"))
    directObj.accept("mouse3-up", lambda: postEvent("mouse1-up"))
    base.buttonThrowers[0].node().setKeystrokeEvent('keystroke')
    directObj.accept("keystroke", lambda v: postEvent(v))
    directObj.accept("f1", lambda : postEvent("f1"))
    directObj.accept("f2", lambda : postEvent("f2"))
    directObj.accept("f3", lambda : postEvent("f3"))
    directObj.accept("f4", lambda : postEvent("f4"))
    directObj.accept("f5", lambda : postEvent("f5"))
    directObj.accept("f6", lambda : postEvent("f6"))
    directObj.accept("f7", lambda : postEvent("f7"))
    directObj.accept("f8", lambda : postEvent("f8"))
    directObj.accept("f9", lambda : postEvent("f9"))
    directObj.accept("f10", lambda : postEvent("f10"))
    directObj.accept("f11", lambda : postEvent("f11"))
    directObj.accept("f12", lambda : postEvent("f12"))
    directObj.accept("escape", lambda : postEvent("escape"))
    directObj.accept("arrow_up", lambda : postEvent("arrow_up"))
    directObj.accept("arrow_down", lambda : postEvent("arrow_down"))
    directObj.accept("arrow_left", lambda : postEvent("arrow_left"))
    directObj.accept("arrow_right", lambda : postEvent("arrow_right"))

    