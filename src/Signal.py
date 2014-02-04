class Signal:
    def __init__ (self, x):
        self.x = x
        self.startTime = Engine.globalTime
    def now(self):
        self.currentTime = Engine.globalTime - self.startTime
        return state(self, currentTime)   
    def state(self, time):
        return time/1000 * time/2000
        
