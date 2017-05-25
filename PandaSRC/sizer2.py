from PandaSRC.Panda import *

# Problems with the photo - need to use a rectangle instead.
# No way to see which way is forward
# No mark on the floor to show where feet should go
maxHPR = pi

h = slider(position = P2(1,.85), min=-maxHPR,max = maxHPR, init = 0, label = "H")
p = slider(position = P2(1,.8), min=-maxHPR,max = maxHPR,init=0,label = "P")
r = slider(position = P2(1,.75), min=-maxHPR,max = maxHPR, init = 0, label = "R")

maxPos = 1
x = slider(position = P2(1,.55), min=-maxPos,max = maxPos, init = 0, label = "X")
y = slider(position = P2(1,.5), min=-maxPos,max = maxPos, init = 0, label = "Y")
z = slider(position = P2(1,.45), min=-maxPos,max = maxPos, init = 0, label = "Z")

size = slider(position = P2(1,.25), min=1,max = 10, init = 1, label = "Size")
lightangle = slider(position = P2(1, .15), min = 0, max = 2*pi, init = 2, label = "Light")

sizeOffset = accum(1, key("q", times(10)) + key("a",times(.1)))
#Height and Zoom factor, doesn't do anything to the model.
text("Camera Pitch", position=P2(1,-.05))
height = slider(position = P2(1,-.1), min=-.5, max=.5, init = 0)
text("Camera Zoom",position=P2(1,.05))
zoom = slider(position = P2(1,0),min=0,max=10,init=5)
####################
##This is the model you'd have to change

model = crow(position = P3(x,y,z), hpr = HPR(h, p, r), size=size*sizeOffset)
####################

overhead = hold(False, key('u', True) + key('s', False))
angle = getX(lbuttonPull)*pi
camera.position = choose(overhead, P3(0,0,10), P3(sin(angle)*zoom, cos(angle)*zoom,-getY(lbuttonPull)))
camera.hpr = choose(overhead, HPR(0, -pi/2, 0), HPR(-angle+pi,height*pi,0))


##############
#Reference Rectangle Generation:
floor = -1
wallRight = 1
wallLeft = -1
wallDepth = 1
lowerLeft = P3(wallLeft,-wallDepth,floor)
lowerRight = P3(wallRight,-wallDepth,floor)
backLeft = P3(wallLeft,wallDepth,floor)
backRight = P3(wallRight,wallDepth,floor)
frontLeft = P3(wallLeft,-wallDepth,1)
frontRight = P3(wallRight,-wallDepth,1)
ts = .2
leftRect = rectangle(lowerLeft,frontLeft,backLeft,red)
#floorRect = photo(lowerLeft,lowerRight,backLeft,"C:\Users\Camp\Desktop\grahamcode\src\MineCraftGuy.egg")
centerRect = rectangle(P3(wallLeft,-wallDepth,floor+1),P3(wallRight,-wallDepth,floor+1),\
             P3(wallLeft,wallDepth,floor+1),purple)
targetRect = rectangle(P3(ts* wallLeft,-ts* wallDepth,floor+1.001),P3(ts*wallRight,-ts*wallDepth,floor+1.001),\
             P3(ts*wallLeft,ts*wallDepth,floor+1.001),white)
rightRect = rectangle(lowerRight,frontRight,backRight,green)
##############

text("Model Sizer")
text("Mouse Controls Camera")
text("'q' scales up by 10x, 'a' scales down by .1x")
text("Size slider for finer scale detail.")
text("u moves camera up, s to side")
text(model.hpr, position=P2(1,.9))
text(model.position,position=P2(1,.6))
text(model.size, position=P2(1,.3))
#directionallight(color = white, hpr = HPR(lightangle, 0 ,0))
#ambientlight(color = color(.5, .5, .5))
def printer(w, x):
    f = open("",'r+')
    print("localSize, " + str(now(model.size)) + "\nlocalPosition, " + \
        str(now(model.position)) + "\nlocalOrientation, " + str(now(model.hpr))
    f.write("localSize, " + str(now(model.size)) + "\nlocalPosition, " + \
        str(now(model.position)) + "\nlocalOrientation, " + str(now(model.hpr)))
    f.close())

printButton = button("Print to Console", position = P2(1, -.8), size = 1)
react(printButton, printer)


start()
