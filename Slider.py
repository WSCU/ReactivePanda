from direct.gui.DirectGui import *
from . import PandaGlobals
from pythonfrp.Factory import *
from pythonfrp.Types import *
from . import Text
from pythonfrp.StaticNumerics import SP2
from pythonfrp.Numerics import *
from . Color import *

class Slider:
    def __init__(self, size, position, min, max, pageSize, init, label):
        name = "slider" + str(PandaGlobals.nextModelId)
        checkType(name, "min", min, numType)
        checkType(name, "max", max, numType)
        if init is not None:
            checkType(name, "init", init, numType)
        else:
            init = min
        if pageSize is None:
            pageSize = (max - min) / 100
        if position is None:
            pos = (.95, 0, PandaGlobals.nextNE2dY)
            PandaGlobals.nextNE2dY = PandaGlobals.nextNE2dY - .1
        else:
            pos = (position.x, 0, position.y)
        if label is not None:
            Text.text(text = label, position = SP2(pos[0]-.3, pos[2]))
        self._name = name
        self._pandaModel = DirectSlider(scale=.2 * size, pos=pos, range=(min, max), pageSize=pageSize, value=init, command=self.setValue)
        self.value = init
    def getValue(self, x):
        return self.value
    def setValue(self):
        self.value = self._pandaModel["value"]


def slider(size=1, position=None, min=0, max=1, pageSize=None, init=None, name='Slider', label=None):
    r = Slider(size, position, min, max, pageSize, init, label)
    return ObserverF(r.getValue, type = numType)

def sliderHPR(init = None, label = ""):
    h = slider(max = 2*pi, label = label + "-h")
    p = slider(max = 2*pi, label = label + "-p")
    r = slider(max = 2*pi, label = label + "-r")
    return HPR(h, p, r)

sliderHpr = sliderHPR

# The init can be either a scalar or a P3.  The same should be done for min and max but I'm lazy.
def sliderP3(min = 0, max = 1, init = 0, label = "P3"):
    if (getPtype(init) is p3Type):
        initx = getX(init)
        inity = getY(init)
        initz = getZ(init)
    else:
        initx = init
        inity = init
        initz = init
    x = slider(min = min, max = max, init = initx, label = label + "-x")
    y = slider(min = min, max = max, init = inity, label = label + "-y")
    z = slider(min = min, max = max, init = initz, label = label + "-z")
    return p3(x, y, z)

# The init can be either a scalar or a P3.  The same should be done for min and max but I'm lazy.
def sliderColor(init = black, label = "Color"):
    r = slider(min = 0, max = 1, init = init.r, label = label + "-r")
    g = slider(min = 0, max = 1, init = init.g, label = label + "-g")
    b = slider(min = 0, max = 1, init = init.b, label = label + "-b")
    a = slider(min = 0, max = 1, init = init.a, label = label + "-a")
    return colora(r, g, b, a)
