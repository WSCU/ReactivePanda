
from PandaModel import *

# Characters/Creatures

def panda(**a):
    return pandaModel("lib/models/panda-model.egg.pz", **a)

def teapot(**a):
    return pandaModel("lib/models/teapot.egg.pz",**a)

def boy(**a):
    return pandaModel("lib/models/jack.egg.pz")

def girl(**a):
    return pandaModel("lib/models/eve/eve.egg",**a)

def gorilla(**a):
    return pandaModel("lib/models/gorilla/gorilla.egg", **a)

def bunny(**a):
    return pandaModel("lib/models/bunny/bunny.egg", **a)

def balloonBoy(**a):
    return pandaModel("lib/models/boyballoon/boymodel.egg", **a)

def r2d2(**a):
    return pandaModel("lib/models/r2d2/r2d2.egg", **a)

def tails(**a):
    return pandaModel("lib/models/tails/tails.egg", **a)

def penguin(**a):
    return pandaModel("lib/models/Penguin/Penguin.egg", **a)

def ralph(**a):
    return pandaModel("lib/models/Ralph/ralph.egg", joints = [('neck', 'Neck'), ('leftWrist', 'LeftWrist'),
                                 ('rightWrist', 'RightWrist'),
                                 ('jaw', 'Jaw'), ('leftElbow', 'LeftElbow'),
                                 ('rightShoulder', 'RightShoulder'), ('leftShoulder', 'LeftShoulder'), ('leftKnee', 'LeftKnee'),
                                 ('rightKnee', 'RightKnee')], animations = {"walk" : g.pandaPath + "/models/Ralph/ralph-walk.egg"}, frame = 4, **a )

def bee (**a):
    return pandaModel("lib/models/Bee/Bee.egg", **a)

def chicken (**a):
    return pandaModel("lib/models/Chicken2/Chicken2.egg", **a)

def dragon (**a):
    return pandaModel("lib/models/dragon3/dragon3.egg", **a)

# Objects and Shapes

def sphere(**a):
    return pandaModel("lib/models/sphere/sphere.egg", **a)

def soccerBall(**a):#This one needs some atttention
    return pandaModel("lib/models/soccerball/soccerball.egg", **a)

def chair(**a):
    return pandaModel("lib/models/deskChair/deskchair.egg",**a)

def stretcher(**a):
    return pandaModel("lib/models/stretcher/strecher.egg",**a)

def russianBuilding(**a):
    return pandaModel("lib/models/russianBuilding/tetris-building.egg", **a)

def volleyBall(**a):
    return pandaModel("lib/models/volleyBall/volleyball.egg", **a)

def stoplightSign(**a):
    return pandaModel("lib/models/stoplight_sign/stoplight_sign.egg", **a)

def slipperyRoadSign(**a):
    return pandaModel("lib/models/slipperySign/slipperySign.egg", **a)

def bowlingPins(**a):
    return pandaModel ("bowlingpins/bowlingpins.egg", **a)

def sonic(**a):#Works as of 6-23-08 ~ Kendric
    return pandaModel("lib/models/sonic/sonic.egg",
                       joints = [('neck', 'Neck'), ('leftEyeBrow', 'LeftEyeBrow'), ('rightEyeBrow', 'RightEyeBrow'),
                                 ('leftLowerSpike', 'LeftLowerSpike'), ('lowerRightSpike', 'LowerRightSpike'),
                                 ('topSpike', 'TopSpike'), ('leftMiddleSpike', 'LeftMiddleSpike'),
                                 ('rightMiddleSpike', 'RightMiddleSpike'), ('lowerSpike', 'LowerSpike'),
                                 ('jaw', 'Jaw'),
                                 ('leftShoulder', 'LeftShoulder'), ('rightShoulder', 'LeftShoulder1'),
                                 ('leftElbow', 'LeftElbow'), ('rightElbow', 'LeftElbow1'),
                                 ('leftWrist', 'LeftWrist'), ('rightWrist', 'LeftWrist1'),
                                 ('leftHip', 'LeftHip'), ('rightHip', 'RightHip'),
                                 ('leftKnee', 'LeftKnee'), ('rightKnee', 'RightKnee'),
                                 ('leftAnkle', 'LeftAnkle'), ('rightAnkle', 'RightAnkle'), ], animations = {"walk" : g.pandaPath + "/models/sonic/sonic-run.egg"},
                                 defaultAnimation = "walk", frame = 11, **a)

# Jointed Models


#vehicles
def truck(**a):
    return pandaModel("lib/models/truck/cartruck.egg", **a)

def ford(**a):
    return pandaModel("lib/models/fordCar/ford.egg", **a)

def jeep(**a):
    return pandaModel("lib/models/jeep/jeep.egg", **a)

def boeing707(**a):
    return pandaModel("lib/models/boeing707/boeing707.egg", **a)


def hangGlider(**a):
    return pandaModel("lib/models/hangglider/hang-glider-1.egg", **a)


#Scenary
def discoHall(**a):  # Seems broken - no local size?
    return pandaModel("lib/models/discohall/disco_hall.egg", **a)

def grassScene(**a):
    return pandaModel("lib/models/environment.egg.pz", **a)

def trainEngineScene(**a):
   return pandaModel("lib/models/trainengine/trainengine.egg",**a)

def forestSky(**a):
    return pandaModel("lib/models/forestSky/forestsky.egg", **a)

def farmSky(**a):
    return pandaModel("lib/models/farmSky/farmsky.egg", **a)
