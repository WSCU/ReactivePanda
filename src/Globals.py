# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys, os
import direct.directbase.DirectStart

currentTime = 1 # The current global time
cam = None # The camera object, exported to the user variable cam
panda3dCamera = camera # The original Panda3d camera
objectNames = None # Hands out unique name to every panda object
eventSignals = {}
newEvents = {} # Events that are being sensed but not reacted to yet
events = {} # This is a dictionary of all events posted in the previous tick interval
simEvents = [] # Simulated events for use in the test engine.
reactEvents = [] # Reactions that are not part of an object
eventSignals = None # This is a dictionary of event values received since the last tick
newObjects = [] # The new list of active models assembled at every tick
worldObjects = [] #dictionary with all of the active world objects
thunks = []
tracking = False
nextNE2dY = .95 # Positioning for 2-D controls
nextNW2dY = .95
tccontext = None
initMousePos = None # True on the first tick when there is no prior location
mousePos = None # Last location of the mouse
nextModelId = 0
observers = {} #dictionary of observers
dt = 1 #global delta time
#world = dict() #dictionary of global signals
sl = {}

#Global Error Tracker
error = ""

# Global GUI signals

mouse = None # Current mouse position
lbutton = None # Left button state
rbutton = None # Right button state
rbuttonPull = None # "Pulled" 2-D Point for the right button
lbuttonPull = None # "Pulled" 2-D point for the left button


# Used to identify signals

nextSignalRef = 0

# Configuration stuff
findClickedModels = None

texture = None # Used to communicate with particle effect code from particle panel

collections = {}
#osType = platform.system() # OS That is being used. # NotReturning Correct osType should be Windows Insted of Java.
#print osType
#osType = 'Linux'
#pandaPath = os.getcwd()
pandaPath = "/c/panda/lib"
'''
osType = 'Windows'
if osType is 'Linux':
# print "we're on Linux"
pandaPath = os.getcwd()+"/lib/" # Since we are on a Linux system we will now use a linux file path.
if osType is 'Windows':
# print "we're on Windows" # Since we are on a Windows system we will use the windows file path.
pandaPath = os.getcwd()+"/lib/"
'''
