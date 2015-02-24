from pythonfrp import Proxy
from pythonfrp import Globals
from pythonfrp.Types import *
from pythonfrp import Numerics
from . Color import gray

def updateWorld(self):
    c = self._get("color")
    base.setBackgroundColor(c.r, c.g, c.b) # What is base?


class World(Proxy.Proxy):
    def __init__(self):
        Proxy.Proxy.__init__(self, "world", updateWorld, {"color": colorType, "gravity": p3Type})
        self.color = gray # Set this in panda specific area
        self.gravity = Numerics.p3(0,0,-1)

world = World()

# Clear out the world.  This doesn't reset the global time or camera position.
def resetWorld(continueFn):
    Globals.resetFlag=continueFn
    # Should make all DirectGUI stuff invisible
    print("done")
