from Proxy import Proxy
from Numerics import P3

def upd(self): pass

class World(Proxy):

    def __init__(self):
        Proxy.__init__(self, "world", upd, {})
        self.gravity = P3(0,0,-1)
