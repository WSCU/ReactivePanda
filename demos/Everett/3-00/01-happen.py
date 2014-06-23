from Panda import *

# Use "happen" to make an event from a boolean


# Make a velocity controller
p = panda()
v = hold(p3(0,0,0), key("leftArrow", p3(-2, 0, 0)) + key("rightArrow", p3(2, 0, 0)) +
                    happen(getX(p.position) < -3, p3(0,0, 0))  + happen(getX(p.position) > 3, p3(0, 0, 0)))


p.position = integral(v)

# Add a score to this!

start()