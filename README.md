ReactivePanda
===============
ReactivePanda is a library that aims to make it easier to teach programming to middle school / high school aged students.

Our philosophy is that using a non-domain specific langague such as python with the addition of reactive programming elements allows for an easier introduction and transition to more advanced programming.

This library is a wrapper of the [panda3d](panda3d.org) game engine.

Usage
---
A simple hello world:

    from ReactivePanda.Panda import *
    panda(hpr = (time, 0 , 0))
    start()

This produces a pandamodel that rotates based on the current time.

Documentation and website
---
All documentation and other information can be found at our webstie, [reactive-engine.org](reactive-engine.org)
