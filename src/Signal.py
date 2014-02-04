class FsSignal:
    def __init__ (self, x):
        self.x = x
        self.startTime = Engine.globalTime
    def now(self):
        pass
    def state(self, time):
        pass
    def start(self):
        pass

class Lift0:
    def __init__(self, v):
        self.now = v
    def start(self):
        return self
    def refresh(self, dt):
        pass
