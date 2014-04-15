
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

pandaParameters = { "localSize" : 0.05,
                    "localPosition" : P3( 0, 200, 0).start(),
                    "localOrientation" : HPR(0, 0, 0).start()}
def pandaModel(fileName = None, size = None, hpr = None, position = None):
    res = PandaModel(  fileName, size, hpr, position)
    return res
class PandaModel(Proxy):
    def __init__(self, fileName, size, hpr, position):
        Proxy.__init__(self, name = "Panda"+str(Globals.nextModelId), updater = updater)
        self._mFile = FileSearch.fileSearch(fileName, "models",["egg"])
        print "File Name: "+str(fileName)
        print "File Path: "+str(pandaPath)
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
                self._mParams = FileIO.loadDict(mParamFile, defaultModelParameters)
            else:
                print "No .model for " + str(fileName)
                self._mParams = defaultModelParameters
            parameterCache[fileName] = self._mParams
        self._pandaModel = loader.loadModel(self._mFile)
        Globals.nextModelId = Globals.nextModelId + 1
        self._onScreen = False
        self._size=pandaParameters['localSize']
        self._hpr=pandaParameters['localOrientation']
        self._position=pandaParameters['localPosition']
        self.size = Lift0F(1)
        self.position = P3(1,1,1)
        self.hpr = HPR(0,0,0)
        if position is not None:
            self.position = position
        if hpr is not None:
            self.hpr = hpr
        if size is not None:
            self.size =size
        showModel(self)#This call needs to move into the updater method. We don't have it working with the engine yet.

def updater(self):
    #These parameters find the static offset which was created during initialization and the current position which is returned by the self.get() method
    p2 = self._position.now()
    p = self.get( "position")
    s = self.get( "size")
    d2 = self._hpr.now()
    d = self.get( "hpr")
    
    #This is the actual updates to position/size/hpr etc.
    self._pandaModel.setScale(s*self._size)
    self._pandaModel.setPos(p.x + p2.x*s,
                            p.y + p2.y*s,
                            p.z + p2.z*s)
                            
     
    self._pandaModel.setHpr(degrees(d.h + d2.h),
                            degrees(d.p + d2.p),
                            degrees(d.r + d2.r))
 
def showModel(self):
    if not self._onScreen:
           self._pandaModel.reparentTo(render)
           self._onScreen = True