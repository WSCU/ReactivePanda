from Panda import *

camera.position = p3(0,-100, 0)

head1 = soccerBall(size = .5,tag = ["head"])
head2 = soccerBall(size = .5,position=p3(2,0,0),tag = ["head"])
head2.dir = hold(p3(0,0,1), key("upArrow", p3(0,0,1)) + key("downArrow", p3(0,0,-1)) + \
                      key("leftArrow", p3(-1,0,0)) + key("rightArrow", p3(1,0,0)))
head1.dir = hold(p3(0,0,1), key("w", p3(0,0,1)) + key("s", p3(0,0,-1)) + \
                      key("a", p3(-1,0,0)) + key("d", p3(1,0,0)))

a = clock(.2)
head1._length = 3
head2._length = 3

def moveHead1(m, v):
    d = now(head1.dir)
    loc = now(head1.position)
    s=sphere(position =  loc, size = .45, color = color(random01(), random01(), random01()), duration = head1._length, tag = ["tail"])
    head1.position = loc + d
    if getX(loc)>30:
        die(m,v)
    if getX (loc)<-30:
        die(m,v)
    if getZ (loc)>20:
        die(m,v)
    if getZ (loc)<-20:
         die(m,v)
def moveHead2(m, v):
    d = now(head2.dir)
    loc = now(head2.position)
    s=sphere(position =  loc, size = .45, color = color(random01(), random01(), random01()), duration = head2._length, tag = ["tail"])
    head2.position = loc + d
    if getX(loc)>30:
        die(m,v)
    if getX (loc)<-30:
        die(m,v)
    if getZ (loc)>30:
        die(m,v)
    if getZ (loc)<-30:
         die(m,v)


react(a, moveHead1)
react(a, moveHead2)
def eat(m, v):
    m._length = m._length + 1
    print head1._length
    print head2._length
    exit(v)
    volleyBall(position = p3(randomInt(-30,30),0,randomInt(-30,30)), tag = ["food"], size = .45)

def die(m, v):
    resetWorld()
    text(head1._length)

food = volleyBall(position = p3(5,0,5), tag = ["food"], size = .45)
hit(head1, "tail", die)
hit(head1, "food", eat)
hit(head2, "tail", die)
hit(head2, "food", eat)



start()
