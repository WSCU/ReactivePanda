# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import unittest
import sched, time
from Signal import *
from Factory import *
import Globals 


def integral(x):
    def integralf(sm): # Euler method for integration
        # state is the previous value of the integral
        i = sm.i.now()
        sm.state = sm.state + i * Globals.dt
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
def hold(x, iv): #Holds the last value of a signal
    def holdFN(sm):
        i = sm.i.now();
        if i != None:
            sm.state = i
    return StateMachineF(iv, maybeLift(x),holdFN)

def key(k, v):
    def keyfunc():
        if Globals.events:
            if k in Globals.events[0][1].keys():
                return v        
        return None
    return ObserverF(keyfunc)

def accum(x): #accumulates the value of a signal over time
    def accumFN(i,s):
        if s!= None:
            i = i + s.now()
            return i

    return StateMachineF(0, maybelift(x), accumFN)
        
def maybeLift(x):
    t = type(x)
    if t is type(1):
        return Lift0(x)
    if t is type(1.0):
        return Lift0(x)
    return x


