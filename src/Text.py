import Globals
from Proxy import *
import colorsys
from direct.gui.OnscreenText import OnscreenText
from Types import * 
from StaticNumerics import SP2
from Numerics import P2
from direct.gui.DirectGui import *
from Externals import postEvent
from Signal import var
from Factory import maybeLift
class TextBox(Proxy): #Creates the text box object that users can enter in values to
    def __init__(self, position2D = None, size = 1, name = 'TextBox', width = 15): #Textbox is not working and not used right now
        Proxy.__init__(self, name = name, updater=updater)
        self.size = maybeLift(size)
        self.width = maybeLift(width)
        if position2D is None:
            position2D = P2(.95, Globals.nextNE2dY)
            Globals.nextNE2dY = Globals.nextNE2dY - .1
        self.text = var("")
        self.enter = eventObserver("enter")
    
def updater(self):
    p1 = self.get("position2D")
    s = self.get("size")
    w = self.get("width")
    self._textBox =  DirectEntry(pos = (p1.x,0,p1.y),scale=s*0.05, command=lambda v:textBoxChange(v,self), width = w)

    
def textBoxChange(v, self):
    postEvent(self.name, v)
    self.text.set(v)

def textBox(*p, **k):
    return TextBox(*p, **k).enter

class Text(Proxy):
    def __init__(self, text = None, name = 'Text', position = None, size = 1, color = None):
        Proxy.__init__(self, name, updater=textUpdater, types = {"position": p2Type, "hpr": hprType, "size": numType})
        
        # This allows the text in the initializer to be reactive.  Not sure why other
        # constructors don't do this.
        self.size = maybeLift(size)
        if text is not None:
            self.text = maybeLift(text)
        else: 
            self.text = maybeLift("No current text")
        if position is not None:
            self.position = maybeLift(position)
        else:
            self.position = P2(-.95, Globals.nextNW2dY)
            Globals.nextNW2dY = Globals.nextNW2dY -.1
        # This code looks OK - we should be able to make the position reactive
        #else:
            #t = getPtype(position)
            #if t != P2Type:
            #    argTypeError(self.name, t, P2Type, 'position')

        #self._text = OnscreenText(pos = (position.x, position.y), scale = size*0.05, fg = color.toVBase4(), mayChange = True)


def textUpdater(self):
    p1 = self.get("position2D")
    s = self.get("size")
    self._text = OnscreenText(pos = (p1.x, p1.y), scale = s*0.05, mayChange = True)
    self._text.setText(str(self.get("text")))

def text(*p, **k):
    return Text(*p, **k)