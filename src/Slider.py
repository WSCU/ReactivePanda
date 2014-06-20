
from direct.gui.DirectGui import *

import Globals
from Factory import *
from Types import *


def slider(size=1, position=None, min=0, max=1, pageSize=None, init=None, name='Slider', label=None):
    checkType(name, "min", min, numType)
    checkType(name, "max", max, numType)
    if init is None:
        init = min
    if pageSize is None:
        pageSize = (max - min) / 100
        '''
        t = getPType(size)
        if t != numType:
            argTypeError(self.name, t, numType, 'size')
        t = getPType(min)
        if t != numType:
            argTypeError(self.name, t, numType, 'min')
        t = getPType(max)
        if t != numType:
            argTypeError(self.name, t, numType, 'max')
        t = getPType(pageSize)
        if t != numType:
            argTypeError(self.name, t, numType, 'pageSize')
        t = getPType(init)
        if t != numType:
            argTypeError(self.name, t, numType, 'init')
            '''
    if position is None:
        pos = (.95, 0, Globals.nextNE2dY)
        Globals.nextNE2dY = Globals.nextNE2dY - .1
    else:
            #t = getPType(position)
            #if t != P2Type:
            #    argTypeError(self.name, t, P2Type, 'position')
        pos = (position.x, 0, position.y)
    val = [init]
    slider = [0]
    def cmd():
        val[0] = slider[0]['value']
    slider[0] = DirectSlider(scale=.2 * size, pos=pos, range=(min, max), pageSize=pageSize, value=init, command=cmd)
    observer = ObserverF(lambda x: val[0], type = numType)
    return observer
        #if label is not None:
        #    text(text = label, position = SP2(pos[0]-.3, pos[2]))
'''
    def set(self, val):
        self.d.model['value'] = val

    def setSlider(self):
        self.d.svalue = self.d.model['value']
'''
# Slider utilities
'''
def sliderHPR(init = None, label = ""):
    h = slider(max = 2*pi, label = label + "-h")
    p = slider(max = 2*pi, label = label + "-p")
    r = slider(max = 2*pi, label = label + "-r")
    return HPR(h, p, r)

sliderHpr = sliderHPR

# The init can be either a scalar or a P3.  The same should be done for min and max but I'm lazy.
def sliderP3(min = 0, max = 1, init = 0, label = "P3"):
    if (getPType(init) == P3Type):
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
    return P3(x, y, z)

# The init can be either a scalar or a P3.  The same should be done for min and max but I'm lazy.
def sliderColor(init = black, label = "Color"):
    r = slider(min = 0, max = 1, init = init.r, label = label + "-r")
    g = slider(min = 0, max = 1, init = init.g, label = label + "-g")
    b = slider(min = 0, max = 1, init = init.b, label = label + "-b")
    a = slider(min = 0, max = 1, init = init.a, label = label + "-a")
    return colora(r, g, b, a)
'''