from Panda import *

car = jeep(size = 0.25)
setType(car.velocity, P3Type)
setType(car.angle, numType)
track = Racetrack("track.txt", model = car)
text(format("Score: %i", track.score))
camera.flatrod(car, distance = 2)
spinThresh = 10   # Force at which we spin out
engineForce = 5   # Power of the engine
frictionForce = 10    # Scales track friction

carhit = Sound("break.wav", volume = 150)
soundwipeout = Sound("screetch.wav", loopCount = 12)
soundwipeout.setRate(3)
soundmove = Sound("engine.wav", loopCount = 0)

def driving(model, p0, h0, speed0):
    print "Driving"
#    text(speed0)
    a1 = hold(0, key("arrow_right",  -1) + keyUp("arrow_right",  0))
    a2 = hold(0, key("arrow_left",  1) + keyUp("arrow_left",  0))
    a3 = hold(0, key("arrow_up",  1) + keyUp("arrow_up",  0))
    a4 = hold(0, key("arrow_down",  -1) + keyUp("arrow_down",  0))
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
    model.hpr = HPR(h,0,0)
    model.velocity = P3C(speed1,h-pi/2,0)
    model.position = p0 + integral(model.velocity)
    model.when1(abs(model.angle*abs(model.velocity)*abs(model.velocity)) > spinThresh, spinout)
    model.when1(track.inWall(model), wallburn)
    model.react1(key(" "), jump)
    
def driveReset(model, var):
    drive(model, var, resetSpeed = 1)
    
def spinout(model, var):
    print "SPINNIN'"
    p0 = now(model.position)
    hpr0 = now(model.hpr)
    v0 = now(model.velocity)
    model.position = p0 + integral(v0 * (1 - localTime / 3))
    model.hpr = hpr0 + HPR(integral(20 * (1 - localTime / 3)),0,0)
    soundwipeout.play()
    # drive away
    model.react1(localTimeIs(3), driveReset)

def chp(hpr):
    return HPR(getH(hpr), -getP(hpr), getR(hpr))

def jump(model, var):
    print "Jumping"
    p0 = now(model.position)
    v0 = now(model.velocity)
    hpr0 = now(model.hpr)
    
    model.velocity = P3(getX(v0), getY(v0), 1.5) + integral(P3(0,0,-1))
    model.position = p0 + integral(model.velocity)
    
    model.hpr = chp(P3toHPR(deriv(model.position, HPRtoP3(hpr0))))
    
    model.when1(getZ(model.position)<0, drive)

def drive(model, var, resetSpeed = 0):
    p0 = now(model.position)
    hpr0 = now(model.hpr)
    v0 = 0 if resetSpeed == 1 else now(model.velocity)
    driving(model, P3(getX(p0), getY(p0), 0), getH(hpr0), abs(v0))

def burning(model, p0, hpr0):
    print "burning"
    
    model.position = p0
    model.hpr = hpr0
    s = fireish(position = p0, duration = 1)

    # reset the model
    model.react1(localTimeIs(1), respawn)

def respawn(m, v):
    driving(car, P3(4,4,0), pi/2, 0)

# burning reaction
def burn(model, var):
    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)
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

def powerUp(model, var):
    p = now(model.position)
    s = shakenSparkles(position = p)
    s.react1(localTimeIs(1), stopIt)

def explosion(model, var):
    p = now(model.position)
    s = fireish(position = p)
    s.react1(localTimeIs(1), stopIt)

# end item reactions

# item generation
def generateObj(model, var):
    track.placeObj(coin, size = .1, position = P3(randomRange(5,track.xmax-5),randomRange(5,track.ymax-5),sin(time * 4) / 64 + .05), score = 1, reaction = powerUp, duration = 30, sound = "good.mp3")

# Other diving reactions
#def setSpeed(m, v):
#    s = abs(now(car.velocity))
#    soundmove.setRate(s)

soundmove.play()

#setAlphaScale(0.5)

a = alarm(step = 4)
react(a, generateObj)


driving(car, P3(4,4,0), pi/2, 0)
#car.react(dist(car.position, P3(5,5,0))<.5, jump) #When the car hits the panda

start()