"""
File IO tools.
Writing csv from array and dictionary
Reading csv to array and dictionary

Non-Reactive
"""
#import g
import csv
#from panda3d.core import Filename
from types import *
#from StaticNumerics import *

"""
Reads the contents of a csv file and returns an array of each row.
"""
def readcsv(file):    
    fileReader = csv.reader(open(file),dialect = 'excel', )
    arr = []
    for row in fileReader:
        arr.append(row)        
    return arr

"""
Creates a dictionary from a given csv file
"""
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

"""
Writes an array to the given csv file
"""
def writecsv(file, arr):    
    fileWriter = csv.writer(open(file, "w"), dialect = 'excel')
    for l in arr:
        fileWriter.writerow(l)
    return

"""
Writes a csv file from the given dictionary
"""
def tocsv(file, dict, type = {}):
    lines = []
    for k,v in dict.iteritems():
        if k in types:
            v = types[k].encode(v)
        else:
            print "No type for " + k
        lines.append([k, v])
    saveCSV(file, lines)   


    