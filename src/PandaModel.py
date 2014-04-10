
# This defines an object that appears on the screen whose representation is obtained from a
# 3-D model in an egg file from the Panda-3D engine.  These have the following reactive parameters:
#   position  P3      location in 3-space
#   hpr       HPR     orientation in 3-space
#   scale     scalar  relative size (1 = unit cube)
#   color     Color   dynamic texture (None = model skin, otherwise = color of object)

from direct.actor import Actor
import direct.directbase.DirectStart
from panda3d.core import Filename
from Engine import *
from Signal import *
from Proxy import *
from Numerics import *
from StaticNumerics import pi
import Globals
import FileIO
import FileSearch

# This fills in all of the defaults
parameterCache = {}
pandaParameters = { "localSize" : 0.05,
                    "localPosition" : P3( 0, 200, 0).start(),
                    "localOrientation" : HPR(0, 0, 0).start()}
def pandaModel(fileName = None, size = None, hpr = None, position = None):
    res = PandaModel(  fileName, size, hpr, position)
    return res
class PandaModel(Proxy):
    def __init__(self, fileName, size, hpr, position):
        Proxy.__init__(self, name = "Panda"+str(Globals.nextModelId), updater = updater)
        #mFile = fileSearch(fileName, "models",["egg"])
        self._mFile = Filename("/c/Panda3D-1.8.1/models/panda-model.egg.pz")
        #print "File Path: " + repr(mFile)
        self._pandaModel = loader.loadModel(self._mFile)
        Globals.nextModelId = Globals.nextModelId + 1
        self._onScreen = False
        """
        self.position = lift('position',P3(0,0,0))
        self.hpr = lift('hpr' ,HPR(0,0,0))
        self.size = lift('size', 0.05)
        """
        self._size=pandaParameters['localSize']
        self._hpr=pandaParameters['localOrientation']
        self._position=pandaParameters['localPosition']
        self.size = Lift0F(1)
        self.position = P3(1,1,1)
        
        if position is not None:
            self.position = position
        if hpr is not None:
            self.hpr = hpr
        if size is not None:
            self.size =size
        showModel(self)#This call needs to move into the updater method. We don't have it working with the engine yet.

def updater(self):
    """
    self._pandaModel.setScale(self.get("scale"))
    self._pandaModel.setHpr(self.get("hpr"))
    self._pandaModel.setPos(self.get("position"))"""

    p = self.position.now()
    p2 = self._position.now()
    s = self.size.now()
    h = self.hpr.now()
    self._pandaModel.setScale(s*self._size)
    self._pandaModel.setPos(p.x + p2.x*s,
                            p.y + p2.y*s,
                            p.z + p2.z*s)
                            
    d = self.hpr.now()
    d2 = self._hpr.now()
    self._pandaModel.setHpr(degrees(d.h + d2.h),
                            degrees(d.p + d2.p),
                            degrees(d.r + d2.r))
  
def degrees( v):
    return v*(180/pi)
def showModel(self):
    if not self._onScreen:
           self._pandaModel.reparentTo(render)
           self._onScreen = True