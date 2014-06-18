import Proxy
import Globals as g
from Proxy import Proxy
import Numerics
from Types import *
from StaticNumerics import *
from Color import gray

def updateWorld(self):
    c = self._get("color")
    base.setBackgroundColor(c.r, c.g, c.b)

def updateCamera(self):
    pos = self._get("position")
    hpr = self._get("hpr")
    g.panda3dCamera.setPos(pos.x, pos.y, pos.z)
    g.panda3dCamera.setHpr(Numerics.degrees(hpr.h), Numerics.degrees(hpr.p), Numerics.degrees(hpr.r))

class Camera(Proxy):

    def __init__(self):
        Proxy.__init__(self, "camera", updateCamera, {"position": p3Type, "hpr": hprType})
        self.position = Numerics.p3(0, -10, 0)
        self.hpr = Numerics.hpr(0,0,0)

class World(Proxy):

    def __init__(self):
        Proxy.__init__(self, "world", updateWorld, {"color": colorType, "gravity": p3Type})
        self.gravity = Numerics.P3(0,0,-1)
        self.color = gray

world = World()
camera = Camera()