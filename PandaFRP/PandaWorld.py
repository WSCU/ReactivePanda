from pythonfrp import Globals
from pythonfrp.Types import *
from pythonfrp import Numerics
from pythonfrp import World
from PandaColor import gray


def updateColor(self):
    c = self._get("color")
    base.setBackgroundColor(c.r, c.g, c.b)  # What is base?


world = World.world
# This is confusing, and maybe needs to be changed: World.world is
# an instance of the World class inside the World module
# World.addSignal is inside the World module, bvt not the World class. world, defined here, is a pointer for the rest
# of the engine. Should we re-name this? There are a lot of worlds, and it took me a while to figure them out.

World.addSignal("color", gray, colorType, updateColor)
World.addSignal("gravity", Numerics.p3(0, 0, -1), p3Type, lambda x: None)


def resetWorld():
    World.resetWorld()
    # Should we export this through engine somehow?
