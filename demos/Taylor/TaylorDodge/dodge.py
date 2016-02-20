from PandaSRC.Panda import*

score = var(0)
world.color=cyan
text(format("Score:%d",score),size=2,color=violet)


directionalLight(hpr=hpr(81,.4,0), color = white)
ambientLight(color = color(.3,.3,.3))

p0=p3(0,0,0)

dv=hold(p3(0,0,0),key("leftArrow", p3(-2,0,0)) + key ("rightArrow",p3(2,0,0)) + key("upArrow",p3(0,0,2)) + key("downArrow",p3(0,0,-2)) + key("space",p3(0,0,0)))
d=dragon(position=p0 + integral(dv))
happen(getX(d.position) < -1, p3(0,0, 0))  + happen(getX(d.position) > 1, p3(0, 0, 0))


def death(m,v):
    if now(score) >=400:
        resetWorld()
        fire(position=p3(0,0,0),texture="fire2")
        likeFountainWater(position=p3(0,0,-1),size=2)
        text("Great Job",size=5,position=p2(0,0))
        text(format("final score: %d",score),size=3,position=p2(0,-.2))
        world.color=coral
        play("marioBrosTheme")
    else:
        resetWorld()
        text("I win u lose... now u die",size=5,position=p2(0,0),color=cyan)
        text(format("final score: %d",score),size=3,position=p2(0,-.2))
        world.color=coral
        pandaModel(("untitled.egg"),position=p3(0,3,0))
        play("loon")

def bomb(m,v):
    s=soccerBall(position=p3(randomRange(-3,3),0,3)+integral(p3(0,0,-1)+.5*p3(sin(localTime*4),0,0)),size=.2,tag=["bad"],hpr=hpr(time,1,6))
    hit1(d, s, death)

def sting(m,v):
    exit(m)
    exit(v)


def shoot(m,v):
    b=bee(position = now(d.position)+ p3(0,0,1)+integral(p3(0,0,3)),size=2)
    hit(b, "bad", sting)

react(key("a"),shoot)
a = clock(1)
react(a,bomb)

def addScore(m,v):
    score.add(40)
    exit(m)

def ford(m,v):
    f=jeep(position=p3(randomRange(-3,3),0,3)+integral(p3(0,0,-1)),hpr=hpr(time,time,6))
    hit(f, d, addScore)

a2 = clock(2)
react(a2,ford)


start()
