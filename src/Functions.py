# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Signal import *
from Factory import *
from StaticNumerics import pi
import Globals

def integerize(r):
    return LiftF("integerize", lambda x: int(x), [r])

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
"""
class TagSignal(Event):
    def __init__(self, fn, s):
        Event.__init__(self)
        self.s = maybeLift(s)
        self.fn = fn
        self.i = 0
        self.context = None
    def refresh(self):
        eventVal = self.s.now()
        if eventVal is None:
            return None
        res = self.fn(self.i, eventVal)
        self.i = self.i + 1
        return res
    def typecheck(self, etype):
        return EventAnyType
    def siginit(self, context):
        if needInit(self, context):
            self.active = TagSignal(self.fn, self.s.siginit(context))
            self.context = context
        return self.active
"""
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
                    reaction()
        return None
    return ObserverF(hitFN)

def hit1(m1, m2, reaction, trace = False):
    def hitFN():
        ml1 = getCollection(m1)
        ml2 = getCollection(m2)
        for m in ml1:
            for e in ml2:
                if m._touches(e, trace = trace):
                    reaction()
                    return
        return None
    return ObserverF(hitFN)

def gTimeObs(x): #Global time Observer
#Not sure about what variables will be passed into the gTOFN
    def gTOFN(): #will track the global time
        if s!= None:
            i = s.now()
            return i
    return ObserverF(0, maybeLift(x), gTOFN)

#Local time Observer
def lTimeObs(x): #Local time Observer
    def lTOFN(i,s): #tracks how long ago some signal was started
        if s!= None:
            i = i + s.now()
            return i
    return ObserverF(0, maybeLift(x), lTOFN)

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
