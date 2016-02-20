from PandaSRC.Panda import *
# Background color didn't use to change
world.color = blue
jeep()
def newWorld():
    print "Setting to red"
    world.color = red
    panda()
def doReset():
    print "Doing reset"
    resetWorld(newWorld)
    print "Done with reset"
atTime(1, doReset)

start()
