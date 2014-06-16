from FileSearch import findSound
from Types import SoundType
from panda3d.core import Filename
from panda3d.core import Loader as loader

class Sound:
    def __init__(self, file, loopCount = 1, volume = 0.5):

        self.filePath = findSound(file)
        self.foundSound = self.filePath is not None
        if self.foundSound:
            self.type = SoundType
            self.volume = volume
            self.loopCount = loopCount
            # there's something strange here wuth the filename representation -
            # only expandFrom seems to give file names usable by loadSfx
            fn = self.filePath.toOsSpecific()
            fn1 = str(Filename.expandFrom(fn))
            self.sound = loader.loadSfx(fn1)
            self.sound.setVolume(self.volume)
        else:
            print "Sound " + file + " not found"
    def __str__(self):
        "Sound: " + self.filePath
    def play(self):
        if self.foundSound:
            if self.loopCount != 1:
                self.sound.setLoop(True)
                self.sound.setLoopCount(self.loopCount)
            self.sound.play()
            return self.sound
    def setRate(self, n):
        if self.foundSound:
            self.sound.setPlayRate(n)

def sound(*p, **k):
    return Sound(*p, **k)


# Add a loop parameter
def play(s, loopCount = 1, volume = 0.5):
    sound(s, loopCount = loopCount, volume = volume).play()
