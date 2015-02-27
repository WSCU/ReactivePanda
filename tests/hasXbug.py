from ReactivePanda.Panda import *

#angle = getX(lbuttonPull)*pi

score = rvar(0)

text(score)
def re(m,v):
    print repr(score)
    print now(score)

react(lbp(), re)

start()