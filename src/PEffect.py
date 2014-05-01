# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class PEffect(Proxy):

    pid = 1 #what is this? 
    def __init__(self, particleFn, name = 'particleEffect', 
               hpr = None, position = None,
                size = None,
                duration = 0, ** a): 

        Proxy.__init__(self, name = name, duration = duration, types = {"position":(positionType, P3(0,0,0)), "size":(sizeType, size(1))})

        #pathname = "/lib/panda/lib/lib-original/particles/"
        base.enableParticles() #should this bbe here? 
        p = ParticleEffect()
        particleFn(p, a)
        self.d.model = p  # ???
        p.reparentTo(render)
        p.start()
        
def updater(self):
    p = self.d.model
    Proxy.update(self)


