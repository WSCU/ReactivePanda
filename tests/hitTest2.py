from ReactivePanda.Panda import *

# Should just increment once.  Fixed error had the object continue to hit after exit
v1 = var(0)
text(v1)
p = panda()
s = soccerball(position = integral(p3(0,0,-1), p3(0,0,3)))

def hit1(m,v):
    exit(v)
    v1.add(1)

hit(p,s,hit1)


start()
