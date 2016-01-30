from direct.showbase.DirectObject import DirectObject
from PandaNumerics import p2

direct = DirectObject()

nextNE2dY = .95 # Positioning for 2-D controls
nextNW2dY = .95

mousePos = None # Last location of the mouse
nextModelId = 0

# Global GUI signals

lbutton = False # Left button state
rbutton = False # Right button state
rbuttonPull = p2(0,0) # "Pulled" 2-D Point for the right button
lbuttonPull = p2(0,0) # "Pulled" 2-D point for the left button

texture = None # Used to communicate with particle effect code from particle panel


# Temporary for testing, this needs to be automatically set
pandaPath = "/c/Panda/ReactivePanda/lib"

panda3dCamera = camera
