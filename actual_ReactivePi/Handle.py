
import g
from Time import *
from Signal import *
from Numerics import *
from Types import *
from Switchers import *
from copy import copy
from sys import exit
from FRP import localTimeIs

# Every object uses SignalRef objects to hold reactive attributes.  Each of these has
# a slot name and a type.  Since we don't have type inference, you have to declare the
# type of anything that's not built-in.

# Each object keeps track of signals to be sustained and initialized.

def newSignalRef(handle, slot, ty, control = None):
#       print "newSignalRef", slot, handle
       res = SignalRef(slot, handle.name, ty, handle, control)
       handle.d.undefined.append(res)
       handle.d.sustain.append(res)
       return res

# As above, except that the signal has a default value if not provided

def newSignalRefd(handle, slot, ty, dfn, control = None):
       res = newSignalRef(handle, slot, ty, control)
       res.d.default = dfn
       return res

# This is used to declare the type of a signal that's not predefined in the object class
# We need to handle forward reference better - scrap this and allow the type checker
# to do simple unification

def setType(ref, ty):
       if not isinstance(ref,SignalRef):
          print "setType: expecting a signal - " + ref
          exit()
       if ref.d.sigtype == anyType or ref.d.sigtype == ty:
          ref.d.sigtype = ty
       else:
          print "Cant change type of " + ref + " to " + ty
          exit()

# This class handles static data within the object - it's just used as a container.
# This always lives in the "d" field of the object.

class HandleData:
    pass

# This is a reactive object (model, light, photo, world, ...).  All of these classes are
# subclasses of this.  At this level we handle reactivity and initialization.
# Users can define arbitrary signals within any of these objects - this is a logical place
# to place local signals.

class Handle:
    # Create a new signal ref and mark it for initialization
    def __init__(self, name = 'unnamed handle', isWorld = False, duration = 0):
        d = HandleData()
        self.__dict__['d'] = d
        d.undefined = []    # Things that need to be initialized
        d.sustain = []      # Make sure everything gets evaluated
        d.switches = []     # switchers for this object
        d.newswitches = []  # newly generated switchers - don't look at these at time of switch
        d.isWorld = isWorld # Need to mark the world object
        d.statics = {}
        d.collections = []
        d.initialized = False
        d.zombie = False
        if isWorld:
             self.__dict__['name'] = 'world'
        else:
             self.__dict__['name'] = uniqueName(name)    # uniquify all names
        # Add this to the list of objects currently in the world
        g.newModels.append(self)
        if duration != 0:
            self.react1(localTimeIs(duration), lambda m, v: m.exit())

    def str(self):
        return self.name
    def showModel(self):  # By default, a handle isn't visible
        pass
    # Allows assignment to the signals.  Expand this to allow local signals.
    # Here are the possibilities:
    #  1.  Slot doesn't exist: create it (can't tell what type it will have!)
    #  2.  Slot exists (has a SignalRef) and the SignalRef is uninitialized:
    #      call setBehavior on the slot
    #  3.  Slot exists and the SignalRef is initialized:
    #      If the slot is in the uninitialized list, multiple definition error
    #      Otherwise, override the old definition.  Note that you can preserve
    #      the type of the old signal.
  
    def __setattr__(self, x, y):
        if getPType(y) is StaticType:
            self.d.statics[x] = y.v
            return
        if x in self.d.statics:
            self.d.statics[x] = y
            return
        oldval = getattr(self,x,None)
        if oldval is None:
           ref = newSignalRef(self, x, anyType)
           self.__dict__[x] = ref
           ref.setBehavior(maybeLift(y))
        elif not isinstance(oldval, SignalRef):
           slotInUse(self.name, x)
        elif undefinedRef(oldval):
            oldval.setBehavior(maybeLift(y))
        elif containsRef(self.d.undefined, oldval):
            multipleDef(self, x)
        else:
#            print "Overriding old " + oldval.sname()
            # Overwrite the old ref here ...
            oldval.signal = maybeLift(y)
            self.d.undefined.append(oldval)

    def __getattr__(self, slot):
       if slot in self.d.statics:
           return self.d.statics[slot]
       if slot in self.__dict__:
           return self.__dict__[slot]
       # References to previously undefined signals create a new signal (no type is known though)
       ref = newSignalRef(self, slot, anyType)
       self.__dict__[slot] = ref
       return ref

    # This is the main entry to the model update.
    # This should be called from the refresh in each object that inherits Handle
    # This just handles sustainment (making sure all signals get evaluated at every time step)
    def refresh(self):
#        print "Refreshing " + self.name
        # Avoid time leaks by looping through all attributes here and evaling.
        for sig in self.d.sustain:
#          print "Signal " + sig.sname()
          sig.now()  #  Now all sustained signals to avoid time leaks
    def __repr__(self):
        return self.__dict__['name']
    # Any object that isn't in the "models" list needs to override this.
    def exit(self):
        removeModel(self)
        if self.d.model is not None:
            self.d.model.detachNode()
        for c in self.d.collections:
            c.remove(self)
        self.d.zombie = True


    # This is called at initialization time.  We will also need to call this
    # after a switching event.

    def checkSignals(self, ctxt):
        self.d.initialized = True
#        print "Checking signals", self.__dict__['name']

        # Probably not needed!  This is an initialization hook
        self.showModel()                 # Attach to "render"
        for obj in self.d.undefined:
#              print "Initializing ",obj.d.slot
             obj.default()               #  Apply a default value to undefined signals
             obj.typecheckandinit(ctxt)  #  Causes signal initialization

# Switching stuff
    # This is called at each clock.  Go through all switchers and determine if
    # it is time to switch.  These switchers are not in any order and it shouldn't
    # matter what order they fire in
    def switch(self):
       # Do a copy in case switches are deleted (the "when1" switcher)
       if len(self.d.switches) > 0:
           print self.name + str(len(self.d.switches))
       for switcher in copy(self.d.switches):
          if switcher.switch():
              g.switched = True  # Avoid looking for signals to initialize if no
                                 # switch has fired

    # Switch when a boolean becomes true, remove the switch after firing
    # handle, signal, oneShot, handler, isEvent, sname:
    def when1(self, condition, handler):
       switcher = When(self, condition, True, handler, False, "when1")
       self.d.newswitches.append(switcher)
       self.d.undefined.append(switcher)

    def when(self, condition, handler):
       switcher = When(self, condition, False, handler, False, "when")
       self.d.newswitches.append(switcher)
       self.d.undefined.append(switcher)

    def react(self, condition, handler):
       switcher = When(self, condition, False, handler, True, "react")
       self.d.newswitches.append(switcher)
       self.d.undefined.append(switcher)

    def react1(self, condition, handler):
       switcher = When(self, condition, True, handler, True, "react1")
       self.d.newswitches.append(switcher)
       self.d.undefined.append(switcher)

    def resetReactions(self):
       self.d.switches = []

def removeModel(model):
        models = g.models
#        print "Exiting ", self.__dict__['name'], models
        newModels = []
        for m in models:
            if m is not model:
                newModels.append(m)
        g.models = newModels
