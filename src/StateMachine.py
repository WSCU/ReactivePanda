import Signal

class StateMachine:
    def __init__ (self, initState, f, s, initV):
        #Signal.__init__(self, 1000)
        self.state = initState
        self.f = f
        self.s = s
        print repr(s)
        self.now = initV
    def refresh(self, dt):
        self.s.refresh(dt)
        s, output = self.f(self.s.now, self.state, dt) 
        self.state = s
        self.now = output
        #print "refresh state machine"

class StateMachineF:
    def __init__ (self, initState, f, s, initV):
        self.state = initState
        self.f = f
        self.s = s
        self.initV = initV
    def start(self):
        return StateMachine(self.state, self.f, self.s.start(), self.initV)

'''

'''
