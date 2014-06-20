#Collection of useful and necessary functions used in the Reactive Engine.
from Signal import *
from Factory import *
from StaticNumerics import pi, zero
from Errors import *
from World import world

import Globals

def now(s):
    if isinstance(s, ObserverF):
        return s.get()
    return None  # Should be an error


    
def integral(x):
    def initIntegral(s):
        s.value = zero
    def thunk(sm):
        i = sm.i.now()
        #print "integral "+ str(sm.state) + " " + str(i) + " " + str(Globals.dt)
        sm.value = sm.value + i * Globals.dt
        #print sm.state
    def integralf(sm):
        Globals.thunks.append(lambda: thunk(sm))
        return sm.value
    return StateMachineF(initIntegral, maybeLift(x), integralf)

def tag(v,evt):
    return lift("tag", lambda e: EventValue(v) if e.occurs() else noEvent)(evt)

def tagMap(fn, evt):
    return lift("tag", lambda e: EventValue(fn(e.value)) if e.occurs() else noEvent) (evt)

def tags(s, vals = None):
    def initTag(s):
        s.count = 0
    def tagFN(sm):
        i = sm.i.now()
        checkEvent(i, "tag")
        if not i.occurs():
            sm.value = noEvent
        else:
            sm.count += 1
            sm.value = EventValue(sm.count) if bals is None else vals[sm.count % len(vals)]
    return StateMachineF(initTag, maybeLift(s), tagFN)

def hold(iv, evt): #Holds the last value of an Event
    def initHold(sm):
        sm.value = iv
    def holdFN(sm):
        i = sm.i.now();
        checkEvent(i, "hold")
        if i.occurs():
            sm.value = i.value;
    return StateMachineF(initHold, maybeLift(evt),holdFN)

def accum(iv, evt): #accumulates the value of a signal over time
    def initAccum(sm):
        sm.value = iv
    def accumFN(sm):
        s = sm.i.now();
        checkEvent(s, "accum")
        if s.occurs():
            sm.value = s.value(sm.value)
    return StateMachineF(initAccum, maybeLift(evt), accumFN)

def getCollection(m):
    if type(m) is str:
        try:
            return Globals.collections[m]
        except KeyErorr:
            print ("No collection with the name: " + m)
            return None
    else:
        return [m]

def hit(m1, m2, reaction, trace = False):
    def hitFN(o):
        ml1 = getCollection(m1)
        ml2 = getCollection(m2)
        for m in ml1:
            for e in ml2:
                if m._touches(e, trace = trace):
                    reaction(m, e)
        return None
    return ObserverF(hitFN)

def hit1(m1, m2, reaction, trace = False):
    def hitFN(o):
        ml1 = getCollection(m1)
        ml2 = getCollection(m2)
        for m in ml1:
            for e in ml2:
                if m._touches(e, trace = trace):
                    reaction(m, e)
                    return
        return None
    return ObserverF(hitFN)

def react(m, when, what = None):
    if what is None:
        what = when
        when = m
        m = world
    coll = getCollection(m)
    for proxy in coll:
        proxy._react(when, what)

def react1(m, when, what):
    coll = getCollection(m)
    for proxy in coll:
        proxy._react1(when, what)

def when(m, when, what):
    coll = getCollection(m)
    for proxy in coll:
        proxy._when(when, what)

def when1(m, when, what):
    coll = getCollection(m)
    for proxy in coll:
        proxy._when1(when, what)

def localtime():
    def ltF(o):
        return Globals.currentTime - o.startTime
    return ObserverF(ltF, type = numType)

localTime = localtime()

def clock(x):
    def initClock(sm):
        sm.value = 0
    def clockFN(sm): # tracks and updates engine time
        # state is the previous value of the clock
        if sm.state >= Globals.currentTime + Globals.dt:
            Globals.currentTime = sm.state
            sm.state += sm.i.now() + Globals.dt
        # add the current clock signal to the list of fast updating signals (which doesn't exist yet)
        return sm.state
    return StateMachineF(initClock, maybeLift(x), clockFN)

#make a clock signal too. Clock will control the heartbeat: make the heartbeat every second
time = ObserverF(lambda x: Globals.currentTime, type = numType)

