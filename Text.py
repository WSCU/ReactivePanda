from . import PandaGlobals
from pythonfrp.Proxy import *
from direct.gui.OnscreenText import OnscreenText
from pythonfrp.Types import *
import StaticNumerics
from direct.gui.DirectGui import *
from . Externals import postEvent
from pythonfrp.Factory import maybeLift
from . Color import yellow

class TextBox(Proxy): #Creates the text box object that users can enter in values to
    def __init__(self, position = None, size = 1, name = 'TextBox', width = 15):
        Proxy.__init__(self, name = name, updater=textboxUpdater, types = {"position":p2Type, "size": numType, "name":stringType, "width":numType})
        checkType(self, "size", size, numType)
        checkType(self, "width", width, numType)
        self.size = maybeLift(size)
        self.width = maybeLift(width)
        if position is None:
            position = StaticNumerics.SP2(.95, PandaGlobals.nextNE2dY)
            PandaGlobals.nextNE2dY = PandaGlobals.nextNE2dY - .1
        self.text = var("")
        self.enter = eventObserver("enter")

def textboxUpdater(self):
    p1 = self.get("position")
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
        Proxy.__init__(self, name, updater=textUpdater, types = {"text": anyType, "color": colorType})
        if text is None:
            self.text = ""
        else:
            self.text = text
        if color is None:
            self.color = yellow
        else:
            self.color = color
        if position is None:
            position = StaticNumerics.SP2(-.95, PandaGlobals.nextNW2dY)
            PandaGlobals.nextNW2dY = PandaGlobals.nextNW2dY -.1
        self._textObject = OnscreenText(pos = (position.x, position.y), scale = size*0.05, mayChange = True)
        #self._text = OnscreenText(pos = (position.x, position.y), scale = size*0.05, fg = color.toVBase4(), mayChange = True)


def textUpdater(self):
    text = self._get("text")
    color = self._get("color")
    self._textObject.setText(str(text))
    self._textObject.setFg(color.toVBase4())

def text(*p, **k):
    return Text(*p, **k)
