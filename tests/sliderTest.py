from ReactivePanda.Panda import *

s1 = slider()
text(format("s1 = %f", s1))
s2 = slider(min = -1, max = 2, init = -1, label = "s2")
text(format("s2 = %f", s2))
s3 = sliderP3(label = "s3",  min = -3, max = 3)
text(s3)
s4 = sliderHpr(label="hpr")
s5 = sliderColor(label="color")
panda(position = s3, hpr= s4, color = s5)
start()
