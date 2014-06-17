#Collection of useful and necessary functions used in the Reactive Engine.
from Signal import *
from Factory import *
from StaticNumerics import pi
import Globals

def integerize(r):
    return LiftF("integerize", lambda x: int(x), [r])

def now(s):
    if isinstance(s, ObserverF):
        return s.get()
    return None

def integral(x):
    def thunk(sm):
        i = sm.i.now()
        #print "integral "+ str(sm.state) + " " + str(i) + " " + str(Globals.dt)
        sm.state = sm.state + i * Globals.dt
        #print sm.state
    def integralf(sm):
        Globals.thunks.append(lambda: thunk(sm))
        return sm.state
    return StateMachineF(0, maybeLift(x), integralf)

# this is a function that uses the Observer class to get a value from the signal list
def ref(key):
    def reffunc():
        return Globals.sl[key]
    return ObserverF(reffunc)

def simkey(key, v):
    return {key : v}

def tag(fn, s):
    def tagFN(sm):
        i = sm.i.now()
        if i is None:
            return None
        res = fn(sm.state, i)
        sm.state += 1
        return res
    return StateMachineF(0, maybeLift(s), tagFN)

def hold(x, iv): #Holds the last value of a signal
    def holdFN(sm):
        i = sm.i.now();
        if i != None:
            return i;
        return iv
    return StateMachineF(iv, maybeLift(x),holdFN)

def key(k, v):
    def keyfunc():
        if Globals.events:
            if k in Globals.events[0][1].keys():
                return v
        return None
    return ObserverF(keyfunc)

def accum(x): #accumulates the value of a signal over time
    def accumFN(sm):
        s = sm.i.now();
        if s!= None:
            sm.state += s
        return sm.state
    return StateMachineF(0, maybeLift(x), accumFN)

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
    def hitFN():
        ml1 = getCollection(m1)
        ml2 = getCollection(m2)
        for m in ml1:
            for e in ml2:
                if m._touches(e, trace = trace):
                    reaction(m, e)
        return None
    return ObserverF(hitFN)

def hit1(m1, m2, reaction, trace = False):
    def hitFN():
        ml1 = getCollection(m1)
        ml2 = getCollection(m2)
        for m in ml1:
            for e in ml2:
                if m._touches(e, trace = trace):
                    reaction(m, e)
                    return
        return None
    return ObserverF(hitFN)

def react(m, when, what):
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

def globaltime():
    def gtF():
        return Globals.currentTime
    return ObserverF(gtF)

time = globaltime()

def localtime():
    starttime = Globals.currentTime
    def ltF():
        return Globals.currentTime - starttime
    return ObserverF(ltF)

localTime = localtime()

def clock(x):
    def clockFN(sm): # tracks and updates engine time
        # state is the previous value of the clock
        if sm.state >= Globals.currentTime + Globals.dt:
            Globals.currentTime = sm.state
            sm.state += sm.i.now() + Globals.dt
        # add the current clock signal to the list of fast updating signals (which doesn't exist yet)
        return sm.state
    return StateMachineF(0, maybeLift(x), clockFN)

#make a clock signal too. Clock will control the heartbeat: make the heartbeat every second
time = ObserverF(lambda: Globals.currentTime)
def degrees( v):
    return v*(180/pi)
