"""
File searching tools

Non-reactive
"""
from types import *
from panda3d.core import Filename

"""
Searches for given file in path
"""
def fileSearch(file, libDir = None, exts = []):
    f1 = Filename.expandFrom(file)
    if f1.exists():        
        return f1
    for e in exts:
        f1.setExtension(e)
        if f1.exists():
            return f1
    if libDir is not None:
        f2 = Filename.expandFrom(g.pandaPath + "/" + libDir + "/" + file)
        if f2.exists():
            return f2
        for e in exts:
            f2.setExtension(e)
            if f2.exists():
                return f2
    return None

"""
Finds given texture file in path
"""
def findTexture(fileName):
    tFile = fileSearch(fileName, "textures", ["jpg", "png", "jpeg"])
    if tFile is None:
        tFile = fileSearch(g.pandaPath + "/textures/default.jpg")
    return loader.loadTexture(tFile)

"""
Finds given sound file in path
"""
def findSound(fileName):
    return fileSearch(fileName, "sounds", ["wav", "mp3"])
