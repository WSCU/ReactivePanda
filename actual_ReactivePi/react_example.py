#from Panda import *
from Reactive import *


#p1 = panda()
#p2 = panda(position = p3(1.5, 0, 0))

l1 = light(3, False)
l2 = light(4, False)
l3 = light(5, False)
l4 = light(6, False)

fan1 = light(0, True)
'''true = fans off'''
fan2 = light(1, True)


keepOn = light(2,False)

rButton = button(2)
sensor = sonar(7, 7)

silent = var(True)

auto = var(False)

approach = happen(sensor < 2)

def shutup():
    l1.on = False
    l2.on = False
    l3.on = False
    l4.on = False
    fan1.on = True 
    fan2.on = True
    
def chooseRandomBehaviorA(m,v):
    setRandomBehavior()
    if not now(silent):
        react1(localTimeIs(30), chooseRandomBehaviorA)
    else:
        shutup()

def chooseRandomBehaviorS(m, v):
    setRandomBehavior()
    if not now(silent):
        react1(localTimeIs(300), nextRandomBehavior)

def nextRandomBehavior(m, v):
    react1(approach, chooseRandomBehaviorS)
        

def setRandomBehavior():
    print "setting random behavior"
    v = random01()
    p1 = random01() * 4 + 1
    l1d = random11()
    l1.on = sin(time * p1) < l1d
    p2 = random01() * 4 + 1
    l2d = random11()
    l2.on = sin(time * p2) < l2d
    p3 = random01() * 4 + 1
    l3d = random11()
    l3.on = sin(time * p2) < l3d
    p4 = random01() * 4 + 1
    l4d = random11()
    l4.on = sin(time * p4) < l4d
    if v < 1:
        fan1.on = interpolate(localTime, interpArr([(False, 15),(True,1)])) 
        fan2.on = False
        print "behavior 1"
    elif v < .5:
        pass
    elif v < .85:
        pass
    else:
        pass
    
def resetRButton(m,v):
    world.when1(rButton == True, modeChange)

def modeChange(m, v):
    '''world.resetReactions()'''
    world.when1(rButton == False, resetRButton)
    if now(silent):
        print "Auto mode"
        silent.set(False)
        auto.set(True)
        react1(localTimeIs(1), chooseRandomBehaviorA)
    else:
        if now(auto):
            print "Reactive mode"
            auto.set(False)
            shutup()
            react1(approach, chooseRandomBehaviorS)
        else:
            print "Silent"
            silent.set(True)
            shutup()

world.when1(rButton == True, modeChange)


start()
