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
class TextBox(Proxy): #Creates the text box object and updates the reactive text which will appear on screen
    def __init__(self, position = None, size = 1, name = 'TextBox', width = 15):
        Proxy.__init__(self, name = name, updater=updater)
        if position is None:
            position = P2(.95, g.nextNE2dY)
            g.nextNE2dY = g.nextNE2dY - .1
        self._textBox =  DirectEntry(pos = (position.x,0,position.y),scale=size*0.05, command=lambda v:textBoxChange(v,self), width = width)
        """self.__dict__['text'] = var("")
        self.__dict__['enter'] = EventMonitor(self.name)"""
    
def updater(self):
    pass
    
def textBoxChange(v, self):
    postEvent(self.name, v)
    self.__dict__['text'].set(v)

def textBox(*p, **k):
    return TextBox(*p, **k).enter

class Text(Proxy):
    def __init__(self, text = None, name = 'Text', position2D = None, size = 1, color = None):
        Proxy.__init__(self, name, updater=textUpdater)
        
        # This allows the text in the initializer to be reactive.  Not sure why other
        # constructors don't do this.
        self.size = maybeLift(size)
        if text is not None:
            self.text = maybeLift(text)
        else: 
            self.text = maybeLift("No current text")
        if position2D is None:
            self.position2D = P2(-.95, Globals.nextNW2dY)
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