from PandaSRC.Panda import *

def bigger(m, v):
    s = now(m.size)
    m.size = s*1.2
    
    
def shoot(m, v):
    p = panda(position = p3(localTime-3, 0, 0), size = 0.4)
    react1(p, leftClick(p), exitScene)
    react(p, rightClick(p), bigger)

react(clock(0.5), shoot)


start()
