# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import unittest
import sched, time
from Signal import *
from Factory import *
import Globals 

def integral(x):
    def integralFN(i, s): #Euler method for integration
    # state s is the previous value of the integral
        c = s + i * Globals.dt
        print str(i) + " " + str(s)
        return c, c
    return StateMachineF(0, integralFN, maybeLift(x), 0)

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
def hold(x):
    def holdFN(i, s, dt):
        if s!= None:
            i = s.now;
            return i,i;
        
    return StateMachineF(0, holdFN,x, 0)

def accum(x):
    def accumFN(i,s,dt):
        v = self.s.now()
        if v is None:
            return self.i
        self.i = v(self.i)
        return self.i
    return StateMachineF(0, accumFN, x, 0)
        
def maybeLift(x):
    t = type(x)
    if t is type(1):
        return Lift0(x)
    if t is type(1.0):
        return Lift0(x)
    return x
