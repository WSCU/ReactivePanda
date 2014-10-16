import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject

direct = DirectObject()
panda3dCamera = camera # The original Panda3d camera

nextNE2dY = .95 # Positioning for 2-D controls
nextNW2dY = .95

mousePos = None # Last location of the mouse
nextModelId = 0

# Global GUI signals

lbutton = False # Left button state
rbutton = False # Right button state
rbuttonPull = None # "Pulled" 2-D Point for the right button
lbuttonPull = None # "Pulled" 2-D point for the left button

texture = None # Used to communicate with particle effect code from particle panel



pandaPath = "/c/Reactive-Engine/src/lib"
#osType = platform.system() # OS That is being used. # NotReturning Correct osType should be Windows Insted of Java.
#print osType
#osType = 'Linux'
#pandaPath = os.getcwd()
#pandaPath = "/c/panda/lib"
#pandaPath = "/c/panda/lib"
#pandaPath = "/c/users/outcast/documents/GitHub/Reactive-Engine/src/lib" #this is for Grahams personal machine
'''
osType = 'Windows'
if osType is 'Linux':
# print "we're on Linux"
pandaPath = os.getcwd()+"/lib/" # Since we are on a Linux system we will now use a linux file path.
if osType is 'Windows':
# print "we're on Windows" # Since we are on a Windows system we will use the windows file path.
pandaPath = os.getcwd()+"/lib/"
'''

