from PandaSRC.Panda import *
d=55*(sin(time*4)+2)
h=2*time+5
p=time*time/(20+time)

rad=100
camera.position=d*hprToP3(hpr(h,p,0))
camera.hpr=hpr(h,p,0)
world.color=coral
directionalLight(hpr=sliderHpr(),color = white)
ambientLight(color = color(.3,.3,.3))


worldSize = 25
vel = 100
def bounceLeft(m, v):
    n = now(m.position)
    m.position = p3(-worldSize, getY(n), getZ(n)) + integral(vel*hprToP3(hpr(randomRange(0,pi),randomRange(-pi,pi),0)))


def bounceRight(m, v):
    n = now(m.position)
    m.position = p3(worldSize, getY(n), getZ(n)) + integral(vel*hprToP3(hpr(randomRange(pi,2*pi),randomRange(-pi,pi),0)))

def bounceTop(m, v):
    n = now(m.position)
    m.position = p3(getX(n), worldSize, getZ(n)) + integral(vel*hprToP3(hpr(randomRange(-pi,pi),randomRange(0,2*pi),0)))

def bounceBottom(m, v):
    n = now(m.position)
    m.position = p3(getX(n), -worldSize, getZ(n)) + integral(vel*hprToP3(hpr(randomRange(-pi,pi),randomRange(0,2*pi),0)))

def bounceBack(m, v):
    n = now(m.position)
    m.position = p3(getX(n), getY(n), -worldSize) + integral(vel*hprToP3(hpr(randomRange(-pi,pi),randomRange(pi,2*pi),0)))
def bounceFront(m, v):
    n = now(m.position)
    m.position = p3(getX(n), getY(n), worldSize) + integral(vel*hprToP3(hpr(randomRange(-pi,pi),randomRange(0,pi),0)))
path = at(red) + to(1,green) + to(30,silver) + to(30,lavender) + to(30,teal) + to(30,cyan) + to(30,tan) + to(30,salmon)

def hitStatic(m1, m2):
    exit(m1)
    t=now(time)
    s=sphere(position = now(m1.position), tag = ["static"], color = interpolate(t,forever(path)))
    genBall()
    fireish(p3 = p3(m.position), duration = .5,texture="fire2")

def genBall():
    b = soccerBall(position = vel*hprToP3(hpr(randomRange(0,2*pi),randomRange(0,2*pi),0)) +\
                   integral(vel*hprToP3(hpr(randomRange(0,2*pi),randomRange(0,2*pi),0))),tag = ["bouncer"])
    when(b,getX(b.position)>worldSize, bounceRight)
    when(b,getX(b.position)<-worldSize, bounceLeft)
    when(b,getY(b.position)>worldSize, bounceTop)
    when(b,getY(b.position)<-worldSize, bounceBottom)
    when(b,getZ(b.position)<-worldSize, bounceFront)
    when(b,getZ(b.position)>worldSize, bounceBack)
    hit(b, "static", hitStatic)

for i in range(48):
    genBall()

volleyBall(position = p3(10,0,0), tag = ["static"])
volleyBall(position = p3(-10,0,0), tag = ["static"])
volleyBall(position = p3(-1,0,6), tag = ["static"])
volleyBall(position = p3(3,2,-3), tag = ["static"])
start()


