import Signal

class StateMachine(Signal):
    def __init__ (self, initState, f):
        Signal.__init__(self, 1000)
        self.init = initState
        self.f = f
        self.alive = True
    def refresh(self):
        if Signal.currentTime > 1:
            self.alive = False
        else:
            self.state = Signal.now(self) 
