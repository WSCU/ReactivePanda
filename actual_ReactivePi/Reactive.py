
#  This is a wrapper for all user-visible functions

#  It also contains "start" which initializes the FRP system and
#  starts the reactive engine

import os, sys
import time as ti
from World import *
from Time import *
from Handle import *
from Numerics import *
from StaticNumerics import randomChoice, random01, random11, randomInt, shuffle
from Signal import time, static
from FRP import *
from Interp import *
from Utils import *
from piobjects import *
import piface.pfio as piface
from g import *


# Call this at the end to fire up Panda

def run():
    ct = 0
    while True:
        ct = ct + 1
        for e in g.fastEvents:
            e()
        ti.sleep(.0001)
        if ct == 200:
            t = ti.time()-g.startTime
        #print t
            heartbeat(t, {})
            ct = 0


def start():
    # Initialize the system.  This is called from "begin" and needs to traverse
    # every active signal in the system.
    piface.init()
    g.startTime = ti.time()
    icontext = 0
    g.models.append(world)  # This doesn't happen during initialization
    for m in g.models:
        m.checkSignals(icontext)
        m.d.switches = m.d.newswitches # Add in switchers generated at initialization
    run()
    # Not sure where this is at the moment -- jp
    

