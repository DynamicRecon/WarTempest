__author__ = 'Scott'


class ColorShift(object):
    def __init__(self,color=(),shiftValue=0):
        self._color = color
        self._value = shiftValue
    #shift a rgb pixel value
    def Shift(self):
        newColor = []
        for c in self._color:
            newColor.append((c & self._value) >> 2)
        return tuple(newColor)


