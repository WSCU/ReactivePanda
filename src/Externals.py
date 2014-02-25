import Globals
from Factory import *
from Signal import *

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
