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
from Functions import degrees
from StaticNumerics import pi
from Globals import pandaPath
import FileIO
import FileSearch

# This fills in all of the defaults
parameterCache = {}
defaultModelParameters = {"localPosition" : SP3(0,0,0),
                          "localSize" : .05,
                          "localOrientation" : SHPR(0,.25,0),
                          "joints" : [],
                          "animations" : None,
                          "defaultAnimation" : None,
                          "frame" : None,
                          "cRadius" : 1,
                          "cFloor" : 0,
                          "cTop" : 1,
                          "cType" : "cyl"}

pandaParameters = { "localSize" : 0.05,
                    "localPosition" : SP3( 0, 200, 0),
                    "localOrientation" : SHPR(0, 0, 0)}
def pandaModel(fileName = None, size = None, hpr = None, position = None):
    res = PandaModel(  fileName, size, hpr, position)
    return res
class PandaModel(Proxy):
    def __init__(self, fileName, size, hpr, position):
        Proxy.__init__(self, name = str(fileName)+"-gID: "+str(Globals.nextModelId), updater = updater)
        self._mFile = FileSearch.fileSearch(fileName, "models",["egg"])
        #print "Object Name: "+ str(fileName)+"-gID: "+str(Globals.nextModelId);
        if self._mFile is None:
            print "Can't find model " + repr(fileName)
            self._mFile = Filename("/c/Panda3D-1.8.1/models/"+fileName)
            self._mParams = pandaParameters
        #self._mFile = Filename("/c/Panda3D-1.8.1/models/"+fileName)
        #print "File Path: " + repr(mFile)
        elif fileName in parameterCache:
            self._mParams = parameterCache[fileName]
        else:
            mParamFile = Filename(self._mFile)
            print repr(mParamFile)
            mParamFile.setExtension("model")
            if mParamFile.exists():
                self._mParams = FileIO.loadDict(mParamFile, defaults = defaultModelParameters)
            else:
                print "No .model for " + str(fileName)
                self._mParams = defaultModelParameters
            parameterCache[fileName] = self._mParams
        self._pandaModel = loader.loadModel(self._mFile)
        Globals.nextModelId = Globals.nextModelId + 1
        self._onScreen = False
        self._size=self._mParams['localSize']
        self._hpr=self._mParams['localOrientation']
        self._position=self._mParams['localPosition']
        self.size = Lift0F(1)
        self.position = P3(1,1,1)
        self.hpr = HPR(0,0,0)
        if position is not None:
            self.position = position
        if hpr is not None:
            self.hpr = hpr
        if size is not None:
            self.size = Lift0F(size)
        showModel(self)#This call needs to move into the updater method. We don't have it working with the engine yet.

def updater(self):
    #These parameters find the static offset which was created during initialization and the current position which is returned by the self.get() method
    positionOffset = self._position
    positionNow = self.get("position")
    sizeScalar = self.get("size")
    hprOffset = self._hpr
    hprNow = self.get( "hpr")
    
    #This is the actual updates to position/size/hpr etc.
    if Globals.eventSignals is not None: 
            for signal in Globals.events:
                print repr(signal)
    self._pandaModel.setScale(sizeScalar*self._size)
    self._pandaModel.setPos(positionNow.x + positionOffset.x*sizeScalar,
                            positionNow.y + positionOffset.y*sizeScalar,
                            positionNow.z + positionOffset.z*sizeScalar)
                            
     
    self._pandaModel.setHpr(degrees(hprNow.h + hprOffset.h),
                            degrees(hprNow.p + hprOffset.p),
                            degrees(hprNow.r + hprOffset.r))
 
def showModel(self):
    if not self._onScreen:
           self._pandaModel.reparentTo(render)
           self._onScreen = True
