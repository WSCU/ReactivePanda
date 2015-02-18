# A reactive menu

from direct.gui.DirectGui import *
import pythonfrp.Factory as Factory
from pythonfrp.Types import checkType, p2Type, numType
from . import PandaGlobals as Globals

# Arguments to the button constructor:
#   text            String        Normal text (required)
#   position        (x,y)         Placement of button (required)
#   size            Size          Defaults to 1
#   name            String        A name used in error message.  Defaults to Buttonx

# Methods / Attributes
#   select - an event that generates a string

def updateMenu(self):
    pass

class Menu:
    def __init__(self, items, position = None, size = 1, name = 'Menu'):
        if position is None:
            pos = (.95, 0, g.nextNE2dY)
            Globals.nextNE2dY = Globals.nextNE2dY - .1
        else:
            checkType(name, "position", position, p2Type)
            pos = (position.x, 0, position.y)
        self._name = name + str(Globals.nextModelId)
        Globals.nextModelId += 1
        self._pandaModel =  DirectOptionMenu(pos = pos,scale=size*0.15,items=items, command=self.setValue)
        self.value = -1
    def getValue(self, e):
        return self.value
    def setValue(self, e):
        self.value = self._pandaModel.selectedIndex

    def addItem(self, string):
        x = self._pandaModel
        tmp_menu = x['items']
        new_item = string
        tmp_menu.insert(-1,new_item) #add the element before add
        x['items'] = tmp_menu

def menu(*p, **d):
    m = Menu(*p, **d)
    return Factory.ObserverF(m.getValue, type = numType)
