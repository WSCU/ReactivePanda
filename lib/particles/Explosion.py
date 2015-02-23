
__author__="michael Reed"
__date__ ="$Feb 26, 2009 9:54:52 PM$"


self.reset()

self.setPos(0.000, 0.000, 0.000)
self.setHpr(0.000, 0.000, 0.000)
self.setScale(1.000, 1.000, 1.000)
p0 = Particles.Particles('particles-1')
# Particles parameters
p0.setFactory("PointParticleFactory")
p0.setRenderer("PointParticleRenderer")
p0.setEmitter("SphereVolumeEmitter")
p0.setPoolSize(40000)
p0.setBirthRate(0.0200)
p0.setLitterSize(1000)
p0.setLitterSpread(10)
p0.setSystemLifespan(1.0000)
p0.setLocalVelocityFlag(1)
p0.setSystemGrowsOlderFlag(0)
# Factory parameters
p0.factory.setLifespanBase(0.5000)
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
p0.renderer.setStartColor(Vec4(1.00, 1.00, 0.30, 1.00))#Yellow
p0.renderer.setEndColor(Vec4(0.50, 0.00, 0.00, 1.00))#dark red
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
p0.emitter.setRadius(0.25000)
self.addParticles(p0)
#f0 = ForceGroup.ForceGroup('Frict')
#f1 = ForceGroup.ForceGroup('Grav')
## Force parameters
#force0 = LinearFrictionForce(1.0000, 21.0000, 0)
#force0.setActive(1)
#f0.addForce(force0)
#force1 = LinearVectorForce(Vec3(0.0000, 0.0000, 12.0000), 9.0000, 0)
#force1.setActive(1)
#f0.addForce(force1)
#force2 = LinearVectorForce(Vec3(0.0000, 0.0000, -9.000), 9.0000, 0)
#force2.setActive(1)
#f1.addForce(force2)
#self.addForceGroup(f0)
#self.addForceGroup(f1)