
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
p0.setBirthRate(0.0500)
p0.setLitterSize(100)
p0.setLitterSpread(10)
p0.setSystemLifespan(0.0000)
p0.setLocalVelocityFlag(1)
p0.setSystemGrowsOlderFlag(0)
# Factory parameters
p0.factory.setLifespanBase(2.0000)
p0.factory.setLifespanSpread(1.0000)
p0.factory.setMassBase(10.0000)
p0.factory.setMassSpread(5.0000)
p0.factory.setTerminalVelocityBase(4000.0000)
p0.factory.setTerminalVelocitySpread(0.0000)
# Point factory parameters
# Renderer parameters
p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
p0.renderer.setUserAlpha(0.22)
# Sprite parameters
#print(__import__("g").texture)
p0.renderer.setTexture(__import__("g").texture)
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
