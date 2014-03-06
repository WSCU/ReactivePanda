import piface.pfio as piface
import time

class SonarDistance:

    def __init__(self, triggerPin, echoPin):
        self.distance = -1
        self.trig = triggerPin+1
        self.echo = echoPin+1
        piface.digital_write(self.trig, 0)

    def update(self):
        '''print "updating sonar"'''
        piface.digital_write(self.trig, 1)
        time.sleep(0.001)
        piface.digital_write(self.trig, 0)

        start = time.time()
        test = start

        while piface.digital_read(self.echo) == 1:
            start = time.time()
            if test + .15 > time.time():
                end = -1
                '''print "failure"'''
                self.distance = -1
                return
            time.sleep(.0001)
        
        end = start

        while piface.digital_read(self.echo) == 0:
            end = time.time()
            if end > start + .15:
                end = -1
                '''print "failure to get distance"'''
                self.distance = -1
                return
            time.sleep(.0001)

        timing = end - start
        self.distance = (timing*340.29)

        piface.digital_write(self.trig, 0)

    def get_value(self):
        return self.distance
