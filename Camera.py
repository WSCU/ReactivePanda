import math

import pythonfrp.Proxy
from . import Globals
import pythonfrp.Numerics as Numerics
from pythonfrp.Types import hprType, p3Type


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


camera = Camera()
