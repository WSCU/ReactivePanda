import Globals
import piface.pfio as piface
from Proxy import *
from Factory import *

class Output(Proxy):
    def __init__(self, pin, on, name = 'Light'):
        Proxy.__init__(self, name)
        self.__dict__['on'] = Lift(self, 'on', boolType)
        self.d.pin = pin + 1
        if not isinstance(on, Signal):
            on = maybeLift(on)
        self.on = on #_setBehavior(_on)
        
    def refresh(self):
        o = self.on.now()
        if o == 0:
            o = 1;
        else:
            o = 0;
        p = self.d.pin
        piface.digital_write(p, o)

def output(*p, **k):
    return Output(*p,**k)

class Input(Signal):
    def __init__(self, pin):
        self.pin = pin + 1
    def now(self):
        return piface.digital_read(self.pin)
    def typecheck(self, expected):
        return boolType
