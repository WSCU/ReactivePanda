# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from Proxy import *
from Panda import *
from pandac.PandaModules import *
from pandac.PandaModules import *
from direct.particles.Particles import *
from direct.particles.ParticleEffect import *
from FileSearch import *
import PandaModel

def peffectUpdater(self):
    #These parameters find the static offset which was created during initialization and the current position which is returned by the self._get() method
    positionNow = self._get("position") + p3(0,0,0) # to make sure we do not get a zero object
    sizeNow = self._get("size") + 0
    hprNow = self._get( "hpr") + hpr(0,0,0)

    #print "size signal: "+repr(sizeScalar)+"  offset size: "+repr(sizeOffset)
    self._pandaModel.setScale(sizeNow)
    self._pandaModel.setPos(positionNow.x, positionNow.y, positionNow.z)
    self._pandaModel.setHpr(degrees(hprNow.h),
                            degrees(hprNow.p),
                            degrees(hprNow.r))
    if not self._onScreen:
#           print "Reparenting " + repr(self) + " to " + repr(self._parent)
           self._pandaModel.reparentTo(self._parent)
           self._onScreen = True

class PEffect(Proxy):

    def __init__(self, particleFn, name = 'particleEffect', 
               hpr = None, position = None,
                size = None, duration = 0, parent = render,
                **a): 
        Proxy.__init__(self, name = name + ":" + str(Globals.nextModelId), updater = peffectUpdater, types = {"position":p3Type, "hpr":hprType, "size":numType})
        
        #pathname = "/lib/panda/lib/lib-original/particles/"
        #base.enableParticles() #this should be in start in main program, this should probably go away
        base.enableParticles()
        p = ParticleEffect()
        self._pandaModel = p
        self._onScreen = False
        self._parent = getModel(parent)
        if position is not None:
            self.position = position
        else:
            self.position = P3(0, 0, 0)
        if hpr is not None:
            self.hpr = hpr
        else:
            self.hpr = SHPR(0, 0, 0)
        if size is not None:
            self.size = size
        else:
            self.size = 1
        particleFn(p, a)
        p.start()

        if duration > 0:
            react(self, delay(duration), exitScene)
    

def fireishFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(1024)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(1200.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(0.22)
    # Sprite parameters
    #print __import__("g").texture
    p0.renderer.setTexture(findTexture(dict["texture"]))
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.0050)
    p0.renderer.setFinalXScale(0.0200)
    p0.renderer.setInitialYScale(0.0100)
    p0.renderer.setFinalYScale(0.0200)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPNOBLEND)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 3.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Disc parameters
    p0.emitter.setRadius(0.5000)
    self.addParticles(p0)

def fireish(texture = "fire.png",lifeSpan = 1, lifeSpanSpread = 2, mass = 10,
     massSpread = 3, terminalVelocity = 10, terminalVelocitySpread = 3, lineScaler = 3,
     birthRate = 0.02,  **a):
        a["texture"] = texture
        a["lifeSpan"] = lifeSpan
        a["lifeSpanSpread"] = lifeSpanSpread
        a["mass"] = mass
        a["massSpread"] = massSpread
        a["terminalVelocity"] = terminalVelocity
        a["terminalVelocitySpread"] = terminalVelocitySpread
        a["birthRate"] = birthRate
        return PEffect(fireishFn, name = "fire", **a)

fire = fireish

def fireFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(1024)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(1200.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(0.22)
    # Sprite parameters
    #print __import__("g").texture
    p0.renderer.setTexture(findTexture(dict["texture"]))
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.0050)
    p0.renderer.setFinalXScale(0.0200)
    p0.renderer.setInitialYScale(0.0100)
    p0.renderer.setFinalYScale(0.0200)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPNOBLEND)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 3.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Disc parameters
    p0.emitter.setRadius(0.5000)
    self.addParticles(p0)

def fire1(texture = "fire.png", **a):
    a["texture"] = texture
    return PEffect(fireFn, name = "fire", **a)

def explosionsFn(self, dict):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(4000)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(1000)
    p0.setLitterSpread(10)
    p0.setSystemLifespan(1.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.25000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(1.00)
    p0.renderer.setStartColor(dict["headColor"].toVBase4())#Yellow
    p0.renderer.setEndColor(dict["tailColor"].toVBase4())#dark red
    p0.renderer.setBlendType(PointParticleRenderer.PPBLENDLIFE)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 9.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(dict["radius"])
    self.addParticles(p0)

def explosions(texture = "explosion.png",headColor = red, tailColor = orange, radius = 0.025, **a):
    a["texture"] = texture
    a["headColor"] = headColor
    a["tailColor"] = tailColor
    a["radius"] = radius
    return PEffect(explosionsFn, name = "explosions", **a)

def fireWorkFn(self, dict):
    self.reset()

    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(.0000, .0000, .0000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(10000)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(5000)
    p0.setLitterSpread(10)
    p0.setSystemLifespan(1.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(dict["pointSize"])
    p0.renderer.setStartColor(dict["headColor"].toVBase4())#Yellow
    p0.renderer.setEndColor(dict["tailColor"].toVBase4())#dark red
    p0.renderer.setBlendType(PointParticleRenderer.PPBLENDLIFE)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 1.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(dict["radius"])
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Sink')
    # Force parameters
    force0 = LinearVectorForce(Vec3(getX(dict["force"]), getY(dict["force"]), getZ(dict["force"])), 1.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)

def fireWorks(headColor = yellow, tailColor = red, radius = .25, force = p3(0,0,-2), pointSize = 1,
    lifeSpan = .5, lifeSpanSpread = .2, mass =1, massSpread = 0, terminalVelocity = 30,
    terminalVelocitySpread = .2, birthRate = 1.5, **a):
        a["lifeSpan"] = lifeSpan
        a["lifeSpanSpread"] = lifeSpanSpread
        a["mass"] = mass
        a["massSpread"] = massSpread
        a["terminalVelocity"] = terminalVelocity
        a["terminalVelocitySpread"] = terminalVelocitySpread
        a["headColor"] = headColor
        a["tailColor"] = tailColor
        a["force"] = force
        a["pointSize"] = pointSize
        a["radius"] = radius
        a["birthRate"] = birthRate
        return PEffect(fireWorkFn, name = "fireWork", **a)

def fireWork(duration = 2,  **a):
   return fireWorks(duration = duration, **a)

def intervalRingsFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("RingEmitter")
    p0.setPoolSize(30000)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(150)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(5.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(1.00)
    p0.renderer.setStartColor(dict["headColor"].toVBase4())
    p0.renderer.setEndColor(dict["tailColor"].toVBase4())
    p0.renderer.setBlendType(PointParticleRenderer.PPBLENDLIFE)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETCUSTOM)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 1.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Ring parameters
    p0.emitter.setRadius(3.0000)
    p0.emitter.setRadiusSpread(0.0000)
    p0.emitter.setAngle(31.6075)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Vortex')
    # Force parameters
    self.addForceGroup(f0)


def intervalRings(texture = None, headColor = blue, tailColor = white, **a):
    a["texture"] = texture
    a["headColor"] = headColor
    a["tailColor"] = tailColor
    return PEffect(intervalRingsFn, name = "intervalRings", **a)

def likeFountainWaterFn(self,dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("LineParticleRenderer")
    p0.setEmitter("TangentRingEmitter")
    p0.setPoolSize(10000)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(100)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(3.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Line parameters
    p0.renderer.setHeadColor(Vec4(0.00, 0.00, 1.00, 1.00))
    p0.renderer.setTailColor(Vec4(0.00, 1.00, 0.00, 1.00))
    p0.renderer.setLineScaleFactor(2.00)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 2.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Tangent Ring parameters
    p0.emitter.setRadius(0.5000)
    p0.emitter.setRadiusSpread(0.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Sink')
    # Force parameters
    force0 = LinearVectorForce(Vec3(0.0000, 0.0000, -1.5000), 1.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)

def likeFountainWater( **a):
    return PEffect(likeFountainWaterFn, name = "likeFountainWater", **a)

fountain = likeFountainWater

def rainFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("LineParticleRenderer")
    p0.setEmitter("RingEmitter")
    p0.setPoolSize(1024)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
    p0.renderer.setUserAlpha(1.00)
    # Line parameters
    p0.renderer.setHeadColor(dict["headColor"].toVBase4())
    p0.renderer.setTailColor(dict["tailColor"].toVBase4())
    p0.renderer.setLineScaleFactor(dict["lineScaler"])
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(3.0000)
    p0.emitter.setAmplitudeSpread(1.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Ring parameters
    p0.emitter.setRadius(1.0000)
    p0.emitter.setRadiusSpread(0.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Sink')
    # Force parameters
    force0 = LinearSinkForce(Point3(getX(dict["force"]), getY(dict["force"]),getZ(dict["force"])), LinearDistanceForce.FTONEOVERR, 1.0000, 1.0000, 1)
    force0.setVectorMasks(1, 1, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)

def rain(headColor = blue, tailColor = blue,lineScaler = 3, force = p3(0,0,-30), **a):
    a["headColor"] = headColor
    a["tailColor"] = tailColor
    a["lineScaler"] = lineScaler
    a["force"] = force
    return PEffect(rainFn, name = "rain", **a)

def shakenSparklesFn(self, dict ):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(10)
    p0.setLitterSpread(3)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(dict["headColor"].toVBase4())
    p0.renderer.setEdgeColor(dict["tailColor"].toVBase4())
    p0.renderer.setBirthRadius(0.1000)
    p0.renderer.setDeathRadius(0.1000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(1.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)
    if dict.has_key("force"):
        # Force parameters
        f0 = ForceGroup.ForceGroup('Sink')
        force0 = LinearSinkForce(Point3(getX(dict["force"]), getY(dict["force"]),getZ(dict["force"])), LinearDistanceForce.FTONEOVERR, 1.0000, 1.0000, 1)
        force0.setVectorMasks(1, 1, 1)
        force0.setActive(1)
        f0.addForce(force0)
        self.addForceGroup(f0)

def shakenSparkles(headColor = white, tailColor = white ,lifeSpan = 0.05, lifeSpanSpread = 1, mass = 1,
     massSpread = 0, terminalVelocity = 400, terminalVelocitySpread = 1, birthRate = 0.02, **a):
    a["headColor"] = headColor
    a["tailColor"] = tailColor
    a["lifeSpan"] = lifeSpan
    a["lifeSpanSpread"] = lifeSpanSpread
    a["mass"] = mass
    a["massSpread"] = massSpread
    a["terminalVelocity"] = terminalVelocity
    a["terminalVelocitySpread"] = terminalVelocitySpread
    a["birthRate"] = birthRate
    return PEffect(shakenSparklesFn, name = "shakenSparkles", **a)

def warpSpeedFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("LineParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(1024)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Line parameters
    p0.renderer.setHeadColor(dict["headColor"].toVBase4())
    p0.renderer.setTailColor(dict["tailColor"].toVBase4())
    p0.renderer.setLineScaleFactor(dict["lineScaler"])
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(2.0000)
    p0.emitter.setAmplitudeSpread(2.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)
    if dict.has_key("force"):
        # Force parameters
        f0 = ForceGroup.ForceGroup('Sink')
        force0 = LinearSinkForce(Point3(getX(dict["force"]), getY(dict["force"]),getZ(dict["force"])), LinearDistanceForce.FTONEOVERR, 1.0000, 1.0000, 1)
        force0.setVectorMasks(1, 1, 1)
        force0.setActive(1)
        f0.addForce(force0)
        self.addForceGroup(f0)



def warpSpeed(headColor = white, tailColor = blue,lifeSpan = 1, lifeSpanSpread = 2, mass = 10,
     massSpread = 3, terminalVelocity = 10, terminalVelocitySpread = 3, lineScaler = 3,
     birthRate = 0.02,  **a):
    a["headColor"] = headColor
    a["tailColor"] = tailColor
    a["lifeSpan"] = lifeSpan
    a["lifeSpanSpread"] = lifeSpanSpread
    a["mass"] = mass
    a["massSpread"] = massSpread
    a["terminalVelocity"] = terminalVelocity
    a["terminalVelocitySpread"] = terminalVelocitySpread
    a["lineScaler"] = lineScaler
    a["birthRate"] = birthRate
    return PEffect(warpSpeedFn, name = "warpSpeed", **a)


def warpFaceFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    #p0.setEmitter("DiscEmitter")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(20000)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(100)
    p0.setLitterSpread(10)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(0.22)
    # Sprite parameters
    #print __import__("g").texture
    p0.renderer.setTexture(findTexture(dict["texture"]))
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.0050)
    p0.renderer.setFinalXScale(0.0200)
    p0.renderer.setInitialYScale(0.0100)
    p0.renderer.setFinalYScale(0.0200)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPNOBLEND)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(6.0000)
    p0.emitter.setAmplitudeSpread(5.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(50.0000)
    self.addParticles(p0)

def warpFace (texture = "face.png",lifeSpan = 2, lifeSpanSpread = 1, mass = 10,
     massSpread = 5, terminalVelocity = 400, terminalVelocitySpread = 0,
     birthRate = 0.02,  **a):
         a["texture"] = texture
         a["lifeSpan"] = lifeSpan
         a["lifeSpanSpread"] = lifeSpanSpread
         a["mass"] = mass
         a["massSpread"] = massSpread
         a["terminalVelocity"] = terminalVelocity
         a["terminalVelocitySpread"] = terminalVelocitySpread
         a["birthRate"] = birthRate
         return PEffect(warpFaceFn, name = "warpFace", **a)


def heavySnowFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(60000)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(100)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(dict["pointSize"])
    p0.renderer.setStartColor(dict["headColor"].toVBase4())
    p0.renderer.setEndColor(dict["tailColor"].toVBase4())
    p0.renderer.setBlendType(PointParticleRenderer.PPONECOLOR)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPNOBLEND)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 9.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(9.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forrce')
    # Force parameters
    force0 = LinearVectorForce(Vec3(getX(dict["force"]), getY(dict["force"]), getZ(dict["force"])))
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)



def heavySnow (lifeSpan = 6, lifeSpanSpread = 0, mass = 1,
     massSpread = 0, terminalVelocity = 400, terminalVelocitySpread = 0,
     birthRate = 0.02, pointSize = 1, headColor = white, tailColor = white,
     force = p3(0,0,-9),  **a):
         a["pointSize"] = pointSize
         a["lifeSpan"] = lifeSpan
         a["lifeSpanSpread"] = lifeSpanSpread
         a["mass"] = mass
         a["massSpread"] = massSpread
         a["terminalVelocity"] = terminalVelocity
         a["terminalVelocitySpread"] = terminalVelocitySpread
         a["birthRate"] = birthRate
         a["headColor"] = headColor
         a["tailColor"] = tailColor
         a["force"] = force
         return PEffect(heavySnowFn, name = "heavySnow", **a)

def lightSnowFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(60000)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(3)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(dict["pointSize"])
    p0.renderer.setStartColor(dict["headColor"].toVBase4())
    p0.renderer.setEndColor(dict["tailColor"].toVBase4())
    p0.renderer.setBlendType(PointParticleRenderer.PPONECOLOR)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPNOBLEND)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 9.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(9.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forrce')
    # Force parameters
    force0 = LinearVectorForce(Vec3(getX(dict["force"]), getY(dict["force"]), getZ(dict["force"])))
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)

def lightSnow (lifeSpan = 6, lifeSpanSpread = 0, mass = 1,
     massSpread = 0, terminalVelocity = 400, terminalVelocitySpread = 0,
     birthRate = 0.02, pointSize = 1, headColor = white, tailColor = white,
     force = p3(0,0,-9),  **a):
         a["pointSize"] = pointSize
         a["lifeSpan"] = lifeSpan
         a["lifeSpanSpread"] = lifeSpanSpread
         a["mass"] = mass
         a["massSpread"] = massSpread
         a["terminalVelocity"] = terminalVelocity
         a["terminalVelocitySpread"] = terminalVelocitySpread
         a["birthRate"] = birthRate
         a["headColor"] = headColor
         a["tailColor"] = tailColor
         a["force"] = force
         return PEffect(lightSnowFn, name = "lightSnow", **a)

def smokeTailFn(self, dict):


    self.reset()

    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(.0000, .0000, .0000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(100000)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(1)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(1.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict['massSpread'])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(dict["pointSize"])
    p0.renderer.setBlendType(PointParticleRenderer.PPBLENDLIFE)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(0.0500)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Sink')
    # Force parameters
    force0 = LinearVectorForce(Vec3(getX(dict["force"]), getY(dict["force"]), getZ(dict["force"])), 1.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


def smokeTail(lifeSpan = 5, lifeSpanSpread = 0, mass = 0.005,
     massSpread = 0, terminalVelocity = 10, terminalVelocitySpread = 0,
     birthRate = 0.05, pointSize = .2, force = p3(-1,0,0),  **a):
         a["pointSize"] = pointSize
         a["lifeSpan"] = lifeSpan
         a["lifeSpanSpread"] = lifeSpanSpread
         a["mass"] = mass
         a["massSpread"] = massSpread
         a["terminalVelocity"] = terminalVelocity
         a["terminalVelocitySpread"] = terminalVelocitySpread
         a["birthRate"] = birthRate
         a["force"] = force
         return PEffect(smokeTailFn, name = "smokeTail", **a)

    





