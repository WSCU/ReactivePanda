from Panda import *

rectangle(p3(-4,0,-3), p3(4,0,-3), p3(-4,0,3), texture = "Clouds2.jpg")
text(time, size = 1.7, color = white)

al = ambientLight(color = color(.5,.5,.5))
dl = directionalLight(hpr = hpr(0,-1,0) )

p = panda(hpr = hpr(pi*.5,0,0), size = .4, color = color(.5,.5,sin(time)))

v = hold(p3(0,0,0), key("upArrow", p3(0,0,1.5))+key("downArrow", p3(0,0,-1.5))+key("leftArrow", p3(-1.5,0,0))+key("rightArrow", p3(1.5,0,0)) +
                    happen(getX(p.position) < -3, p3(1,0, 0))  + happen(getX(p.position) > 3, p3(-1, 0, 0))+ happen(getZ(p.position)> 2.4, p3(0,0,-1))+ happen(getZ(p.position)<-2.4, p3(0,0,1)))
p.position = p3(0,-.8,0)+integral(v)



def endGame(m, v):
    exit(m)
    exit(p)
    text(format("Fly free! Your score: %i seconds", now(time)), size = 3, position = p3(0,0,0), color = blue)

def randomBall(m, v):
    s = sphere(position = p3(4-localTime, -.8, randomRange(-2.5,2.5)), size = randomRange(.05,.2), duration = 8, color = color(randomRange(.8,1),randomRange(.8,1),randomRange(.8,1)))
    hit(s, p, endGame)

a = clock(step = .5)
react(a, randomBall)

start()
