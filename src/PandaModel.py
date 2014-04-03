
# This defines an object that appears on the screen whose representation is obtained from a
# 3-D model in an egg file from the Panda-3D engine.  These have the following reactive parameters:
#   position  P3      location in 3-space
#   hpr       HPR     orientation in 3-space
#   scale     scalar  relative size (1 = unit cube)
#   color     Color   dynamic texture (None = model skin, otherwise = color of object)

from direct.actor import Actor
import direct.directbase.DirectStart
from panda3d.core import Filename
from Engine import *
from Signal import *
from Proxy import *
from Numerics import *
import Globals
import FileIO
import FileSearch

# This fills in all of the defaults
parameterCache = {}
"""
defaultModelParameters = {"localPosition" : P3(0,0,0),
                          "localSize" : 1,
                          "localOrientation" : HPR(0,0,0),
                          "joints" : [],
                          "animations" : None,
                          "defaultAnimation" : None,
                          "frame" : None,
                          "cRadius" : 1,
                          "cFloor" : 0,
                          "cTop" : 1,
                          "cType" : "cyl"}

modelParameters = {"localPosition" : P3Type,
                   "localSize" : numType,
                   "localOrientation" : HPRType,
                   "joints" : StringListType,
                   "animations" : StringListType,
                   "defaultAnimation" : stringType,
                   "frame" : numType,
                   "cRadius" : numType,
                   "cFloor" : numType,
                   "cTop" : numType,
                   "cType" : stringType}
"""
pandaParameters = { "localSize" : 0.00178,
                    "localPosition" : P3( 0, 0.21, 0),
                    "localOrientation" : HPR(0, 0, 0)}
def pandaModel(fileName = None, size = None, hpr = None, position = None):
    res = PandaModel(size, hpr, position, fileName)
    return res
class PandaModel(Proxy):
    def __init__(self, fileName, size, hpr, position):
        self._pandaModel = PandaModel
        Proxy.__init__(self, name = Globals.nextModelId, updater = updater)
        #mFile = fileSearch(fileName, "models",["egg"])
        mFile = Filename("/c/Panda3D-1.8.1/models/panda-model.egg.pz")
        winfile = mFile.toOsSpecific()
        print "File Path: " + repr(mFile)
        """
        if mFile is None:
            print "Can't find model" + str(fileName)
            mFile = Filename("panda-model.egg.pz")
            mParams = pandaParameters
        elif fileName in parameterCache:
            mParams = parameterCache[fileName]
            
        else:
            mParamFile = Filename(mFile)
            mParamFile.setExtension("model")
            if mParamFile.exists():
                mParams = loadDict(mParamFile, modelParameters, defaultModelParameters)
            else:
                print "No .model for " + str(fileName)
                mParams = defaultModelParameters
            parameterCache[fileName] = mParams
            """
            
        
        self._pandaModel = loader.loadModel(mFile)
        
        Globals.nextModelId = Globals.nextModelId + 1
        self._signals['size']=maybeLift(size)
        self._signals['hpr']=maybeLift(hpr)
        self._signals['position']=maybeLift(position)
        self._onScreen=False
        
def updater(self, sigs):
    self._pandaModel.setSize(sigs.size)
    self._pandaModel.setHpr(sigs.hpr)
    self._pandaModel.setPos(sigs.position)
    
def showModel(self):
    if not self._onScreen:
        self._pandaModel.reparentTo(render)
        self._onScreen = True
