"""
A non-reactive color type.
This has the type field but doesn't check args
r, g, b, and a values are in (0,1)

Many predefined colors (stolen from Clastic)
"""
from pandac.PandaModules import VBase4   
from Types import numType, ColorType, ColorHSLType
from StaticNumerics import staticLerp
from colorsys import rgb_to_hls, hls_to_rgb

class Color:
    """
    Color describes a color
    """
    def __init__(self, r, g, b, a = 1, type = ColorType):
        """
        Color constructor(r,g,b values are beween 0 and 1)(or HSL values)
        """
        if(type == ColorHSLType):
            self.h = r
            self.s = g
            self.l = b
        else:
            self.r = r
            self.g = g
            self.b = b
        self.a = a
        self.type = type

    def rgb_to_hsl(self):
        """
        transitions from rgb to hsl color
        """
        if(self.type == ColorType):
            hls = rgb_to_hls(self.r, self.g, self.b)
            self.h = hls[0]
            self.l = hls[1]
            self.s = hls[2]
            self.type = ColorHSLType
        else:
            print "Error: Color already ColorHSL"

    def hsl_to_rgb(self):
        """
        transitions from hsl to rgb color
        """
        if(self.type == ColorHSLType):
            rgb = hls_to_rgb(self.h, self.l, self.s)
            self.r = rgb[0]
            self.g = rgb[1]
            self.b = rgb[2]
            self.type = ColorType
        else:
            print "Error: Color already ColorRGB"


    def show(self):
        """
        This is used to get color values into the representation used within
        the Panda library
        """
        if(self.type == ColorType):
            return "[" + str(self.r) + ", " + str(self.g) + ", " + str(self.b) + "]"
        else:
            return "[" + str(self.h) + ", " + str(self.s) + ", " + str(self.l) + "]"
    
    def toVBase4(self):
        """
        Changes the representation to be used by Panda
        """
        if(self.type == ColorHSLType):
            hsl_to_rgb()
        self.type = ColorHSLType
        return VBase4(self.r, self.g, self.b, self.a)

    

    def interp(self, t, c2):
        """
        Returns a Color based on a time t between two colors
        """
        if(self.type == ColorHSLType):
            hsl_to_rgb()
        self.type = ColorHSLType
        return Color(staticLerp(t, self.r, c2.r),
                     staticLerp(t, self.g, c2.g),
                     staticLerp(t, self.b, c2.b),
                     staticLerp(t, self.a, c2.a))

    def __str__(self):
        """
        Returns a String representation of the Color
        """
        if(self.type == ColorType):
            return "(" + str(self.r) + ", " + str(self.g) + ", " + str(self.b) + ")"
        else:
            return "(" + str(self.h) + ", " + str(self.s) + ", " + str(self.l) + ")"


# Avoid integer division!!!  Not sure why this worked with the .0
def color24(r, g, b, a = 1):
    """
    A Color factory(r,g,b values are between 0 and 255)
    """
    return Color(r/255.0, g/255.0, b/255.0, a)

def colorHSL(h, s, l):
    """
    A Color factory to build a HSL color
    """
    return Color(h, s, l, type = ColorHSLType)

#Predefined Colors
black = color24(0,0,0)
blue = color24(0,0,255)
darkBlue = color24(0,0,139)
lightBlue = color24(173, 216, 230)
gray = color24(128, 128, 128)
lightGray = color24(200, 200, 200)
darkGray = color24(60, 60, 60)
limeGreen = color24(102, 255, 0)
green = color24(0,255,0)
darkGreen = color24(0,100,0)
hotpink = color24(255, 77, 148)
red = color24(255,0, 0)
darkRed = color24(139,0,0)
white = color24(255,255,255)
yellow = color24(255, 255, 0)
gold = color24(255,215,0)
silver = color24(192,192,192)
navyBlue = color24(0,0,128)
purple = color24(128,0,128)
deepPurple = color24(153, 50, 204)
violet = color24(148, 0, 211)
brown = color24(165,42,43)
orange = color24(255,122,0)


#Extra Colors (start)
teal = color24(0,188,188) #Good Color :)
tan = color24(210,180,140)
cyan = color24(0,255,255)
aquamarine = color24(112,219,147)
slateGray = color24(198,226,255)
purpleBlue = color24(71,60,139)
bloodOrange = color24(255, 94, 77)
fuchsia = color24(255, 51, 255)
tan = color24(238, 197, 145)
lightTan = color24(255, 211, 155)
olive = color24(128, 128, 0)
springGreen = color24(0, 255, 127)
coral = color24(240, 128, 128)
salmon = color24(250, 128, 114)
lavender = color24(186, 85, 211)

def grayShade(n):
    """
    Returns a Color shade of gray between black(0) and white(1)
    """
    return Color(n,n,n)

def inverse(c):
    """
    return a Color that is the inverse of a Color c
    """
    return (color24(255-(255*c.r), 255-(255*c.g), 255-(255*c.b)))

noColor = color24(0,0,0,0)  # Special: used to indicate no added texturing
