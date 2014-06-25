import Proxy
import Globals
import math
import Functions
from Types import *
from StaticNumerics import *
from Color import gray
import Numerics

def updateWorld(self):
    c = self._get("color")
    base.setBackgroundColor(c.r, c.g, c.b)

def updateCamera(self):
    pos = self._get("position")
    hpr = self._get("hpr")
    Globals.panda3dCamera.setPos(pos.x, pos.y, pos.z)
    Globals.panda3dCamera.setHpr(math.degrees(hpr.h), math.degrees(hpr.p), math.degrees(hpr.r))

class Camera(Proxy.Proxy):

    def __init__(self):
        Proxy.Proxy.__init__(self, "camera", updateCamera, {"position": p3Type, "hpr": hprType})
        self.position = Numerics.p3(0, -10, 0)
        self.hpr = Numerics.hpr(0,0,0)

class World(Proxy.Proxy):

    def __init__(self):
        Proxy.Proxy.__init__(self, "world", updateWorld, {"color": colorType, "gravity": p3Type})
        self.color = gray
        self.gravity = Numerics.p3(-1,0,0)

world = World()
camera = Camera()
# Clear out the world.  This doesn't reset the global time or camera position.
def resetWorld(continueFn):
    Globals.resetFlag=continueFn
    # Should make all DirectGUI stuff invisible
    print "done"