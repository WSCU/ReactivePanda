from Panda import*



x=pandaModel(("taylor.egg"),position=p3(-1.5,0,0),size=.66,hpr=hpr(1.54,0,0),tag=["good"])
#x=jeep(position=p3(-1.5,0,0),size=2,hpr=sliderHpr(),kind="good")
pt0=p3(3,0,0)
p=panda(position=p3(-1.5,0,1.5),tag = ["great"])
p1=panda(position=p3(0,0,0),tag = ["great"])
p2=panda(position=p3(1,0,-1),tag = ["great"])
p3=panda(position=p3(-3,0,-1.5),tag = ["great"])
mv=hold(p3(0,0,0),key("leftArrow", p3(-2,0,0)) + key ("rightArrow",p3(2,0,0)) + key("upArrow",p3(0,0,2)) + key("downArrow",p3(0,0,-2)) + key("space",p3(0,0,0)))
gh=hold(hpr(0,0,0),key("1",hpr(1,0,0))+key("2",hpr(0,1,0))+key("3",hpr(0,0,1))+key("4",hpr(0,0,0)))

d=dragon(position=pt0 + integral(mv),tag=["bad"],hpr=hpr(0,0,0)+integral(gh))
f=fire(position=p3(0,8,10) ,hpr=hpr(0,-2.2,0),size=1)
text(d.hpr)

f._reparent(d)
#reparent(f, d) -- Change back later
#text(x.hpr)


def shoot(m,v):
    b=bee(position = now(x.position)+p3(0,0,.42)+integral(p3(1,0,0)),size=.1)
    hit(b, "bad", sting)

    b1=bee(position = now(p.position)+p3(0,0,-.2)+integral(p3(0,0,-1)),size=.1)
    hit(b1, "bad", sting)

    b2=bee(position = now(pp.position)+p3(0,0,.42)+integral(p3(-1,0,0)),size=.1)
    hit(b2, "bad", sting)

    b3=bee(position = now(ppp.position)+p3(0,0,.42)+integral(p3(-1,0,0)),size=.1)
    hit(b3, "bad", sting)

    b4=bee(position = now(pppp.position)+p3(0,0,.42)+integral(p3(1,0,0)),size=.1)
    hit(b4, "bad", sting)


react(key("a"),shoot)
a = alarm(1)


def fire1(m,v):

    ff=fire(position =p3(0,8,10) ,hpr=hpr(0,-2.2,0),size=3,duration=3,tag = ["fire1"])
    reparent(ff, d)


react(key("s"),fire1)

a1=alarm(1)

#def panda(m,v):
#    p(color=black)
#    pp(color=black)
#    ppp(color=black)
#    pppp(color=black)

def fire2(m,v):
    exit(m)
    exit(v)

def sting(m,v):
    exit(m)
    exit(v)

def death(m,v):
    if now(hit(x,d)):
        resetWorld()

        text("You Win",size=5,position=p2(0,0))
        world.color=silver
        play("marioBrosTheme")
    else:
        resetWorld()
        text("You Lose",size=5,position=p2(0,0),color=cyan)
        world.color=brown


react1(hit(x,d),death)
react1(hit(p,d),death)
react1(hit(pp,d),death)
react1(hit(ppp,d),death)
react1(hit(pppp,d),death)
#react1(hit("fire1",p),panda)
#react1(hit("fire1",pp),panda)
#react1(hit("fire1",ppp),panda)
#react1(hit("fire1",pppp),panda)



start()
