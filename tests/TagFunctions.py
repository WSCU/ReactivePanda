from Panda import *

panda(position = hold(p3(-1,-1,-1),tagList([p3(0,0,0),p3(1,1,1),p3(2,2,2)],lbp())))
panda(position = p3(hold(-1,tag(1,lbp())), 0,0))
panda(position = p3(hold(0,tagMap(lambda x: sqrt(x),tagCount(lbp()))), 0,0))

start()