from ReactivePanda.Panda import *

# panda disappears on lbp, bunny at 2 seconds

p = panda(position = p3(time, 0, 0))
react(lbp(),lambda m, v: exit(p))
bunny(position = p3(1,0,0), duration = 2)
start()