import sched, time, StateMachine

world = StateMachine(self, 1)
globalTime = 0

s = sched.scheduler(time.time, time.sleep)
s.enter(100, 1, tick(), ())
s.run()

def tick():
    globalTime += 100
    world.refresh(self)
    print world.state 
