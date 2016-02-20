from Light import *
from PandaFRP import PandaEngine

#"Sanity check" testing scenarios will go here

#place panda on the screen 
#b = panda(position = P3(2,0,2), hpr = HPR(0,-.75,time), size = .5)
#b = panda(position = P3(0,0,0))

#p = panda(position = P3(integral(1), integral(1), integral(1)))
#a = ambientLight(color24(100,100,100))
p = pointLight(color24(100,100,100))
PandaEngine.engine(0)
