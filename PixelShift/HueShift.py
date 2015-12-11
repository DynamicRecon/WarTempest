import colorsys



class HueShift(object):
    """
        *Summary*
        class HueShift():
	        shifts hue of image based on shift value.
        *PARAMETERS*
	        colorIn = input color
	        red = sets red value
	        green = sets green value
	        blue = sets blue value
	        saturation = default saturation value.
	        shiftValue = Hue shift value converted to degrees
        *RETURNS*
	        ColorOut property
    """

    def __init__(self, red,green,blue, saturation=0, shiftvalue=0):
        h, s, v = colorsys.rgb_to_hsv(red / 255., green / 255., blue / 255.)
        h = ((h + shiftvalue) / 360.0) % 1.0
        s = s ** saturation
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        self._colorOut = ((int(r * 255.9999), int(g * 255.9999), int(b * 255.9999)))

    def ColorOut(self):
        "returns pixel from conversion"
        return self._colorOut
