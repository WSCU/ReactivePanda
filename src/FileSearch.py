# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from types import *
from panda3d.core import Filename

file = "C:\\School\\Visual Programming\\test.csv"
def fileSearch(file, libDir = None, exts = []):

    f1 = Filename.expandFrom(file)
    if f1.exists():
 #       print "Local file"
        print(f1)
        return f1

    for e in exts:
        f1.setExtension(e)
        if f1.exists():
 #           print "Extension: " + e
            return f1
    if libDir is not None:
        f2 = Filename.expandFrom(g.pandaPath + "/" + libDir + "/" + file)
 #       print "Searching library"
        if f2.exists():
            return f2
        for e in exts:
            f2.setExtension(e)
            if f2.exists():
                return f2
    return None

fileSearch(file)