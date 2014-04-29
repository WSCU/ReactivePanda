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

class ALight(Proxy):
    def __init__(self, color = None, name = 'ambientLight'):
        Proxy.__init__(self, name = name, types = {"color":colorType}, updater = updater)
        if color is None:
            self.color = white
        else:
            self.color = color
        self._onScreen = False
        self._Light = AmbientLight('alight')
        showModel(self)

def updater(self):
        c = self.get("color")
        self._Light.setColor(c.toVBase4())
        
def ambientLight(color):
    return ALight(color)

def showModel(self):
    if not self._onScreen:
           self._onScreen = True
        
class DLight(Proxy):
    def __init__(self, color = None, hpr = None, name = 'directionalLight'):
        Proxy.__init__(self, name = name, types = {"color":colorType}, updater = updater)
        if color is None:
            self.color = white
        else:
            self.color = color
        if hpr is None: 
            hpr = HPR(0,0,0)
        else: 
            hpr = hpr
        self._onScreen = False
        showModel(self)
    def updater(self):
        c = self.get("color")
        self._Light.setColor(c.toVBase4())
        positionNow = self.get("position")
        hprNow = self.get("hpr")

def directionalLight(color = None, hpr = None):
    if color is None:
        return DLight(hpr)
    else: 
        return DLight(color)


    


