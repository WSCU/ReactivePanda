import Globals
class Proxy:
    def __init__(self, name, updater):
        self._alive = True;
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
            self._updateSignals[name] = value
    def __getattr__(self, name):
        if name[0] == '_':
            return self.__dict__[name]
        else:
            return ObserverF(lambda : self.get(name))
    def get(self, name):
        try: 
            return self._signals[name].now()
        except KeyError:
            print( str(name) + " does not exist in this Proxy " + repr(self)
    def initialize(self):
        for k, v in self._updateSignals.items():
            print("Objects: " + repr(k) + " is initializing: " + str(v))
            self._signals[k] = v.start() # This is screwing up Integral
        self._updateSignals = {}
    def updater(self):
        self._updater(self)
    def react(self, when, what):
        if alive:
            when = maybeLift(when)
            self._gReactions.append((when.start(), what))
    def react1(self, when, what):
        if alive:
            when = maybeLift(when)
            self._1Reactions.append((when.start(), what))
    def update(self):
        tempSigVals = {}
        if self._alive:
            for k, v in self._signals.items():
                #print("Objects: " + str(self) + " is updating: " + k)
                tmepSigVals[k] = v.now()
            thunks = []
            for a in self._1Reactions:
                #print("Object: " + str(self) + " is updating: " + str(a[0]))
                temp = a[0].now()
                if temp != None:
                    #print("    " + str(temp) + " is being added to thunks")
                    thunks.add(lambda : a[1](self, temp))
                if (len(thunks) >= 2):
                    print("Multiple one time reactions in a heartbeat")
            for a in self._gReactions:
                temp = a[0].now()
                #print("Object: " + str(self) + " is updating: " + str(a[0]))
                temp = a[0].now()
                if temp != None:
                    #print("    " + str(temp) + " is being added to thunks")
                    thunks.add(lambda : a[1](self, temp))
                self._updateSignals = {}
            self.updater(tempSigVals)
            return thunks

    def __str__(self):
        return self._name

    def __repr__(self):
        return str(self._name)
