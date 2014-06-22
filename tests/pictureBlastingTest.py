from Panda import *
#frags = blastPicture("realpanda", rows = 5, columns = 5)
#for f in frags:
#    f.position = itime(at(p3(random11(), random11(), random11()))+to(2,f._location))
c, frags = slicePicture("realpanda", rows = 5, columns = 5)
for f in frags:
    f.position = itime(at(p3(random11(), random11(), random11()))+to(2,p3(0,0,0)))
c.hpr = hpr(time, 0, 0)
start()
