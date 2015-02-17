import math
import pythonfrp.Proxy as Proxy
from . import PandaGlobals
from . Numerics import hpr
from pythonfrp.Numerics import p3
from pythonfrp.Types import hprType, p3Type


def updateCamera(self):
    pos = self._get("position")
    hpr = self._get("hpr")
    panda3dCamera.setPos(pos.x, pos.y, pos.z)
    panda3dCamera.setHpr(math.degrees(hpr.h), math.degrees(hpr.p), math.degrees(hpr.r))


class Camera(Proxy.Proxy):
    def __init__(self):
        Proxy.Proxy.__init__(self, "camera", updateCamera, {"position": p3Type, "hpr": hprType})
        self.position = p3(0, -10, 0)
        self.hpr = hpr(0,0,0)


camera = Camera()
panda3dCamera = camera
