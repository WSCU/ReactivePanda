from Panda import *

camera.position=p3(0,-30, 6)

world.gravity = p3(0,0,-5)

paddle = boeing707(size = 3)

def col(t):
    return interpolate(t, forever(at(red) + to(.5, purple) + to(.5, blue) + to(.5, green) + to(.5, yellow) + to(.5, orange) + to(.5, red)))
world.color = col(localTime/2)

def moveLeft(m,p):
    p = now(m.position)
    paddle.position=  p + p3(-localTime*3, 0, 0)

def moveRight(m,p):
    p = now(m.position)
    paddle.position=  p + p3(localTime*3, 0, 0)
   
react(paddle, lbp(), moveLeft)
react(paddle, rbp(), moveRight)

def bounceFloor(m, v):
    v = now(m.velocity)
    p = now(m.position)
    v1 = p3(getX(v), getY(v), -getZ(v)*.95)
    launch(m, p, v1)

def bounceWall(m, v):
    v = now(m.velocity)
    p = now(m.position)
    v1 = p3(-getX(v), getY(v), getZ(v))
    launch(m, p, v1)

def die(m,v):
    text(("You Lose"), position = P2(-.3,.3),size = 10)

p = r2d2(size = 2)
launch(p, p3(0,0,10), p3(5, 0, 5))
when(p, (getZ(p.position) < 0) & (getZ(p.velocity) < 0) & (abs(p.position - paddle.position)<2.5), bounceFloor)
when(p, (getX(p.position) > 10) & (getX(p.velocity) > 0 ), bounceWall)
when(p, (getX(p.position) < -10) & (getX(p.velocity) < 0 ), bounceWall)
when1(p, (getZ(p.position) < -2), die)

start()