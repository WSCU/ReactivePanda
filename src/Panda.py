from Numerics import *
from Functions import *
from PandaModels import *
from Interp import *
from Externals import lbp, lbr, rbp, rbr, lbr, key, keyUp, leftClick, rightClick,\
                      mouse, lbutton, rbutton, lbuttonPull, rbuttonPull
from Physics import *
from Text import text, textBox
from Color import *
from Light import *
from Slider import slider
from World import world, camera
from DynamicGeometry import triangle, rectangle
from Engine import engine as _engine
from PEffect import *
from Button import button

def start():
    print("Starting...")
    _engine(0)
