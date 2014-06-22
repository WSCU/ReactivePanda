from Panda import *
def man(**a):
    return model("man.egg",**a)
car = jeep(size = 0.25,kind="bullet")
setType(car.velocity, P3Type)
setType(car.angle, numType)
track = Racetrack("track.txt", model = car)
#text(format("Score: %i", track.score))
camera.flatrod(car, distance = 2)
spinThresh = 10   # Force at which we spin out
engineForce = 5   # Power of the engine
frictionForce = 10    # Scales track friction
score= var(0)

text(format("Score: %d", score))
carhit = Sound("break.wav", volume = 150)
soundwipeout = Sound("screetch.wav", loopCount = 12)
soundwipeout.setRate(3)
soundmove = Sound("engine.wav", loopCount = 0)
def boss(m,v):
#     q=p3(0,0,-2)
#     t=truck(position=p3(0,0,2) + integral(q), size = 2)
   
    p0 = now(car.position) + p3c(3, randomRange(0,2*pi), 0)
    q = man(size = .5, hpr=hpr(time,0.2*sin(time*10),0), duration = 20, position = p0, kind="panda")
  

 
    
  
#    rm(q, p3(0,0,5))
#    react(q,localTimeIs(2), moveagain)
    
    reactAll(q, hit(q,"bullet"), blowUp1)
    reactAll(q, hit(q,"bullet"), addScore)
a4=alarm(1)
react(a4,boss)


def driving(model, p0, h0, speed0):
    print "Driving"
#    text(speed0)
    a1 = hold(0, key("rightArrow",  -1) + keyUp("rightArrow",  0))
    a2 = hold(0, key("leftArrow",  1) + keyUp("leftArrow",  0))
    a3 = hold(0, key("upArrow",  1) + keyUp("upArrow",  0))
    a4 = hold(0, key("downArrow",  -1) + keyUp("downArrow",  0))
    delta = a1 + a2
    dspeed = a3 + a4

    decay = -1.95*model.angle   # Straighten wheels after turning
    model.angle = integral(delta + decay)   # Should be limited

    # the force on the vehicle
    forward = (speed0 * 4) + engineForce * integral(dspeed)
    # velocity
    fvelocity = abs(model.velocity)
    # friction on vehicle
    # get friction from track
    pushBack = track.friction(model.position)
    friction = pushBack * frictionForce * fvelocity
    # speed
    speed = integral(forward - friction)
#    text(speed)
    speed1 = choose(speed < -.4, -.4, speed)
    # heading
    h = h0 + integral(speed1 * model.angle)
    model.hpr = hpr(h,0,0)
    model.velocity = p3c(speed1,h-pi/2,0)
    model.position = p0 + integral(model.velocity)
    when1(model, track.inWall(model), wallburn)






def chp(hpr):
    return hpr(getH(hpr), -getP(hpr), getR(hpr))



def drive(model, var, resetSpeed = 0):
    p0 = now(model.position)
    hpr0 = now(model.hpr)
    v0 = 0 if resetSpeed == 1 else now(model.velocity)
    driving(model, p3(getX(p0), getY(p0), 0), getH(hpr0), abs(v0))

def burning(model, p0, hpr0):
    print "burning"

    model.position = p0
    model.hpr = hpr0
    fireish(position = p0, duration = 1)

    # reset the model
    react1(model, localTimeIs(1), respawn)

def respawn(m, v):
    driving(car, p3(4,4,0), pi/2, 0)

# burning reaction
def burn(model, var):
    # preserve state
    p = now(model.position)
    #hpr = now(model.hpr)
    # burning!
    play("bad.mp3")
    burning(model, p, hpr)

def wallburn(model, var):
    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)
    # burning!
    carhit.play()
    burning(model, p, hpr)


def explosion(model, var):
    p = now(model.position)
    s = fireish(position = p)
    react1(s, wait(1), stopIt)


def addScore(m,v):
    score.add(20)
    exit(m)


def blowUp1(m, v):
    addScore(m,v)
    exit(m)
    fireish(position = now(m.position), duration = 1)
    play("explosion2")

# end item reactions

# item generation


# Other diving reactions
#def setSpeed(m, v):
#    s = abs(now(car.velocity))
#    soundmove.setRate(s)


#setAlphaScale(0.5)

#a = alarm(step = 4)
#react(a, generateObj)


driving(car, p3(4,4,0), pi/2, 0)
#car.react(dist(car.position, p3(5,5,0))<.5, jump) #When the car hits the panda

start()