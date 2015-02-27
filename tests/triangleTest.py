from ReactivePanda.Panda import *
# Test with both triangle and rectangle

#rectangle(p3(-2,0,0), p3(-2,0,1), p3(-1,0,0),color = red)
#rectangle(p3(0,0,0), p3(0,0,1), p3(1,0,0), texture="realpanda", hpr = hpr(time,0,0), side2 = "sand")

triangle(p3(-2,0,0), p3(-2,0,1), p3(-1,0,0),color = red)
triangle(p3(0,0,0), p3(0,0,1), p3(1,0,0), texture="realpanda", hpr = hpr(time,0,0), sideTwo = "sand")


start()