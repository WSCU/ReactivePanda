

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
p0.setBirthRate(0.5000)
p0.setLitterSize(1)
p0.setLitterSpread(1)
p0.setSystemLifespan(1.0000)
p0.setLocalVelocityFlag(1)
p0.setSystemGrowsOlderFlag(0)
# Factory parameters
p0.factory.setLifespanBase(0.5000)
p0.factory.setLifespanSpread(0.0000)
p0.factory.setMassBase(0.0050)
p0.factory.setMassSpread(0.0000)
p0.factory.setTerminalVelocityBase(10.0000)
p0.factory.setTerminalVelocitySpread(0.0000)
# Point factory parameters
# Renderer parameters
p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
p0.renderer.setUserAlpha(1.00)
# Point parameters
p0.renderer.setPointSize(0.20)
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
force0 = LinearVectorForce(Vec3(0.0000, 0.0000, -1.0000), 1.0000, 0)
force0.setActive(1)
f0.addForce(force0)
self.addForceGroup(f0)
#force1 = LinearVectorForce(Vec3(12.0000, 0.0000, 0.0000), 5.0000, 0)
#force1.setActive(1)
#f0.addForce(force1)
#force2 = LinearVectorForce(Vec3(0.0000, 0.0000, 0.000), 5.0000, 0)
#force2.setActive(1)
#f1.addForce(force2)
#self.addForceGroup(f0)
#self.addForceGroup(f1)
