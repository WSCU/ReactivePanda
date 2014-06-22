import Globals
from panda3d.core import *

def findClickedModels():
           pickerNode = CollisionNode('mouseRay')
           pickerNP = Globals.panda3dCamera.attachNewNode(pickerNode)
           pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
           pickerRay = CollisionRay()
           pickerNode.addSolid(pickerRay)
           mpos = base.mouseWatcherNode.getMouse()
           pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())
           myHandler = CollisionHandlerQueue()
           myTraverser = CollisionTraverser('traverser name')
           myTraverser.addCollider(pickerNP, myHandler)
           myTraverser.traverse(render)
           # Assume for simplicity's sake that myHandler is a CollisionHandlerQueue.
           print "Found " + str(myHandler.getNumEntries()) + " Collisions"
           if myHandler.getNumEntries() > 0:
              # This is so we get the closest object.
              myHandler.sortEntries()
              pickedObj = myHandler.getEntry(0).getIntoNodePath()
              # print "Closest = " + str(pickedObj)
              pickedObj = pickedObj.findNetTag('rpandaid')
              # print "tag: " + str(pickedObj)
              if not pickedObj.isEmpty():
                 t = pickedObj.getTag('rpandaid')
                 # print "Clicked on " + str(t)
                 return t
           return None