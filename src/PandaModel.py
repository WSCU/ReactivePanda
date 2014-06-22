
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
from StaticNumerics import pi, degrees
import Globals
import FileIO
import FileSearch
import Functions
from Color import *

# This fills in all of the defaults
parameterCache = {}
defaultModelParameters = {"localPosition" : SP3(0,0,0),
                          "localSize" : 1,
                          "localOrientation" : SHPR(0,0,0),
                          "joints" : [], # jointed models not currently supported
                          "animations" : None,
                          "defaultAnimation" : None,
                          "frame" : None,
                          "cRadius" : 1,
                          "cFloor" : 0,
                          "cTop" : 1,
                          "cType" : "cyl"}

def getModel(x):
    if hasattr(x, "_pandaModel"):
        x = x._pandaModel
    return x

def pandaModel(fileName = None, name = "PandaModel", size = None, hpr = None, position = None, tag = [], color = None, texture = None, parent = render, duration = 0):
    return PandaModel(  fileName, size, hpr, position, tag, color, texture, name, parent, duration)

class PandaModel(Proxy):
    def __init__(self, fileName, size, hpr, position, tag, color, texture, name, parent, duration):
        Proxy.__init__(self, name = str(name) + ":" + str(Globals.nextModelId), updater = modelUpdater,
                             types = {"position": p3Type, "hpr": hprType , "size": numType,
                                      "color": colorType, "texture": stringType})
        modelTypes = {"localOrientation": hprType, "localSize": numType, "localPosition": p3Type,
                      "cRadius": numType, "cType": stringType, "cFloor": numType, "cTop": numType}
        #(p3Type, SP3(0,0,0)), "hpr": (hprType, SHPR(0,0,0)), "size": (numType, 1)})
        Globals.nextModelId = Globals.nextModelId + 1
        self._parent = getModel(parent)
        self._mFile = FileSearch.fileSearch(fileName, "models",["egg"])
        #print "Object Name: "+ str(fileName)+"-gID: "+str(Globals.nextModelId);
        if type(tag) == type("s"):
            collections = [tag]
        else:
            collections = tag
        self._collections = collections
        if fileName in parameterCache:
            self._mParams = parameterCache[fileName]
        elif self._mFile is None:
            print "Can't find model " + repr(fileName) #should substitute pandafor unknown models
        #self._mFile = Filename("/c/Panda3D-1.8.1/models/"+fileName)
        #print "File Path: " + repr(mFile)
        else:
            mParamFile = Filename(self._mFile)
            #print repr(mParamFile)
            mParamFile.setExtension("model")
            if mParamFile.exists():
                self._mParams = FileIO.loadDict(mParamFile,types = modelTypes,  defaults = defaultModelParameters)
            else:
                print "No .model for " + str(fileName)
                self._mParams = defaultModelParameters
            parameterCache[fileName] = self._mParams
        self._pandaModel = loader.loadModel(self._mFile)
        self._onScreen = False
        self._size=self._mParams['localSize']
        self._hpr=self._mParams['localOrientation']
        self._position=self._mParams['localPosition']
        self._cRadius = float(self._mParams['cRadius'])
        self._cType = self._mParams['cType']
        self._cFloor = float(self._mParams['cFloor'])
        self._cTop = float(self._mParams['cTop'])
        self._currentTexture = ""
        self._onscreen = False   # This defers the reparenting until the model has been updated the first time
        self._parent = parent
        if position is not None:
            self.position = position
        else:
            self.position = P3(0,0,0)
        if hpr is not None:
            self.hpr = hpr
        else:
            self.hpr = SHPR(0,0,0)
        if size is not None:
            self.size = size
        else:
            self.size = 1
        if texture is not None:
            self.texture = texture
        else:
            self.texture = ""
        if color is not None:
            self.color = color
        else:
            self.color = noColor
        for tag in collections:
            if tag not in Globals.collections:
                Globals.collections[tag] = [self]
            Globals.collections[tag].append(self)

        #Get saved reaction functions for this collection
        for t, v in Globals.collectionReactions.items():
            for tag in collections:
                if tag in v:
                    for args in v[tag]:
                        getattr(Functions, t)(self, args[0], what = args[1])
        if duration > 0:
            react(self, delay(duration), exitScene)

    def _remove(self):
            if self._pandaModel is not None:
                self._pandaModel.detachNode()
            for c in self._collections:
                old = Globals.collections[c]
                Globals.collections[c] = [x for x in old if x is not self]

    def _reparent(self, m):
        self._pandaModel.reparentTo(m)
    def _touches(self, handle, trace = False):
        if trace:
           print "Touch: " + repr(self) + " (" + self._cType + ") " + repr(handle) + " (" + handle._cType + ")"
        #print (repr(self._cRadius))
        #print (repr(self.get("size")))
        mr = self._cRadius * self._get("size")
        mp = self._get("position") + p3(0,0,0)
        yr = handle._cRadius*handle._get("size")
        yp = handle._get("position") + p3(0,0,0)
        if trace:
            print repr(mp) + " [" + repr(mr) + "] " + repr(yp) + " [" + repr(yr) + "]"
        if self._cType == "sphere":
            if handle._cType == "sphere":
                return absP3(subP3(mp, yp)) < mr + yr
            elif handle._cType == "cyl": # Test if the x,y points are close enough. This treats the sphere as a cylinder
                d = absP2(subP2(P2(mp.x, mp.y), P2(yp.x, yp.y)))
                if d > mr + yr:
                    return False
                else:
                    cb = yp.z + handle._get("size")*handle._cFloor
                    ct = yp.z + handle._get("size")*handle._cTop
                    sb = mp.z-mr
                    st = mp.z+mr
                    # print str(cb) + " " + str(ct) + " " + str(sb) + " " + str(st)
                    if ct > sb and cb < st:
                        return True
                    else:
                        return False
        elif self._cType == "cyl":
            if handle._cType == "sphere":
                d = absP2(subP2(P2(mp.x, mp.y), P2(yp.x, yp.y)))
                # print "c to s (dist = " + str(d) + ")"
                if d > mr + yr:
                    return False
                else:
                    cb = mp.z + self._get("size")*self._cFloor
                    ct = mp.z + self._get("size")*self._cTop
                    sb = yp.z-yr
                    st = yp.z+yr
                    # print str(cb) + " " + str(ct) + " " + str(sb) + " " + str(st)
                    return ct > sb and cb < st
            elif handle._cType == "cyl":
                # print str(mp.x) + " , " + str(mp.y)
                d = absP2(subP2(P2(mp.x, mp.y), P2(yp.x, yp.y)))
                if trace:
                    print "c to c (dist = " + str(d) + ") " + str(mr+yr)
                if d > mr + yr:
                    return False
                else:
                    res = self._cTop + mp.z > handle._cFloor + yp.z and self._cFloor + mp.z < handle._cTop + yp.z
                    if trace:
                        print "Result: " + str(res) + " " + str((self._cTop, mp.z, handle._cFloor, yp.z, self._cFloor, handle._cTop))
                    #print ("*****"+repr(res))
                    return res

def modelUpdater(self):
    #These parameters find the static offset which was created during initialization and the current position which is returned by the self._get() method
    positionOffset = self._position
    positionNow = self._get("position") + p3(0,0,0) # to make sure we do not get a zero object
    sizeScalar = self._get("size") + 0
    sizeOffset = self._size
    hprOffset = self._hpr

    hprNow = self._get( "hpr") + hpr(0,0,0)

    #print str(positionNow) + " " + str(positionOffset) + " " + str(hprNow)
    #This is the actual updates to position/size/hpr etc.
    #if Globals.eventSignals is not None:
    #        for signal in Globals.events:
    #            print repr(signal)


    #print "size signal: "+repr(sizeScalar)+"  offset size: "+repr(sizeOffset)
    self._pandaModel.setScale(sizeScalar*sizeOffset)
    self._pandaModel.setPos(positionNow.x + positionOffset.x*sizeScalar,
                            positionNow.y + positionOffset.y*sizeScalar,
                            positionNow.z + positionOffset.z*sizeScalar)

    self._pandaModel.setHpr(degrees(hprNow.h + hprOffset.h),
                            degrees(hprNow.p + hprOffset.p),
                            degrees(hprNow.r + hprOffset.r))
    texture = self._get("texture")
    if texture != "" and texture != self._currentTexture:
        texf = FileSearch.findTexture(texture)
        self._currentTexture = texture
        #print "The texture is: "+repr(texf)
        self._pandaModel.setTexture(texf, 1)
    color = self._get("color")
    if color.a != 0:
        self._pandaModel.setColor(color.toVBase4())
    # This is used to keep the model off the screen until the first update happens
    if not self._onScreen:
           self._reparent(self._parent)
           self._onScreen = True
