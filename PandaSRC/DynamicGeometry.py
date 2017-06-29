
# Todo: add code for surface normals

from panda3d.core import *
from PandaFRP.PandaColor import *
from PandaFRP.PandaNumerics import *

import pythonfrp.Functions as Functions
import pythonfrp.Proxy as Proxy
from PandaFRP import PandaGlobals
from PandaSRC import FileSearch
from PandaSRC import PandaModel
from pythonfrp.Types import *


# This has a lot in common with PandaModel - there should be a super class
# to hold the common code

def geometryUpdater(self):
    #These parameters find the static offset which was created during initialization and the current position which is returned by the self._get() method
    positionNow = self._get("position")
    sizeNow = self._get("size")
    hprNow = self._get( "hpr")
    textureNow = self._get("texture")
    colorNow = self._get("color")

    #print("size signal: "+repr(sizeScalar)+"  offset size: "+repr(sizeOffset))
    self._pandaModel.setScale(sizeNow)
    self._pandaModel.setPos(positionNow.x, positionNow.y, positionNow.z)
    self._pandaModel.setHpr(degrees(hprNow.h),
                            degrees(hprNow.p),
                            degrees(hprNow.r))
    if textureNow != "" and textureNow != self._currentTexture:
        texf = FileSearch.findTexture(textureNow)
        self._currentTexture = textureNow
        #print("The texture is: "+repr(texf))
        self._pandaModel.setTexture(texf, 1)

    if colorNow.a != 0:
        self._pandaModel.setColor(colorNow.toVBase4())
    if self._twoSided:
        sideTwoNow = self._get("sideTwo")
        if sideTwoNow != "" and sideTwoNow != self._currentsideTwo:
            tex = FileSearch.findTexture(sideTwoNow)
            self._currentsideTwo = sideTwoNow
            #print("The texture is: "+repr(texf))
            self._sideTwo._pandaModel.setTexture(tex, 1)
    # This is used to keep the model off the screen until the first update happens
    if not self._onScreen:
           self._reparent(self._parent)
           self._onScreen = True

def getModel(x):
    if hasattr(x, "_pandaModel"):
        x = x._pandaModel
    return x

class GeometryHandle(Proxy.Proxy):
    def __init__(self, object, position=None, hpr=None, size=1, color=None,
                 texture=None, duration = 0, parent = render, name = "gemometry"):
        Proxy.Proxy.__init__(self, name="dynamicGeometry", updater=geometryUpdater,
                       types={"position": p3Type, "hpr": hprType, "size": numType,
                            "color": colorType, "texture": stringType, "sideTwo": stringType})
        self._pandaModel = object
        self._parent = PandaModel.getModel(parent)
        self._name = name + str(PandaGlobals.nextModelId)
        PandaGlobals.nextModelId = PandaGlobals.nextModelId + 1
        self._name = name + str()
        self._onScreen = False
        self._currentTexture = ""
        self._currentsideTwo = ""
        if position is not None:
            self.position = position
        else:
            self.position = P3(0, 0, 0)
        if hpr is not None:
            self.hpr = hpr
        else:
            self.hpr = SHPR(0, 0, 0)
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
        if duration != 0:
            Functions.react(self, Functions.delay(duration), Functions.exitScene)
    def _reparent(self, m):
        self._pandaModel.reparentTo(m)
    def _remove(self):
        if self._pandaModel is not None:
            self._pandaModel.detachNode()

# This creates a model on the fly.  The array of spacePoints and texturePoints have to be the same length.
# The spacePoints contains P3 objects and texturePoints contains P2 objects.
# The triangles array contains triples of points, one for each triangle.
# The color is just a default - either color or texture override this.

def mesh(spacePoints, texturePoints, triangles, c):
#getV3c4t2() means 3-dimensional Vector, 4-dimensional Color and 2-dimensional Texture Coordinates.
# c can be a list of colors, corresponding to the spacePoints
    def zip(space, c):
        i = 0
        res = []
        for p in space:
            if getPtype(c) is colorType:
                res.append((p, c))
            else:
                res.append((p, c[i]))
                i = i + 1
        return res

    format = GeomVertexFormat.getV3c4t2()

#####I believe this provides a link of some sort to the Geom.UHStatic collection of vertices.
#####This seems to be a necessary step to making the shapes appear on the screen.
    vdata = GeomVertexData('name', format, Geom.UHStatic)

    vertex = GeomVertexWriter(vdata, 'vertex')
#    normal = GeomVertexWriter(vdata, 'normal')
    color = GeomVertexWriter(vdata, 'color')
    texcoord = GeomVertexWriter(vdata, 'texcoord')
    for p in zip(spacePoints, c):
        vertex.addData3f(p[0].x, p[0].y, p[0].z)
        color.addData4f(p[1].r, p[1].g, p[1].b, p[1].a)
    for p in texturePoints:
        texcoord.addData2f(p.x, p.y)
    geom = Geom(vdata)
    for triangle in triangles:

    #GeomTriangles contains a number of disconnected triangles, all apparently stored in a big pile.
        prim = GeomTriangles(Geom.UHStatic)

#####This seems to take the points we added in earlier and remove them.
#####Why this is all static, I don't understand.
        prim.addVertex(triangle[0])
        prim.addVertex(triangle[1])
        prim.addVertex(triangle[2])
        prim.closePrimitive()

#Converting the vertices we just retrieved from the collection inside Geom.UHStatic into a node
#####
        geom.addPrimitive(prim)

    node = GeomNode('gnode')
    node.addGeom(geom)

    #Adds the node we've just made into the render path, therefore making it appear on screen.
#####I believe that if we want an actory-thing, this might be the place to do it.

    # nodePath = NodePath(node)
    # Not sure why this goes through render.  It makes the geometry visible too soon.
    # Can't reparent to render in showModel like a real model does.
    nodePath = render.attachNewNode(node)
    nodePath.setTwoSided(True)
    return nodePath

def emptyModel(color = None, position = None, hpr = None, size = None, duration = 0):
    nodePath = mesh([], [], [], white)
    result = GeometryHandle(nodePath, position = position, hpr = hpr, size = size, color = color,
                            texture = None, duration = duration)
    result._twoSided = False
    return result

def triangle(p1, p2, p3, color = None, position = None, hpr = None, size = None, texture = None, texP1 = p2(0, 0), \
    texP2 = p2(1, 0), texP3 = p2(0, 1), sideTwo = None, duration = 0, parent = render):
#checking to ensure that the second argument is an instance of the third argument
    #The first and fourth are for error handling.
    checkType("triangle", "first point", p1, p3Type)
    checkType("triangle", "second point", p2, p3Type)
    checkType("triangle", "third point", p3, p3Type)
    nodePath = mesh([p1, p2, p3], [texP1, texP2, texP3], [[0, 1, 2]], white)
    if (sideTwo is not None):
        nodePath.setTwoSided(False)
        result = GeometryHandle(nodePath, position = position, hpr = hpr, size = size,
                                color = color, texture = texture, parent = parent)
        if sideTwo is not False:
            result.sideTwo = sideTwo
            otherSide = triangle(p2, p1, p3, texture = sideTwo, sideTwo = False, texP1 = texP1, texP2 = texP2, texP3 = texP3, parent = result)
            result._twoSided = True
#            otherSide._reparent(result)
# Not working at the moment!
#            otherSide._pandaModel.reparentTo(result._pandaModel)
            result._sideTwo = otherSide
        else:
            result._twoSided = False
        return result
    result = GeometryHandle(nodePath, position = position, hpr = hpr, size = size, color = color,
                            texture = texture,  duration = duration, parent = parent)
    # result.d.model.setScale(0)
    result._twoSided = False
    return result

def rectangle(p1, p2, p3, color = None, position = None, hpr = None, size = None, texture = None, sideTwo = None,
    texP1 = P2(0, 0), texP2 = P2(1, 0), texP3 = P2(0, 1), texP4 = P2(1, 1), duration = 0, parent = render):
    # If sideTwo is a string, it is interpreted as a file name in the pictures area
    # If sideTwo is False, the texture is one sided (invisible from the back)
    #checking to ensure that the second argument is an instance of the third argument
    #The first and fourth are for error handling.
    checkType("rectangle", "first point", p1, p3Type)
    checkType("rectangle", "second point", p2, p3Type)
    checkType("rectangle", "third point", p3, p3Type)

    p4 = p3 + p2 - p1
    nodePath = mesh([p1, p2, p3, p4], [texP1, texP2, texP3, texP4], [[0, 1, 2], [2, 1, 3]], white)
    if color is None:
        nodePath.setTransparency(True)
    if (sideTwo is not None):
        nodePath.setTwoSided(False)
        result = GeometryHandle(nodePath, position = position, hpr = hpr, size = size,
                                color = color, texture = texture, parent = parent)
        if sideTwo is not False:
            otherSide = rectangle(p2, p1, p4, texture = sideTwo, sideTwo = False,
               parent = result, texP1 = texP1, texP2 = texP2, texP3 = texP3, texP4 = texP4)
            result.sideTwo = sideTwo
            result._twoSided = True
            result._sideTwo = otherSide
        else:
            result._twoSided = False
        return result
    result = GeometryHandle(nodePath, position = position, hpr = hpr, size = size,
                                color = color, texture = texture, parent = parent, duration = duration)
    result._twoSided = False
    #result.d.model.setScale(0)  # Hack - this is rendered too soon and we get 1 frame before update.  This keeps the model invisible
    #                            # until the first refresh
    return result

def unitSquare(**a):
    return rectangle(P3(-1, 0, -1), P3(1, 0, -1), P3(-1, 0, 1), **a)

def photoWheel(p, radius = 1.2, height = 1.2, **a):
    total = len(p)
    center = emptyModel(**a)
    for i in range(total):
      r = (2*pi/total)*i
      r2 = (2*pi/total)*(i+1)
      p1 = p3c(radius, r, height)
      p2 = p3c(radius, r, 0)
      p3 = p3c(radius, r2, 0)
      ph = rectangle(p2,p3,p1, texture = p[i], parent = center)
    return center

def cube(t1, t2, t3, t4, t5, t6, **a):
    center = emptyModel(**a)
    v1 = P3(1,1,1)
    v2 = P3(1,1,-1)
    v3 = P3(1, -1, 1)
    v4 = P3(1, -1, -1)
    v5 = P3(-1,1,1)
    v6 = P3(-1,1,-1)
    v7 = P3(-1, -1, 1)
    v8 = P3(-1, -1, -1)
    f1 = rectangle(v8, v4, v7, texture = t1, parent = center)
    f2 = rectangle(v4, v2, v3, texture = t2, parent = center)
    f3 = rectangle(v2, v6, v1, texture = t3, parent = center)
    f4 = rectangle(v6, v8, v5, texture = t4, parent = center)
    f5 = rectangle(v7, v3, v5, texture = t5, parent = center)
    f6 = rectangle(v2, v6, v4, texture = t6, parent = center)
    return center

def tetra(t1, t2, t3, t4, v1 = P3(-1, -1, -1), v2 = P3(1,-1,-1),v3 = P3(0, 1, -1), v4 = P3(0, 0, 1),  **a):
    center = emptyModel(**a)
    f1 = triangle(v1, v2, v4, texture = t1, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1), parent = center)
    f2 = triangle(v2, v3, v4, texture = t2, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1), parent = center)
    f3 = triangle(v3, v1, v4, texture = t3, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1), parent = center)
    f4 = triangle(v1, v2, v3, texture = t4, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1), parent = center)
    return center

#
# This creates a single object with subobjects for each piece of the picture
#
# To assemble a picture send each fragment to p3(0,0,0)

def slicePicture(p,columns = 1, rows = 1, **a):
    center = emptyModel(**a)
    res = []
    xsz = 1.0/columns
    ysz = 1.0/rows
    xi = 0
    for x in range(columns):
        yi = 0
        for y in range(rows):
            ll = P2(x*xsz, y*ysz)
            lr = P2((x+1)*xsz, y*ysz)
            ul = P2(x*xsz, (y+1)*ysz)
            ur = P2((x+1)*xsz, (y+1)*ysz)
            r = rectangle(P3(2*x*xsz-1, 0, 2*y*ysz-1), (P3(2*(x+1)*xsz-1, 0, 2*y*ysz-1)),
                          P3(2*x*xsz-1, 0, 2*(y+1)*ysz-1), texP1 = ll, texP2 = lr, texP3 = ul, texP4 = ur,
                          texture = p, parent = center)
            r._location = P3(2*(x+.5)*xsz-1, 0, 2*(y+.5)*ysz-1)
            r._x = xi
            r._y = yi
            yi = yi + 1
            res.append(r)
        xi = xi + 1
    return (center, res)

#
# This creates fragment objects that are not parented to anything
# Spatial locations are stored in the fragments
# This isn't smart enough to match the aspect of the picture to the generated pieces.
# To assemble a picture send each fragment to "_location"

def blastPicture(p,columns = 1, rows = 1, size = 1, **a):
    res = []
    xsz = 1.0/columns
    ysz = 1.0/rows
    xi = 0
    for x in range(columns):
        yi = 0
        for y in range(rows):
            ll =  P2(x*xsz, y*ysz)
            lr =  P2((x+1)*xsz, y*ysz)
            ul =  P2(x*xsz, (y+1)*ysz)
            ur =  P2((x+1)*xsz, (y+1)*ysz)
            r = rectangle(size * P3(-xsz, 0, -ysz), size * P3(xsz, 0, -ysz), size * P3(-xsz, 0, ysz),
                          texP1 = ll, texP2 = lr, texP3 = ul, texP4 = ur, texture = p)
            r._location = size*P3(2*(x+.5)*xsz-1, 0, 2*(y+.5)*ysz-1)
            r._x = xi
            r._y = yi
            yi = yi + 1
            res.append(r)
        xi = xi + 1
    return res


'''
def surface(f, xmin = -10, xmax = 10, ymin = -10, ymax = 10, slices = 40, dx = None, dy = None,
            color = None, position = None, hpr = None, size = None, texture = None, delta = 0.001):
    def surfaceNormal(x, y):
        p = SP3(x, y, f(x, y))
        p1 = SP3(x + delta, y, f(x + delta, y))
        p2 = SP3(x, y + delta, f(x, y + delta))
        a = p1 - p
        b = p2 - p
        return normP3(crossProduct(a, b))

    def parX(x, y):
        return (f(x + delta, y)-f(x, y)) / delta

    def parY(x, y):
        return (f(x, y + delta)-f(x, y)) / delta
    if dx is None:
        dx = (xmax - xmin)/(slices*1.0)
    if dy is None:
        dy = (ymax - ymin)/(slices*1.0)
    if getPType(texture)==ColorType:
        color = texture
        texture = None
    ver = []
    tex = []
    tri = []
    p = 0
    row = int((ymax - ymin)/dy)
    col = int((xmax - xmin)/dx)
    for c in range(col + 1):
        tx = c / (col + 0.0)
        sx = tx * (xmax- xmin) + xmin
        for r in range(row + 1):
            ty = r / (row + 0.0)
            sy = ty * (ymax - ymin) + ymin
            v = SP3(sx, sy, f(sx, sy))
            t = SP2(tx, ty)
            ver.append(v)
            tex.append(t)
            if r < row and c < col:
                t1 = [p, p + 1, p + col + 1]
                t2 = [p + 1, p + col + 1, p + col + 2]
                tri.extend([t1, t2])
            p = p + 1
    nodePath = mesh(ver, tex, tri, white)
    result = GeometryHandle(nodePath, position, hpr, size, color, texture)
    result.d.twoSided = False
    result.d.model.setScale(0)
    result.f = static(lift(f, "Surface function", numType2, numType))
    result.normal = static(lift(surfaceNormal, "Surface Normal", numType2, numType))
    result.dx = static(lift(parX, "X Partial", numType2, numType))
    result.dy = static(lift(parY, "Y Partial", numType2, numType))
    result.sNormal = static(surfaceNormal)
    result.xmin = static(xmin)
    result.xmax = static(xmax)
    result.ymin = static(ymin)
    result.ymax = static(ymax)
    return result
'''
