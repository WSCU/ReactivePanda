from pythonfrp.StaticNumerics import *
from pythonfrp.Factory import *
from pythonfrp.Types import *
from pythonfrp.Numerics import *
from PandaStaticNumerics import *
from SHPR import *
from Color import Color, colorHSL



hpr = lift("hpr", SHPR, types=[numType, numType, numType], outType=hprType)
HPR = hpr

getH = lift("getH", lambda v:v.h, [hprType], numType)
getP = lift("getP", lambda v:v.p, [hprType], numType)
getR = lift("getR", lambda v:v.r, [hprType], numType)

getUp = lift("getUp", lambda hpr:getUpHPR(hpr), [hprType], p3Type)

color    = lift("rgb color", Color, [numType, numType, numType], colorType)
colora   = lift("rgb color", Color, [numType, numType, numType, numType], colorType)
colorhsl = lift("hsl color", colorHSL, [numType, numType, numType], colorType)

getR     = lift("getR", lambda x: x.r, [colorType], numType)
getG     = lift("getG", lambda x: x.g, [colorType], numType)
getB     = lift("getB", lambda x: x.b, [colorType], numType)

getCH     = lift("getH", lambda x: x.getH(), [colorType], numType)
getCS     = lift("getS", lambda x: x.getS(), [colorType], numType)
getCL     = lift("getL", lambda x: x.getL(), [colorType], numType)

P3toHPR = lift("P3toHPR", sP3toHPR, [p3Type], hprType)
p3ToHpr = P3toHPR

HPRtoP3 = lift("HPRtoP3", sHPRtoP3, [hprType], p3Type)
hprToP3 = HPRtoP3


hprType.encoder = lambda p: encodeNums(p.h, p.p, p.r)
hprType.decoder = lambda s: decodeNums(s, hpr)
