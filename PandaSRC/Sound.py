from PandaSRC.FileSearch import findSound
from pythonfrp.Types import soundType
from panda3d.core import Filename

global globSound

class Sound:
    def __init__(self, file, loopCount = 1, volume = 0.5):

        self.filePath = findSound(file)
        self.foundSound = self.filePath is not None
        if self.foundSound:
            self.type = soundType
            self.volume = volume
            self.loopCount = loopCount
            # there's something strange here wuth the filename representation -
            # only expandFrom seems to give file names usable by loadSfx
            fn = self.filePath.toOsSpecific()
            fn1 = str(Filename.expandFrom(fn))
            self.sound = loader.loadSfx(fn1)
            self.sound.setVolume(self.volume)
        else:
            print("Sound " + file + " not found")
    def __str__(self):
        "Sound: " + self.filePath
    def play(self):
        if self.foundSound:
            if self.loopCount != 1:
                self.sound.setLoop(True)
                self.sound.setLoopCount(self.loopCount)
            self.sound.play()
            return self.sound
    def stop(self):
        if self.foundSound:
            self.sound.stop()
    def setRate(self, n):
        if self.foundSound:
            self.sound.setPlayRate(n)

def sound(*p, **k):
    return Sound(*p, **k)


#Start/stop a sound; uses globSound to refer to same sound object
def play(s, loopCount = 1, volume = 0.5):
    global globSound
    globSound = sound(s, loopCount = loopCount, volume = volume)
    globSound.play()

def stopSound():
    global globSound
    globSound.stop()
    
