from ReactivePanda.Panda import *

def playit(m,v):
    play(v)
react(key("a", "beep"), playit)
react(key("b", "bomb"), playit)
react(key("c", "click"), playit)
react(key("d", "duck"), playit)
start()
