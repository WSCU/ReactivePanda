
from Numerics import *
from Functions import *

def itime(i):
    return interpolate(localTime, i)

# Place one object (usually a camera) behind another, always oriented toward the
# object and at a fixed height and distance
def flatRod(cam, target, distance = 3, height = 0.5):
      cam.position = target.position + p3c(distance,  getH(target.hpr)+pi/2, height)
      cam.hpr = hpr(getH(target.hpr)+pi,0,0)

def pointForward(m):
    m.hpr = P3toHPR(deriv(m.position, p3(0,0,0)))

