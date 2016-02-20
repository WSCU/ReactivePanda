import pythonfrp.Functions as Functions
import pythonfrp.Globals
import pythonfrp.StaticNumerics as StaticNumerics
from PandaFRP import PandaGlobals
from PandaSRC import Click
from pythonfrp.Factory import *
from pythonfrp.Types import *


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
    pythonfrp.Globals.newEvents[ename] = val



def key(kname, val = True):
    kname = checkValidKey(kname)
    return getEventSignal(kname, val)

def keyUp(kname, val = True):
    kname = checkValidKey(kname)
    return getEventSignal(kname + "-up", val)

def leftClick(model, val = True):
    val = model._alive
    return getEventSignal(model._pandaModel.getTag('rpandaid') + "-leftclick", val)

def rightClick(model, val = True):
    val = model._alive
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
        if pythonfrp.Globals.eventSignals.has_key(ename):
            return Functions.tag(val, pythonfrp.Globals.eventSignals[ename])
        e = eventObserver(ename)
        pythonfrp.Globals.eventSignals[ename] = e
        PandaGlobals.direct.accept(ename, lambda: postEvent(ename))
        return Functions.tag(val, e)


def initEvents():
    base.disableMouse()
    directObj = PandaGlobals.direct
    directObj.accept("mouse1", lambda: postEvent("mouse1"))
    directObj.accept("mouse3", lambda: postEvent("mouse3"))
    directObj.accept("mouse1-up", lambda: postEvent("mouse1-up"))
    directObj.accept("mouse3-up", lambda: postEvent("mouse3-up"))
    PandaGlobals.mousePos = StaticNumerics.SP2(0, 0)
    PandaGlobals.lbutton = False
    PandaGlobals.rbutton = False
    PandaGlobals.lbuttonPull = StaticNumerics.SP2(0, 0)
    PandaGlobals.rbuttonPull = StaticNumerics.SP2(0, 0)


def pollGUI():
    if base.mouseWatcherNode.hasMouse():
       lbp = pythonfrp.Globals.events.has_key("mouse1")
       rbp = pythonfrp.Globals.events.has_key("mouse3")
       lbr = pythonfrp.Globals.events.has_key("mouse1-up")
       rbr = pythonfrp.Globals.events.has_key("mouse3-up")
       if lbp:
           PandaGlobals.lbutton = True
       if rbp:
           PandaGlobals.rbutton = True
       if lbr:
           PandaGlobals.lbutton = False
       if rbr:
           PandaGlobals.rbutton = False
       mpos = base.mouseWatcherNode.getMouse() #get the mouse position in Panda3D form
       lastMousePos = PandaGlobals.mousePos
       PandaGlobals.mousePos = StaticNumerics.SP2(mpos.getX(), mpos.getY())
       if PandaGlobals.lbutton and lastMousePos is not None:
               PandaGlobals.lbuttonPull = PandaGlobals.lbuttonPull + PandaGlobals.mousePos - lastMousePos
       if PandaGlobals.rbutton and lastMousePos is not None:
               PandaGlobals.rbuttonPull = PandaGlobals.rbuttonPull + PandaGlobals.mousePos - lastMousePos
       # If a left / right mouse click has happened, ask Panda which model was clicked on.  Post an event
       # if there is a model where the mouse clicked
       if lbp or rbp:
           m = Click.findClickedModels()
           if m is not None:
               if pythonfrp.Globals.events.has_key("mouse1"):
                    pythonfrp.Globals.events[m + "-leftclick"] = True
               else:
                    pythonfrp.Globals.events[m + "-rightclick"] = True

mouse = ObserverF(lambda x: PandaGlobals.mousePos)

lbutton = ObserverF(lambda x: PandaGlobals.lbutton, boolType)
rbutton = ObserverF(lambda x: PandaGlobals.rbutton, boolType)
rbuttonPull = ObserverF(lambda x: PandaGlobals.rbuttonPull, p2Type)
lbuttonPull = ObserverF(lambda x: PandaGlobals.lbuttonPull, p2Type)
