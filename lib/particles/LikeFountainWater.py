
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
