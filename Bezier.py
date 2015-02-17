# allow use of actor
from direct.gui.DirectGui import * # 2D GUI elements
from . Maze import *
#from Racetrack import *
from pythonfrp.World import *
#from Time import *
from . Color import *
from . PandaModels import *
from pythonfrp.Proxy import *
from pythonfrp.Numerics import *
from . Numerics import *
from . Slider import *
from . Text import *
#from Signal import time, static
#from FRP import *
# from Switch import *
from . Light import *
from . Sound import *
from . Button import *
from . Menu import *
from . PEffect import *
from . DynamicGeometry import *
#from Interp import *
#from TextBox import *
#from PoseAndScriptFiles import *
#from Utils import *
#from Roll import *
from . Globals import *
from . Camera import camera
from pythonfrp.Functions import *

class Bezier:
    def __init__ (self, p00, p01, p02, p03):
        self.p00 = p00
        self.p01 = p01
        self.p02 = p02
        self.p03 = p03
#        bunny(position = self.p00)
#        bunny(position = self.p01)
#        bunny(position = self.p02)
#        bunny(position = self.p03)
        print("p00 "+ str(p00))
        print("p01 "+ str(p01))
        print("p02 "+ str(p02))
        print("p03 "+ str(p03))

    def interp(self, time):
        p10 = staticLerp(time, self.p00, self.p01)
        p11 = staticLerp(time, self.p01, self.p02)
        p12 = staticLerp(time, self.p02, self.p03)
        p20 = staticLerp(time, p10, p11)
        p21 = staticLerp(time, p11, p12)
        p30 = staticLerp(time, p20, p21)
        #print "p10 "+ str(p10)
        #print "p11 "+ str(p11)
        #print "p12 "+ str(p12)
        #print "p20 "+ str(p20)
        #print "p21 "+ str(p21)
        #print "p30 "+ str(p30)
        return (p30, p21-p20)

class PatchElement:
    def __init__(self, point, hpr, speed):
        self.point = point
        self.velocity = speed * HPRtoP3(hpr)
        self.roll = hpr.r
        self.duration = 0
        self.start = 0
        self.hpr = hpr
        self.speed = speed

class Patch:
    def __init__ (self):
        self.patchList = []

    def add(self, point, hpr, speed):
        pe = PatchElement(point, hpr, speed)
        self.patchList.append(pe)

        if len(self.patchList) > 1:
            prev = self.patchList[len(self.patchList)- 2]
            prev.duration = deltaT(pe.point, pe.velocity, prev.point, prev.velocity)
            pe.start = prev.start + prev.duration
            prev.rollFinal = hpr.r
            p01 = prev.point - prev.velocity * prev.duration*(1.0/3)
            p02 = pe.point + pe.velocity * prev.duration*(1.0/3)
            prev.bezier = Bezier(prev.point, p01, p02, pe.point)
    def delPoint(self):
        if len(self.patchList) > 0:
            del self.patchList[-1]
        if len(self.patchList) == 0:
            return SP3(0,0,0), SHPR(0,0,0)
        return self.patchList[-1].point, self.patchList[-1].hpr
    def interp(self, time):
        if len(self.patchList) < 2:
            return (P3(0,0,0), HPR(0,0,0))
        high = len(self.patchList)-2
        low = 0
        pe = self.patchList[0]
        if time < 0:
            return self.patchList[0].point, self.patchList[0].hpr
        elif(time >= self.duration()):
            return self.patchList[-1].point, self.patchList[-1].hpr
        else:
            while True:
               i = int((high+low)/2)
               pe1 =  self.patchList[i]

               if time >= pe1.start and time <= pe1.start + pe1.duration:
                   pe = pe1
                   break

               if time > pe1.start:
                   low = i + 1
                   if low > len(self.patchList)-2:
                       break
               else:
                   high = i - 1
                   if high < 0:
                       break
        #print str(pe.duration)
        localT = (time - pe.start)/pe.duration
        print("Time " + str(time) + " Local t " + str(localT) + " # " + str(i))
        roll = staticLerpA(localT, pe.roll, pe.rollFinal)
        pos, v = pe.bezier.interp(localT)
        #print "velocity "+str(v)
        hpr = sP3toHPR(v)
        #print "hpr "+ str(hpr)
        return (pos, SHPR(pi+hpr.h, hpr.p, roll))

    def getPos(self, s):
        return lift("bezierControl", lambda t: self.interp(t)[0], [numType], p3Type)(s)
    def getHPR(self, s):
        return lift("bezierControl", lambda t: self.interp(t)[1], [numType], hprType)(s)
    def duration(self):
        return self.patchList[len(self.patchList)- 1].start
    def saveToFile(self, fname, status):
        file = fname + ".csv"
        result = []
        for patch in self.patchList:
            result.append(str(patch.point.x) + "," + str(patch.point.y) + "," + str(patch.point.z) + "," +
                          str(patch.hpr.h) + ", " + str(patch.hpr.p) + ", " + str(patch.hpr.r) + "," +
                          str(patch.speed) + "\n")
        saver = open(file ,"w")
        saver.writelines(result)
        saver.close()
        status.set("Path " + fname + " written to disk")


def deltaT(p1, v1, p2, v2):
        distance = abs(p1 - p2)
        if distance == 0:
            distance = .1
        speed = (abs(v1) + abs(v2))*.5
        if speed == 0:
            speed = 1
        deltaT = distance/speed
        return deltaT



#p = panda(position = P3C(1,time/5, sin(time*4)/5))
#pointForward(p)

#text(norm(deriv(p.position)))
#text(HPRtoP3(p.hpr))

def saveCamera(name):
    status = var("Ready")
    len = var(0)

    text(status, position = P2(0, .95))
    text(" ")
    text(format("Camera: %s", camera.position))
    models = [[]]
    sTime = slider(min = 0 , max = 1, label = "t", position = P2(.8, .8))
    speed = slider(max = 100, min = 1, label = "Speed", position = P2(.8, .72))
    roll = slider(max = 2*pi, label = "Roll", position = P2(.8, .64))
    text(format("Time: %s", sTime*len))
    spb = button("Save Point")
    sfb = button("Save File")
    pathb = button("Show Path")
    pvb = button("Preview")
    delp = button("Delete")
    spline = Patch()
    previewing = var(0)
    rp = rbuttonPull
    def addPoint(m, v):
        cp = now(camera.position)
        chpr = now(camera.hpr)
        spline.add( cp, chpr, now(speed))
        status.set("Added a point at " + str(cp) + " hpr = " + str(chpr))  # Should say where and how many
        #bunny(position = cp, hpr = chpr)

    react(spb,addPoint)
    def camerapreview(m, v):
        for m in models[0]:
            m.exit()
        models[0] = []
        if now(previewing) == 0:
            camera.position = spline.getPos(sTime * spline.duration())
            camera.hpr = spline.getHPR(sTime*spline.duration())
            status.set("Preview mode - move camera with time slider")
            len.set(spline.duration())
        else:
            world1.t = 0
            camera.hpr = HPR(getX(rp), getY(rp), roll)  # Control the camera hpr with the
            v = choose(lbutton, -speed, 0)  # left button to move
            pos = now(camera.position) + integral(v*HPRtoP3(camera.hpr))
            camera.position = pos
            status.set("Exiting preview mode")
        previewing.set(1-now(previewing))
    react(pvb, camerapreview)
    def delPoint(m, v):
        oldpos, oldhpr = spline.delPoint()
        rp1 = now(rp)
        camera.hpr = oldhpr + HPR(getX(rp)-getX(rp1), getY(rp) - getY(rp1), roll)  # Control the camera hpr with the
        v = choose(lbutton, -speed, 0)  # left button to move
        pos = oldpos + integral(v*HPRtoP3(camera.hpr))
        camera.position = pos
        status.set("Deleted last point")
    react(delp, delPoint)
    def preview(m, v):
        t = 0
        while t< spline.duration():
            ppos, phpr = spline.interp(t)
            pan = panda(size = .5, position = ppos, hpr = phpr)
            models[0].append(pan)
            t = t +.1
        status.set("Camera path visualized")
        #  Add bunnies
    react(pathb, preview)

    def saveFile(m, v):
        spline.saveToFile(name, status)
        status.set("Saved to file")
    react(sfb, saveFile)
    #text(format("Camera is at %f", camera.position))
    camera.hpr = HPR(getX(rp), getY(rp), roll)  # Control the camera hpr with the
    v = choose(lbutton, -speed, 0)  # left button to move
    pos = integral(v*HPRtoP3(camera.hpr))
    camera.position = pos


def launchCamera(fileName):
    spline = Patch()
    fileLoader = open(fileName + ".csv",  "r")
    contents = fileLoader.read().split("\n")
    for line in contents:
        data = line.split(",")
        if len(data) == 7:
                x = float(data[0].strip())
                y = float(data[1].strip())
                z = float(data[2].strip())
                h = float(data[3].strip())
                p = float(data[4].strip())
                r = float(data[5].strip())
                speed = float(data[6].strip())
                hpr = HPR(h, p, r)
                point = P3(x,y,z)

                spline.add(point, hpr, speed)
    fileLoader.close()
    camera.position = spline.getPos(time)
    camera.hpr = spline.getHPR(time)

