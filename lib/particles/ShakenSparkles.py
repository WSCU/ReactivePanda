
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
p0.setBirthRate(0.2000)
p0.setLitterSize(10)
p0.setLitterSpread(3)
p0.setSystemLifespan(0.0000)
p0.setLocalVelocityFlag(1)
p0.setSystemGrowsOlderFlag(0)
# Factory parameters
p0.factory.setLifespanBase(0.05000)
p0.factory.setLifespanSpread(1.0000)
p0.factory.setMassBase(1.0000)
p0.factory.setMassSpread(0.0000)
p0.factory.setTerminalVelocityBase(400.0000)
p0.factory.setTerminalVelocitySpread(1.0000)
# Point factory parameters
# Renderer parameters
p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
p0.renderer.setUserAlpha(1.00)
# Sparkle parameters
p0.renderer.setCenterColor(Vec4(1.00, 1.00, 1.00, 1.00))
p0.renderer.setEdgeColor(Vec4(1.00, 1.00, 1.00, 1.00))
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
