from pythonfrp import Proxy
from pythonfrp import Globals
from pythonfrp.Types import *
from pythonfrp import Numerics
from . Color import gray

def updateColor(self):
    c = self._get("color")
    base.setBackgroundColor(c.r, c.g, c.b) # What is base?


#class World(Proxy.Proxy):
#    def __init__(self):
#        Proxy.Proxy.__init__(self, "world", updateWorld, {"color": colorType, "gravity": p3Type})
#        self.color = gray # Set this in panda specific area
#        self.gravity = Numerics.p3(0,0,-1)
        
#world = World()
pWorld = World.world

pWorld.addSignal("color",gray,colorType,updateColor)
pWorld.addSignal("gravity",Numerics.p3(0,0,-1),p3Type,lambda: None)

def resetWorld(continueFn = lambda: None):
    Globals.resetFlag=continueFn
    # Should make all DirectGUI stuff invisible

