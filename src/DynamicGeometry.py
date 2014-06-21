
# Todo: add code for surface normals

import Globals

from Types import *
import PandaModel
import Proxy
from Numerics import *
from Color import *
from panda3d.core import *
import FileSearch
import Types


# This has a lot in common with PandaModel - there should be a super class
# to hold the common code

def geometryUpdater(self):
    #These parameters find the static offset which was created during initialization and the current position which is returned by the self._get() method
    positionNow = self._get("position") + p3(0,0,0) # to make sure we do not get a zero object
    sizeNow = self._get("size") + 0
    hprNow = self._get( "hpr") + hpr(0,0,0)
    textureNow = self._get("texture")
    colorNow = self._get("color")

    #print "size signal: "+repr(sizeScalar)+"  offset size: "+repr(sizeOffset)
    self._pandaModel.setScale(sizeNow)
    self._pandaModel.setPos(positionNow.x, positionNow.y, positionNow.z)
    self._pandaModel.setHpr(degrees(hprNow.h),
                            degrees(hprNow.p),
                            degrees(hprNow.r))
    if textureNow != "" and textureNow != self._currentTexture:
        texf = FileSearch.findTexture(textureNow)
        self._currentTexture = textureNow
        #print "The texture is: "+repr(texf)
        self._pandaModel.setTexture(texf, 1)

    if colorNow.a != 0:
        self._pandaModel.setColor(colorNow.toVBase4())
    if self._twoSided:
        side2now = self._get("side2")
        if texture != "" and texture != self._currentSide2:
            tex = FileSearch.findTexture(side2now)
            self._currentSide2 = tex
            #print "The texture is: "+repr(texf)
            self._sideTwo.setTexture(tex, 1)
    # This is used to keep the model off the screen until the first update happens
    if not self._onScreen:
           self._pandaModel.reparentTo(self._parent)
           self._onScreen = True

    

class GeometryHandle(Proxy.Proxy):
    def __init__(self, object, position=None, hpr=None, size=1, color=None, texture=None, extraUpdates=lambda x:x, duration = 0):
        Proxy.Proxy.__init__(self, name="dynamicGeometry", updater=geometryUpdater,
                       types={"position": p3Type, "hpr": hprType, "size": numType,
                            "color": colorType, "texture": stringType, "side2": stringType})
        self._pandaModel = object
        Globals.nextModelId = Globals.nextModelId + 1
        self._onScreen = False
        self._parent = render
        self._currentTexture = ""
        self._currentSide2 = ""
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
    normal = GeomVertexWriter(vdata, 'normal')
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
    result = GeometryHandle(nodePath, position, hpr, size, color, None)
    return result

def triangle(p1, p2, p3, color = None, position = None, hpr = None, size = None, texture = None, texP1 = P2(0, 0), \
    texP2 = P2(1, 0), texP3 = P2(0, 1), side2 = None, duration = 0):
#checking to ensure that the second argument is an instance of the third argument
    #The first and fourth are for error handling.
    checkType("triangle", "first point", p1, p3Type)
    checkType("triangle", "second point", p2, p3Type)
    checkType("triangle", "third point", p3, p3Type)
    nodePath = mesh([p1, p2, p3], [texP1, texP2, texP3], [[0, 1, 2]], white)
    if (side2 is not None):
        nodePath.setTwoSided(False)
        result = GeometryHandle(nodePath, position, hpr, size, color, texture)
        if side2 is not False:
            otherSide = triangle(p2, p1, p3, texture = side2, side2 = False, texP1 = texP1, texP2 = texP2, texP3 = texP3)
            otherSide.reparentTo(result)
            result._twoSided = True
            result._sideTwo = otherSide
        return result
    result = GeometryHandle(nodePath, position, hpr, size, color, texture, duration = duration)
    result._twoSided = False
    # result.d.model.setScale(0)
    return result

def rectangle(p1, p2, p3, color = None, position = None, hpr = None, size = None, texture = None, side2 = None,
    texP1 = P2(0, 0), texP2 = P2(1, 0), texP3 = P2(0, 1), texP4 = P2(1, 1), duration = 0):
    # If side2 is a string, it is interpreted as a file name in the pictures area
    # If side2 is False, the texture is one sided (invisible from the back)
    #checking to ensure that the second argument is an instance of the third argument
    #The first and fourth are for error handling.
    checkType("rectangle", "first point", p1, p3Type)
    checkType("rectangle", "second point", p2, p3Type)
    checkType("rectangle", "third point", p3, p3Type)

    p4 = p3 + p2 - p1
    nodePath = mesh([p1, p2, p3, p4], [texP1, texP2, texP3, texP4], [[0, 1, 2], [2, 1, 3]], white)
    if (side2 is not None):
        nodePath.setTwoSided(False)
        result = GeometryHandle(nodePath, position, hpr, size, color, texture)
        if side2 is not False:
            otherSide = rectangle(p2, p1, p4, texture = side2, side2 = False, texP1 = texP1, texP2 = texP2, texP3 = texP3, texP4 = texP4)
            otherSide.reparentTo(result)
            result._twoSided = True
            result._side2 = otherSide
        return result
    result = GeometryHandle(nodePath, position, hpr, size, color, texture, duration = duration)
    result._twoSided = False
    #result.d.model.setScale(0)  # Hack - this is rendered too soon and we get 1 frame before update.  This keeps the model invisible
    #                            # until the first refresh
    return result
'''
def unitSquare(**a):
    return rectangle(P3(-1, 0, -1), P3(1, 0, -1), P3(-1, 0, 1), **a)

def photoWheel(p, radius = 1.2, height = 1.2, **a):
    total = len(p)
    center = emptyModel(**a)
    for i in range(total):
      r = (2*pi/total)*i
      r2 = (2*pi/total)*(i+1)
      p1 = P3C(radius, r, height)
      p2 = P3C(radius, r, 0)
      p3 = P3C(radius, r2, 0)
      ph = rectangle(p2,p3,p1, texture = p[i])
      ph.reparentTo(center)
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
    f1 = rectangle(v8, v4, v7, texture = t1)
    f2 = rectangle(v4, v2, v3, texture = t2)
    f3 = rectangle(v2, v6, v1, texture = t3)
    f4 = rectangle(v6, v8, v5, texture = t4)
    f5 = rectangle(v7, v3, v5, texture = t5)
    f6 = rectangle(v2, v6, v4, texture = t6)
    f1.reparentTo(center)
    f2.reparentTo(center)
    f3.reparentTo(center)
    f4.reparentTo(center)
    f5.reparentTo(center)
    f6.reparentTo(center)
    return center


def tetra(t1, t2, t3, t4, v1 = P3(-1, -1, -1), v2 = P3(1,-1,-1),v3 = P3(0, 1, -1), v4 = P3(0, 0, 1),  **a):
    center = emptyModel(**a)
    f1 = triangle(v1, v2, v4, texture = t1, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1))
    f2 = triangle(v2, v3, v4, texture = t2, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1))
    f3 = triangle(v3, v1, v4, texture = t3, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1))
    f4 = triangle(v1, v2, v3, texture = t4, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1))
    f1.reparentTo(center)
    f2.reparentTo(center)
    f3.reparentTo(center)
    f4.reparentTo(center)
    return center
#
# This creates a single object with subobjects for each piece of the picture
#

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
                          P3(2*x*xsz-1, 0, 2*(y+1)*ysz-1), texP1 = ll, texP2 = lr, texP3 = ul, texP4 = ur, texture = p)
            r.reparentTo(center)
            r.location = static(P3(2*(x+.5)*xsz-1, 0, 2*(y+.5)*ysz-1))
            r.x = static(xi)
            r.y = static(yi)
            yi = yi + 1
            res.append(r)
        xi = xi + 1
    return (center, res)

#
# This creates fragment objects that are not parented to anything
# Spatial locations are stored in the fragments
# This isn't smart enough to match the aspect of the picture to the generated pieces.


def blastPicture(p,columns = 1, rows = 1, **a):
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
            r = rectangle(P3(-xsz, 0, -ysz), P3(xsz, 0, -ysz), P3(-xsz, 0, ysz),
                          texP1 = ll, texP2 = lr, texP3 = ul, texP4 = ur, texture = p)
            r.location = static(P3(2*(x+.5)*xsz-1, 0, 2*(y+.5)*ysz-1))
            r.x = static(xi)
            r.y = static(yi)
            yi = yi + 1
            res.append(r)
        xi = xi + 1
    return res



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