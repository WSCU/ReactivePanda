from Panda import *

m = hangGlider()
grassScene(size=10)
#camera.position = p3(0,-50,0)
camera.flatrod(m)

friction = -1
climbK = 1
rv = -getX(mouse)*.1
pv = (getY(mouse)+1)/2 * .6 + .7
gravity = p3(0,0,-1)
#thrust = slider(max = 5)
thrust = 1
m.position = p3(15, 0, 0) + integral(m.velocity)
m.velocity = p3(-1,0,0) + integral(m.accel)
roll = integral(rv*abs(m.velocity))
hpr1 = p3ToHpr(m.velocity)
m.hpr = hpr(getH(hpr1), getP(hpr1), roll)
fwd = (thrust + abs(m.velocity) * friction) * norm(m.velocity)
lift = getUp(m.hpr)*climbK*abs(m.velocity)*pv
panda(position = m.position + getUp(m.hpr), size = .1)
text(format("Position: %s", m.position))
text(format("Velocity: %s", m.velocity))
text(format("Up: %s",  getUp(m.hpr)))
text(format("HPR: %s", m.hpr))
text(format("Gravity: %s", gravity))
text(format("Thrust: %s", fwd))
text(format("Lift: %s", lift))

m.accel = gravity + fwd + lift
start()
