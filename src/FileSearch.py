"""
File searching tools

Non-reactive
"""
from Types import *
from panda3d.core import Filename


def fileSearch(file, libDir = None, exts = []):
    """
    Searches for given file in path
    """
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


def findTexture(fileName):
    """
    Finds given texture file in path
    """
    tFile = fileSearch(fileName, "textures", ["jpg", "png", "jpeg"])
    if tFile is None:
        tFile = fileSearch(g.pandaPath + "/textures/default.jpg")
    return loader.loadTexture(tFile)


def findSound(fileName):
    """
    Finds given sound file in path
    """
    return fileSearch(fileName, "sounds", ["wav", "mp3"])
