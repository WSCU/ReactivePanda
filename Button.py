

# A reactive button

from pythonfrp.Types import *
from direct.gui.DirectGui import DirectButton
import pythonfrp.StaticNumerics as StaticNumerics
import pythonfrp.Factory as Factory
from . import Externals
from . import Globals

# Arguments to the button constructor:
#   text            String        Normal text (required)
#   position        (x,y)         Placement of button (required)
#   size           Size          Defaults to 0.15
#   name            String        A name used in error message.  Defaults to Buttonx

# Methods / Attributes
#   click - an event that generates a

class Button:
    def __init__(self, text, position = None, size = 1, name = 'Button', e = True):
        if position is None:
            position = StaticNumerics.SP2(-.95, Globals.nextNW2dY)
            Globals.nextNW2dY = Globals.nextNW2dY -.1
        self._name = name + str(Globals.nextModelId)
        Globals.nextModelId += 1
        self._click = Factory.eventObserver(self._name, e)
        self._pandaModel = DirectButton(text = text, pos = (position.x, 0, position.y), scale = size*0.1, command = lambda: Externals.postEvent(self._name))

def updateButton(self):
       pass

def button(*p, **k):
    return Button(*p, **k)._click
