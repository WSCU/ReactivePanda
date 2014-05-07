import Globals
from Factory import *
from Types import proxyType

class Proxy:
    def __init__(self, name, updater, types):
        self._types = types
        self._alive = True;
        self._type = proxyType
        self._signals = {}
        self._1Reactions = []
        self._gReactions = []
        self._updateSignals = {}
        self._name = name
        self._updater = updater
        Globals.newObjects.append(self)

    def __setattr__(self, name, value):
        if name[0] == '_':
            self.__dict__[name] = value
        else:
            #if value.type == SignalType:
            self._updateSignals[name] = value
            #else:
             #   print("Error: Tried to set attribute to non-signal.")
    def __getattr__(self, name):
        if name[0] == '_':
            return self.__dict__[name]
        else:
            return ObserverF(lambda : self.get(name))
            #return self._signals[name]
    def get(self, name):
        try: 
            return self._signals[name].now()
        except KeyError:
            print( str(name) + " does not exist or has not been started in this Proxy " + repr(self))
    def initialize(self):
        for k, v in self._updateSignals.items():
            print("Object: " + self._name + " is initializing: " + str(v))
            if self._types.has_key(k):
                ty = self._types[k]
            else:
                ty = anyType
            v = maybeLift(v)
            Globals.error = "On Line 46 of Proxy, In object " + self._name + ", attribute " + v.name
            self._signals[k] = v.start(expectedType = ty)[0] # This is screwing up Integral
        self._updateSignals = {}
    def updater(self):
        self._updater(self)
    def react(self, when, what):
        if self._alive:
            when = maybeLift(when)
            Globals.error = "On Line 54 of Proxy, In object " + self._name + ", initializing reaction " + when.name
            self._gReactions.append((when.start()[0], what))
    def react1(self, when, what):
        if alive:
            when = maybeLift(when)
            Globals.error = "On Line 59 of Proxy, In object " + self._name + ", initializing one time reaction " + when.name
            self._1Reactions.append((when.start()[0], what))
    def update(self):
        tempSigVals = {}
        if self._alive:
            for k, v in self._signals.items():
                #print("Objects: " + str(self) + " is updating: " + k)
                v.now()
            thunks = []
            for a in self._1Reactions:
                #print("Object: " + str(self) + " is updating: " + str(a[0]))
                temp = a[0].now()
                if temp != None:
                    #print("    " + str(temp) + " is being added to thunks")
                    thunks.append(lambda : a[1](self, temp))
            if (len(thunks) >= 2):
                print("Multiple one time reactions in a heartbeat")
            for a in self._gReactions:
                temp = a[0].now()
                #print("Object: " + str(self) + " is updating: " + str(a[0]))
                if temp != None:
                    #print("    " + str(temp) + " is being added to thunks")
                    thunks.append(lambda : a[1](self, temp))
            self._updater(self)
            return thunks

    def __str__(self):
        #print (self._signals)
        #print (self._updateSignals)
        return self._name

    def __repr__(self):
        return str(self._name)
