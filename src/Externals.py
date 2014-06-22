
import Globals
from Factory import *
from Signal import *
import StaticNumerics
from direct.actor import Actor
import Errors
import Functions
import Click

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
    #print "posting " + ename
    Globals.newEvents[ename] = val



def key(kname, val = True):
    kname = checkValidKey(kname)
    return getEventSignal(kname, val)

def keyUp(kname, val = True):
    kname = checkValidKey(kname)
    return getEventSignal(kname + "-up", val)

def leftClick(model, val = True):
    return getEventSignal(model._pandaModel.getTag('rpandaid') + "-leftclick", val)

def rightClick(model, val = True):
    return getEventSignal(model._pandaModel.getTag('rpandaid') + "-rightclick", val)

allKeyNames = ["escape", "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12", "space"]

keyRenamings = {"upArrow": "arrow_up", "downArrow": "arrow_down",
                "leftArrow": "arrow_left", "rightArrow": "arrow_right"}
def checkValidKey(s):
    if s in keyRenamings:
        return keyRenamings[s]
    if type(s) is type("s"):
        if len(s) == 1 or s in allKeyNames:
            return s
    Errors.badKeyName(s)

  # These methods handle signals from the GUI
  # Cache keypress events so there's no duplication of key events - not
  # sure this is useful but it can't hurt.  Probably not a good idea to
  # have multiple accepts for the same event.


def getEventSignal(ename, val):
        if Globals.eventSignals.has_key(ename):
            return tag(val, Globals.eventSignals[ename])
        e = eventObserver(ename)
        Globals.eventSignals[ename] = e
        Globals.direct.accept(ename, lambda: postEvent(ename))
        return Functions.tag(val, e)


def initEvents():
    base.disableMouse() 
    directObj = Globals.direct
    directObj.accept("mouse1", lambda: postEvent("mouse1"))
    directObj.accept("mouse3", lambda: postEvent("mouse3"))
    directObj.accept("mouse1-up", lambda: postEvent("mouse1-up"))
    directObj.accept("mouse3-up", lambda: postEvent("mouse3-up"))
    Globals.mousePos = None
    Globals.lbutton = False
    Globals.rbutton = False
    Globals.lbuttonPull = StaticNumerics.SP2(0,0)
    Globals.rbuttonPull = StaticNumerics.SP2(0,0)

def pollGUI():
    if base.mouseWatcherNode.hasMouse():
       lbp = Globals.events.has_key("mouse1")
       rbp = Globals.events.has_key("mouse3")
       lbr = Globals.events.has_key("mouse1-up")
       rbr = Globals.events.has_key("mouse3-up")
       if lbp:
           Globals.lbutton = True
       if rbp:
           Globals.rbutton = True
       if lbr:
           Globals.lbutton = False
       if rbr:
           Globals.rbutton = False
       mpos = base.mouseWatcherNode.getMouse() #get the mouse position in Panda3D form
       lastMousePos = Globals.mousePos
       Globals.mousePos = StaticNumerics.SP2(mpos.getX(), mpos.getY())
       if Globals.lbutton and lastMousePos is not None:
               Globals.lbuttonPull = Globals.lbuttonPull + Globals.mousePos - lastMousePos
       if Globals.rbutton and lastMousePos is not None:
               Globals.rbuttonPull = Globals.rbuttonPull + Globals.mousePos - lastMousePos
       # If a left / right mouse click has happened, ask Panda which model was clicked on.  Post an event
       # if there is a model where the mouse clicked
       if lbp or rbp:
           m = Click.findClickedModels()
           if m is not None:
               if Globals.events.has_key("mouse1"):
                    Globals.events[m + "-leftclick"] = True
               else:
                    Globals.events[m + "-rightclick"] = True

mouse = ObserverF(lambda x: Globals.mousePos)

lbutton = ObserverF(lambda x: Globals.lbutton)
rbutton = ObserverF(lambda x: Globals.rbutton)
rbuttonPull = ObserverF(lambda x:Globals.rbuttonPull)
lbuttonPull = ObserverF(lambda x:Globals.lbuttonPull)
