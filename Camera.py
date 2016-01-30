import math
import pythonfrp.Proxy as Proxy
from . import PandaGlobals
from . PandaNumerics import hpr
from pythonfrp.Numerics import p3
from pythonfrp.Types import hprType, p3Type
from pythonfrp.World import world


def updateCamera(self):
    pos = self._get("position")
    hpr = self._get("hpr")
    PandaGlobals.panda3dCamera.setPos(pos.x, pos.y, pos.z)
    PandaGlobals.panda3dCamera.setHpr(math.degrees(hpr.h), math.degrees(hpr.p), math.degrees(hpr.r))

class Camera(Proxy.Proxy):
    def __init__(self):
        Proxy.Proxy.__init__(self, "camera", updateCamera, {"position": p3Type, "hpr": hprType})
        self.position = p3(0, -10, 0)
        self.hpr = hpr(0,0,0)

camera = Camera()