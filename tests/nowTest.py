from ReactivePanda.Panda import *
# Each panda should be bigger if now works on reactive variables.
va = var(1)
def makeB(m, v):
    panda(position = p3(random11()*3, 0, random11()*2), size = now(va))
    va.add(.5)
react(lbp(), makeB)
start()

