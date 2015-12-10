import math
import colorsys

'''
*Summary*
class HueShift():
	shifts hue of image based on shift value.
*PARAMETERS*
	colorIn = input color
	colorOut = result color after hue shift
	saturation = default saturation value.
	shiftValue = Hue shift value converted to degrees
*RETURNS*
	ColorOut method
'''


class HueShift(object):
    def __init__(self, colorin=(), saturation=0.65, shiftvalue=0):
        h, s, v = colorsys.rgb_to_hsv(colorin[0] / 255., colorin[1] / 255., colorin[2] / 255.)
        h = (h + -(math.degrees(shiftvalue)) / 360.0) % 1.0
        s = s ** saturation
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        self._colorOut = ((int(r * 255.9999), int(g * 255.9999), int(b * 255.9999)))

    def ColorOut(self):
        return self._colorOut
