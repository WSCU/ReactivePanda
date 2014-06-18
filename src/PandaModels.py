
from PandaModel import *

# Characters/Creatures

def panda(**a):
    return pandaModel("panda-model.egg.pz", **a)

def teapot(**a):
    return pandaModel("teapot.egg.pz",**a)

def boy(**a):
    return pandaModel("jack.egg.pz")

def girl(**a):
    return pandaModel("eve/eve.egg",**a)

def gorilla(**a):
    return pandaModel("gorilla/gorilla.egg", **a)

def bunny(**a):
    return pandaModel("bunny/bunny.egg", **a)

def balloonBoy(**a):
    return pandaModel("boyballoon/boymodel.egg", **a)

def r2d2(**a):
    return pandaModel("r2d2/r2d2.egg", **a)

def tails(**a):
    return pandaModel("tails/tails.egg", **a)

def penguin(**a):
    return pandaModel("Penguin/Penguin.egg", **a)

def ralph(**a):
    return pandaModel("Ralph/ralph.egg", joints = [('neck', 'Neck'), ('leftWrist', 'LeftWrist'),
                                 ('rightWrist', 'RightWrist'),
                                 ('jaw', 'Jaw'), ('leftElbow', 'LeftElbow'),
                                 ('rightShoulder', 'RightShoulder'), ('leftShoulder', 'LeftShoulder'), ('leftKnee', 'LeftKnee'),
                                 ('rightKnee', 'RightKnee')], animations = {"walk" : g.pandaPath + "/models/Ralph/ralph-walk.egg"}, frame = 4, **a )

def bee (**a):
    return pandaModel("Bee/Bee.egg", **a)

def chicken (**a):
    return pandaModel("Chicken2/Chicken2.egg", **a)

def dragon (**a):
    return pandaModel("dragon3/dragon3.egg", **a)

# Objects and Shapes

def sphere(**a):
    return pandaModel("sphere/sphere.egg", **a)

def soccerBall(**a):#This one needs some atttention
    return pandaModel("soccerball/soccerball.egg", **a)

def chair(**a):
    return pandaModel("deskChair/deskchair.egg",**a)

def stretcher(**a):
    return pandaModel("stretcher/strecher.egg",**a)

def russianBuilding(**a):
    return pandaModel("russianBuilding/tetris-building.egg", **a)

def volleyBall(**a):
    return pandaModel("volleyBall/volleyball.egg", **a)

def stoplightSign(**a):
    return pandaModel("stoplight_sign/stoplight_sign.egg", **a)

def slipperyRoadSign(**a):
    return pandaModel("slipperySign/slipperySign.egg", **a)

def bowlingPins(**a):
    return pandaModel ("bowlingpins/bowlingpins.egg", **a)

def sonic(**a):#Works as of 6-23-08 ~ Kendric
    return pandaModel("sonic/sonic.egg",
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
    return pandaModel("truck/cartruck.egg", **a)

def ford(**a):
    return pandaModel("fordCar/ford.egg", **a)

def jeep(**a):
    return pandaModel("jeep/jeep.egg", **a)

def boeing707(**a):
    return pandaModel("boeing707/boeing707.egg", **a)


def hangGlider(**a):
    return pandaModel("hangglider/hang-glider-1.egg", **a)


#Scenary
def discoHall(**a):  # Seems broken - no local size?
    return pandaModel("discohall/disco_hall.egg", **a)

def grassScene(**a):
    return pandaModel("environment.egg.pz", **a)

def trainEngineScene(**a):
   return pandaModel("trainengine/trainengine.egg",**a)

def forestSky(**a):
    return pandaModel("forestSky/forestsky.egg", **a)

def farmSky(**a):
    return pandaModel("farmSky/farmsky.egg", **a)
