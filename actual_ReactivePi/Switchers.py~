
from Time import *
from Signal import *
from Types import *

# This is a type used in switching - it polls a signal and either returns a switcher or None if no
# switching occurs.

class When:
  def __init__(self, handle, signal, oneShot, handler, isEvent, sname):
    self.handle = handle
    self.signal = signal
    self.handler = handler
    self.isEvent = isEvent
    self.oneShot = oneShot
    self.sname = sname
  def default(self):
    pass
  def typecheckandinit(self, ctxt):
    if not self.isEvent:
        ty = self.signal.typecheck(boolType)
        if not boolType.implies(ty):
            signalTypeError(self.handle.name, self.sname, boolType, ty)
    self.signal = self.signal.siginit(ctxt)
  def switch(self):
    doit = self.signal.now()
    switched = False
    if self.isEvent:
        if doit is not None:
            switched = True
            self.handler(self.handle, doit)
    else:
        if doit:
            switched = True
            self.handler(self.handle, True)
    if self.oneShot and switched:
        #self.handle.d.switches.remove(self)
        # Remove all one-shots at once
        s1 = []
        for s in self.handle.d.switches:
            if not s.oneShot:
                s1.append(s)
        self.handle.d.switches = s1
    return switched
  def sname():
    return self.handle.name + "." + self.sname
