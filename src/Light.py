# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from direct.actor import Actor
import direct.directbase.DirectStart
from Engine import *
from Signal import *
from Proxy import *
from Numerics import *
from Color import *
from pandac.PandaModules import *

def updateALight(self):
        c = self._get("color")
        self._ALight.setColor(c.toVBase4())

class ALight(Proxy):
    def __init__(self, color = None, name = 'ambientLight'):
        Proxy.__init__(self, name = name, types = {"color":colorType}, updater = updateALight)
        self._ALight = AmbientLight('alight')
        self._Light = render.attachNewNode(self._ALight)
        render.setLight(self._Light)
        if color is not None:
            self.color = color
        else:
            self.color = white

def ambientLight(color = None):
    return ALight(color = color)
 
def updateDLight(self):
    c = self._get("color")
    self._DLight.setColor(c.toVBase4())
    hprNow = self._get("hpr")
    self._Light.setHpr(degrees(hprNow.h), degrees(hprNow.p), degrees(hprNow.r))

class DLight(Proxy):
    def __init__(self, color = None, hpr = None, name = 'directionalLight'):
        Proxy.__init__(self, name = name, types = {"color":colorType, "hpr":hprType}, updater = updateDLight)
        self._DLight = DirectionalLight("directionalLight")
        self._Light = render.attachNewNode(self._DLight)
        render.setLight(self._Light)
        #need to add parents to lights so that we can attach them to objects
        if color is not None:
            self.color = color
        else:
            self.color = white
        if hpr is not None:
            self.hpr = hpr
        else:
            self.hpr = SHPR(0,0,0)

def updatePLight(self):
    c = self._get("color")
    self._PLight.setColor(c.toVBase4())
    self._Light.setColor(c.toVBase4())
    
class PLight(Proxy):
    def __init__(self, color = None, position = None, name = 'pointLight'):
        Proxy.__init__(self, name = name, types = {"color":(colorType, white), "position":(p3Type, P3(0,0,0))}, updater = updatePLight)
        self._PLight = DirectionalLight("directionalLight")
        self._Light = render.attachNewNode(self._PLight)
        render.setLight(self._Light)
        if color is not None:
            self.color = color
        else:
            self.color = white
        if position is not None:
            self.position = position
        else:
            self.position = SP3(0,0,0)
        
def pointLight(color = None, position = None):
    return PLight(color = color, position = position)

def directionalLight(color = None, hpr = None):
    return DLight(color = color, hpr = hpr)




    





    


