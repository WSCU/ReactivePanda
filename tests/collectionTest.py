from Panda import *

def destroy2(m,v):
    exit(m)
    exit(v)

# This should work but currently doesn't
# react1("pandas", "soccerballs", destroy2)

def firePanda(m,v):
    p = panda(position =  integral(p3(3,0,0), p3(-3,0,0)), tag = "pandas", size = 0.2)
    hit(p,"soccerballs", destroy2)

def fireBall(m,v):
    soccerBall(position = integral(p3(0,0,3), p3(0,0,-2)), tag = "soccerballs", size = 0.3)

react(clock(1), firePanda)
react(clock(1.427), fireBall)
start()