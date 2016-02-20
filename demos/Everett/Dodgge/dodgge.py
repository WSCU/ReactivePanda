from PandaSRC.Panda import *
score = var(0)

text(format("Score: %d", score))

p0 = p3(0,0,0)
pv = hold (p3(0,0,0),key("leftArrow", p3(-1,0,0)) + key ("rightArrow" , p3(1,0,0)) + key ("upArrow" , p3(0,0,1)) + key ("downArrow" , p3(0,0,-1)) + key ("z" , p3(0,0,0)))


p = panda ( position = p0 + integral (pv), size = .5)

def bomb(m,v):
    h=randomRange(3,3)
    x=randomRange(-3,3)
    s=soccerBall (position = p3(x,0,h) + integral(p3( 0,0,-2)), tag = ["bad"] ,size= .2)
    hit(s, p, die)

def die(m,v):
    resetWorld()
    text("Try again", size=5, position = p2 (0,0))

def addScore (m,v):
    score.add(1)
    exit(m)

def peng (m,v):
    q=randomRange(3,3)
    a=randomRange(-3,3)
    pn=penguin (position = p3(a,0,q) + integral (p3(0,0,-1)))
    hit(pn, p, addScore)

   # pn=penguin (position = p3(a,0,q) + integral(p3( 0,0,-2)),size= .2)

def sting(m,v):
    exit(m)
    exit(v)
    addScore(m,v)
    fireish(position = m.position, duration = .4)
    play("explosion1")

def shoot(m,v):
    b=bee (position= now(p.position) + p3(0,0,1) +integral(p3(0,0,3)))
    reactAll(b, hit(b, "bad"), sting)
    hit(b, "bad", sting)
react(key(" "), shoot)


a = clock(2)
react(a, bomb)
react(a,peng)

start()
