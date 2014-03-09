import g
from Handle import *
from Types import *
import piface.pfio as piface
import time as t

piface.init()

class Text(Handle):
    def __init__(self, text = None, name = 'Text'):
        Handle.__init__(self, name)
        self.__dict__['text'] = newSignalRef(self, 'Text', anyType)
        # This allows the text in the initializer to be reactive.  Not sure why other
        # constructors don't do this.
        if text is not None:
            if not isinstance(text, Signal):
                text = Lift0(text)
            self.text.setBehavior(text)
        #if position is None:
            #position = P2(-.95, g.nextNW2dY)
            #g.nextNW2dY = g.nextNW2dY -.1
        # This code looks OK - we should be able to make the position reactive
        #else:
            #t = getPtype(position)
            #if t != P2Type:
            #    argTypeError(self.name, t, P2Type, 'position')

        #self.d.model = OnscreenText(pos = (position.x, position.y), scale = size*0.05, fg = color.toVBase4(), mayChange = True)

    def refresh(self):
        print (str(self.text.now()))

def text(*p, **k):
    return Text(*p, **k)

class Output(Handle):
    def __init__(self, pin, on, name = 'Light'):
        Handle.__init__(self, name)
        self.__dict__['on'] = newSignalRef(self, 'on', boolType)
        self.d.pin = pin + 1
        if not isinstance(on, Signal):
            on = Lift0(on)
        self.on.setBehavior(on)
        
    def refresh(self):
        o = self.on.now()
        if o == 0:
            o = 1;
        else:
            o = 0;
        p = self.d.pin
        piface.digital_write(p, o)

def output(*p, **k):
    return Output(*p,**k)

class Input(Signal):
    def __init__(self, pin):
        self.pin = pin + 1
    def now(self):
        return piface.digital_read(self.pin)
    def typecheck(self, expected):
        return boolType


def relay(pin):   # JP thinks this should be an output!
    return Output(pin)

def input(pin):
    return Input(pin)

def lightSensor(pin):
    return Input(pin)

def irSensor(pin):
    return Input(pin)

def button(pin):
    return Input(pin)

def light(*p, **k):
    return Output(*p, **k)

def dimLight(*p,**k):
    return PWM(*p,**k)

class PWMTimer:
    def __init__(self, pin):
        self.t = 0
        self.pin = pin
        self.width = 0
    def update(self):
        self.t = self.t+1
        if (self.t < self.width):
            piface.digital_write(self.pin, 1)
        else:
            piface.digital_write(self.pin, 0)
        if self.t >= g.pwmTicks:
            self.t = 0


class PWM(Handle):
    def __init__(self, pin, val, name = 'Dimmable Light'):
        Handle.__init__(self, name)
        self.__dict__['val'] = newSignalRef(self, 'val', numType)
        if not isinstance(val, Signal):
            val = Lift0(val)
        self.val.setBehavior(val)
        self.d.pwm = PWMTimer(pin)
        g.fastEvents.append(lambda: self.d.pwm.update())

    def refresh(self):
        v = self.val.now()
        self.d.pwm.width = v*g.pwmTicks

class SonarDistance:
    def __init__(self, triggerPin, echoPin):
        self.distance = 100
        self.trig = triggerPin+1
        self.echo = echoPin+1
        piface.digital_write(self.trig, 0)
        self.t = 0

    def update(self):
        
        if self.t == 0:   # Send out the ping at time 0
            piface.digital_write(self.trig, 1)
            t.sleep(0.001)
            piface.digital_write(self.trig, 0)
            self.start = t.time()
            self.test = self.start
            self.loop1 = True
            self.t = 1
            return
        else:
            self.t = self.t + 1
            if self.loop1:
                if piface.digital_read(self.echo) == 1:
                    self.start = t.time()
                    if self.test + .15 > t.time():
                        self.distance = 100
                        self.loop1 = False
                        self.loop2 = False
                        return
                    return
                self.end = self.start
                self.loop1 = False
                self.loop2 = True
                return
            if self.loop2:
                if piface.digital_read(self.echo) == 0:
                    self.end = t.time()
                    if self.end > self.start + .15:
                        self.end = -1
                        self.distance = 100
                        self.loop2 = False
                        return
                    else:
                        return
                timing = self.end - self.start
                self.distance = (timing*340.29)
                piface.digital_write(self.trig, 0)
                self.loop2 = False
            else:
                if self.t == 5000:
                    self.t = 0


class SonarInput(Signal):
    def __init__(self, triggerPin, echoPin):
        self.sonar = SonarDistance(triggerPin, echoPin)
        g.fastEvents.append(lambda: self.sonar.update())
    def now(self):
        return self.sonar.distance
    def typecheck(self, expected):
        return numType

def sonar(triggerPin, echoPin):
    return SonarInput(triggerPin, echoPin)
