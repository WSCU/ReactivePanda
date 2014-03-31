import Globals
from PiEngine import piface
from Proxy import *
from Factory import *


def slapBendix(self): #This is to make everything happy, and bendix is a douche 
    o = self._on.now()
    if o == 0:
        o = 1;
    else:
        o = 0;
    p = self._pin
    piface.digital_write(p, o)
    print str(o)

class Output(Proxy):
    def __init__(self, pin, on, name = 'Light'):
        Proxy.__init__(self, name, lambda x: slapBendix(x))
        self._pin = pin + 1
        if not isinstance(on, Signal):#???
            on = maybeLift(on)
        self.on = on #_setBehavior(_on)
        #self.__dict__['on'] = Lift(self, 'on', boolType)# Not using Types, change to lifted int(0, 1)

def output(*p, **k):
    return Output(*p,**k)

class Input(Observer):
    def __init__(self, pin):
        Observer.__init__(self, lambda: piface.digital_read(pin+1))
        
def input1(*p, **k):
    return Input(*p, **k)
