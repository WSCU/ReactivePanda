from PandaFRP.PandaGlobals import *
from PandaSRC.PandaModel import *


# Characters/Creatures

def panda(**a):
    return pandaModel("panda-model.egg.pz", name = "Panda", **a)

def teapot(**a):
    return pandaModel("teapot.egg.pz", name = "TeaPot" **a)

def boy(**a):
    return pandaModel("jack.egg.pz", name = "Boy", **a)

def girl(**a):
    return pandaModel("eve/eve.egg", name = "Girl",
            #animation={"walk":"eve/eve-walk.egg","run":"eve/eve-run.egg","jump":"eve/eve-jump.egg",
            #"offbalance":"eve/eve-offbalance.egg","tireroll":"eve/eve-tireroll"},
            **a)

def firefighter(**a):
    return pandaModel("firefighter/firefighter-base.egg", name = "firefighter",
            #animation={"pointup":"firefighter/firefighter-point-up.egg","run":"firefighter/firefighter-run.egg",
            #"stand":"firefighter/firefighter-stand.egg"},
            **a)

def gorilla(**a):
    return pandaModel("gorilla/gorilla.egg", name = "Gorilla",
            #animation={"walk":"gorilla/gorillawalking.egg"},
            **a)

def bunny(**a):
    return pandaModel("bunny/bunny.egg", name = "Bunny", **a)

def boyBalloon(**a):
    return pandaModel("boyballoon/boymodel.egg", name = "BoyBalloon",
            #animation={"act":"boyballon/boyanimation.egg"},
            **a)

def r2d2(**a):
    return pandaModel("r2d2/r2d2.egg", name = "R2D2", **a)

def tails(**a):
    return pandaModel("tails/tails.egg", name = "tails", **a)

def penguin(**a):
    return pandaModel("Penguin/Penguin.egg", name = "Penguin", **a)

def ralph(**a):
    return pandaModel(Globals.pandaPath + "/models/Ralph/ralph.egg", name = "Ralph",
#                        joints = [('neck', 'Neck'), ('leftWrist', 'LeftWrist'),
#                                 ('rightWrist', 'RightWrist'),
#                                 ('jaw', 'Jaw'), ('leftElbow', 'LeftElbow'),
#                                 ('rightShoulder', 'RightShoulder'), ('leftShoulder', 'LeftShoulder'), ('leftKnee', 'LeftKnee'),('rightKnee', 'RightKnee')],
                                 animation = {"walk" : Globals.pandaPath + "/models/Ralph/ralph-walk.egg","run" : Globals.pandaPath + "/models/Ralph/ralph-run.egg",
                                 "jump": Globals.pandaPath + "/models/Ralph/ralph-jump.egg","offbalance":Globals.pandaPath + "/models/Ralph/ralph-offbalance.egg"}, frame = 4, **a )

def bee (**a):
    return pandaModel("Bee/Bee.egg", name = "Bee", **a)

def chicken (**a):
    return pandaModel("Chicken2/Chicken2.egg", name = "Chicken", **a)

def dragon (**a):
    return pandaModel("dragon3/dragon3.egg", name = "Dragon", **a)
condecendingDragon = dragon
# Objects and Shapes

def sphere(**a):
    return pandaModel("sphere/sphere.egg", name = "Sphere", **a)

def soccerBall(**a):#This one needs some atttention
    return pandaModel("soccerball/soccerball.egg", name = "SoccerBall", **a)

soccerball = soccerBall

def chair(**a):
    return pandaModel("deskChair/deskchair.egg", name = "Chair", **a)

def stretcher(**a):
    return pandaModel("stretcher/strecher.egg", name = "Stretcher", **a)

def russianBuilding(**a):
    return pandaModel("russianBuilding/tetris-building.egg", name = "RussianBuilding", **a)

def volleyBall(**a):
    return pandaModel("volleyBall/volleyball.egg", name = "VolleyBall", **a)

def stoplightSign(**a):
    return pandaModel("stoplight_sign/stoplight_sign.egg", name = "StopLightSign", **a)

def slipperyRoadSign(**a):
    return pandaModel("slipperySign/slipperySign.egg", name = "SlipperyRoadSign", **a)

def bowlingPins(**a):
    return pandaModel ("bowlingpins/bowlingpins.egg", name = "BowlingPins", **a)

def tardis(**a):
    return pandaModel ("TARDIS/tardis.egg", name = "Tardis", **a)

def crow(**a):
    return pandaModel ("crow/crow.egg", name = "crow", **a)

def flower(**a):
    return pandaModel ("Flower/flower#3", name = "Flower", texture=Globals.pandaPath+"/models/Flower/flowerPurple.png", **a)

def spiderman(**a):
    return pandaModel(PandaGlobals.pandaPath + "/models/Spiderman/SpiderMan.egg", name = "Spiderman",
            animation={"DOIT!":PandaGlobals.pandaPath + "/models/Spiderman/SpiderMan-DOIT.egg","pose":PandaGlobals.pandaPath + "/models/Spiderman/SpiderMan-Pose.egg"},
            texture=PandaGlobals.pandaPath + "/models/Spiderman/spiderman_d.tga",
            **a )

def sonic(**a):#Works as of 6-23-08 ~ Kendric
    return pandaModel("sonic/sonic.egg", name = "Sonic",
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
                                 ('leftAnkle', 'LeftAnkle'), ('rightAnkle', 'RightAnkle'), ], animation = {"walk" : Globals.pandaPath + "/models/sonic/sonic-run.egg"},
                                  frame = 11, **a)

# Jointed Models


#vehicles
def truck(**a):
    return pandaModel("truck/cartruck.egg", name = "Truck", **a)

def ford(**a):
    return pandaModel("fordCar/ford.egg", name = "Ford", **a)

def jeep(**a):
    return pandaModel("jeep/jeep.egg", name = "Jeep", **a)

def boeing707(**a):
    return pandaModel("boeing707/boeing707.egg", name = "Boeing707", **a)

def hangGlider(**a):
    return pandaModel("hangglider/hang-glider-1.egg", name = "HangGlider", **a)


#Scenary
def volcano(**a):
    return pandaModel("Volcano/volcanoModel.egg", name = "Volcano", **a)

def discoHall(**a):  # Seems broken - no local size?
    return pandaModel("discohall/disco_hall.egg", name = "DiscoHall", **a)

def grassScene(**a):
    return pandaModel("environment.egg.pz", name = "GrassScene", **a)

def trainEngine(**a):
   return pandaModel("trainengine/trainengine.egg", name = "TrainEngine", **a)

def forestSky(**a):
    return pandaModel("forestSky/forestsky.egg", name = "ForestSky", **a)

def farmSky(**a):
    return pandaModel("farmSky/farmsky.egg", name = "farmSky", **a)

def celestial(**a):
    return pandaModel("celestial/celestial.egg", name = "celestial", **a)

def sunset(**a):
    return pandaModel("sunset/sunset.egg", name = "sunset", **a)
