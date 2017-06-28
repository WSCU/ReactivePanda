from PandaSRC.Panda import *
# Background color didn't use to change
world.color = blue
jeep()

def newWorld():
    print("Setting to red")
    world.color = red
    panda1 = panda(position=p3(-3,0,0))
    panda2 = panda()
    hit(panda1, panda2, printText)
    print("Time: " + str(now(time)))
    react(clock(2, start=now(time)), printText)
#    atTime(5, text)
    print("After react call")
    
def doReset():
    print("Doing reset")
    resetWorld(newWorld)
    print("Done with reset")

def printText(m, v):
    text("Hello!")
    print "adsa"
    
atTime(2, doReset)

##### We need to double check why the function is being called with only 1 param

start()
