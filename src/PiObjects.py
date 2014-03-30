import Globals
import piface.pfio as piface
from Proxy import *
from Factory import *


def slapBendix(): #This is to make everything happy, and bendix is a douche.
    pass

class Output(Proxy):
    def __init__(self, pin, on, name = 'Light'):
        Proxy.__init__(self, name, slapBendix)
        #self.__dict__['on'] = Lift(self, 'on', boolType)# Not using Types, change to lifted int(0, 1)
        self._pin = pin + 1
        if not isinstance(on, Signal):#???
            on = maybeLift(on)
        self._on = on #_setBehavior(_on)
        
    def refresh(self):
        o = self.on.now()
        if o == 0:
            o = 1;
        else:
            o = 0;
        p = self._pin
        piface.digital_write(p, o)

def output(*p, **k):
    return Output(*p,**k)

class Input(Observer):
    def __init__(self, pin):
        Observer.__init__(self, piface.digital_write(pin+1)
        
def input1(*p, **k):
    return Input(*p, **k)
