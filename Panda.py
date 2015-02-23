from pythonfrp.Numerics import *
from . Numerics import *
from pythonfrp.Functions import *
from . PandaModels import *
#from . Maze import * --Currently not working. 11/18/14
from pythonfrp.Interp import *
from . Externals import lbp, lbr, rbp, rbr, lbr, key, keyUp, leftClick, rightClick,\
                      mouse, lbutton, rbutton, lbuttonPull, rbuttonPull
from . Physics import *
from . Text import text, textBox
from . Color import *
from . Light import *
from . Slider import slider, sliderHpr, sliderColor, sliderP3
from pythonfrp.World import world
from . Camera import camera
from . DynamicGeometry import triangle, rectangle, emptyModel, photoWheel, cube, tetra, blastPicture, slicePicture
from . Engine import engine as _engine
from . PEffect import *
from . Button import button
from . Sound import play
from . Menu import menu
from . Bezier import *
from . Utils import itime, pointForward, flatRod


def start():
    print("Starting...")
    _engine(0)
