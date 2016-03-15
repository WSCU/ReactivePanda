from pythonfrp.Numerics import *
from PandaFRP.PandaNumerics import *
from pythonfrp.Functions import *
from PandaSRC. PandaModels import *

from pythonfrp.Interp import *
from PandaSRC. Externals import lbp, lbr, rbp, rbr, lbr, key, keyUp, leftClick, rightClick,\
                      mouse, lbutton, rbutton, lbuttonPull, rbuttonPull
from PandaSRC. Physics import *
from PandaSRC. Text import text, textBox
from PandaFRP.PandaColor import *
from PandaSRC. Light import *
from PandaSRC. Slider import slider, sliderHpr, sliderColor, sliderP3
from PandaFRP.PandaWorld import world, resetWorld
from PandaSRC. DynamicGeometry import triangle, rectangle, emptyModel, photoWheel, cube, tetra, blastPicture, slicePicture
from PandaFRP.PandaHeartbeat import engine as _engine
from  PandaSRC.PEffect import *
from  PandaSRC.Button import button
from PandaSRC. Sound import play
from PandaSRC. Menu import menu
from PandaSRC. Bezier import *
from PandaSRC. Utils import itime, pointForward, flatRod



def start():
    print("Starting...")
    _engine(0)