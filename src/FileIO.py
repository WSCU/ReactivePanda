# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
#import g
import csv
#from panda3d.core import Filename
from types import *
#from StaticNumerics import *


file = "C:\\School\\Visual Programming\\test.csv"

    
def readcsv(file):
    
    fileReader = csv.reader(open(file),dialect = 'excel', )

    arr = []
    for row in fileReader:
        arr.append(row)
        print(', '.join(row))
        print(arr)
    return arr

def fromcsv(file, types={}, defaults = {}):
    arr = loadCSV(file)
    res = {}
    for l in arr:
        if len(l) == 2:
            key = l[0]
            val = l[1]
            if key in types:
                val = types[key].decode(val)
            res[key] = val
    for k,v in defaults.iteritems():
        if not (k in res):
            res[k] = v
    return res

def writecsv(file, arr):
    
    fileWriter = csv.writer(open(file, "w"), dialect = 'excel')
    for l in arr:
        fileWriter.writerow(l)
    return
    
def tocsv(file, dict, type = {}):
    lines = []
    for k,v in dict.iteritems():
        if k in types:
            v = types[k].encode(v)
        else:
            print "No type for " + k
        lines.append([k, v])
    saveCSV(file, lines)
    
writecsv("C:\\School\\Visual Programming\\test1.csv", readcsv(file))

    