import wave
import time
import threading

from PIL import Image

import Files
import PixelShift
import os


class VanEck(threading.Thread):
    """
    This VanEck object gets a image frame from a wave file and returns a folder
    of files that based on frames per second and length of wave file.
     constructor: opens wave file and reads the data into an array.
    _DeltaTime(): returns change in time based on refresh rate.
    _SaveImage(): creates screen shot from run method.
    run(): loop through the wav file and builds screen shot.
    """
    def __init__(self,**kwargs):
        "constructor sets values for thread"
        threading.Thread.__init__(self)
        self._audio = []
        self._path = kwargs["path"]
        self._title = kwargs["title"]
        self._loggs = Files.TempestLogs(self._path)
        self._rate = kwargs["framerate"]
        self._h = kwargs["height"]
        self._w = kwargs["width"]
        self._fProc = Files.Process()
        self._saturation = kwargs["saturation"]
        self._r = kwargs["contrastred"]
        self._g = kwargs["contrastgreen"]
        self._b = kwargs["contrastblue"]
        self._href_timing = (self._DeltaTime() / (self._w * self._rate))
        self._vref_timing = (self._DeltaTime() / self._rate)
        self._pixel_timing = (self._DeltaTime() / (self._h * self._w * self._rate))

    def _DeltaTime(self):
        "gets time difference based on refresh rate."
        seconds = 1/self._rate
        timeOne = time.clock()
        time.sleep(seconds/1000)
        timeTwo = time.clock()
        return abs(timeTwo - timeOne)

    def _SaveImage(self,screen=[],index=0):
        "saves image with Pillow"
        print("Saving Screenshot: " + str(index))
        pixel_out = []
        for i in range(len(screen)):
            for j in range(len(screen[i])):
                pixel_out.append(screen[i][j])
        im = Image.new('RGB',(self._w,self._h),None)
        im.putdata(pixel_out)
        im.save(os.path.join(self._path,self._title + str(index) +".bmp"))
        print("Saved: %s" % os.path.join(self._path,self._title + str(index) +".bmp"))

    def run(self):
        "thread override run method. writes screenshots from audio."
        pos = 0
        photo = 0
        screens = []
        line = []
        for wav in self._fProc.GetAllWaves(self._path):
            print("Parsing Audio file: %s" % wav)
            self._loggs.WriteMsg("Parsing Audio file %s" % wav)
            f = wave.open(wav, 'r')
            for i in range(f.getnframes()):
                for x in f.readframes(i):
                    if time.clock() % self._pixel_timing != 0:
                        hue = PixelShift.HueShift(self._r,self._g,self._b,self._saturation,x)
                        line.append(hue.ColorOut())
                    if time.clock() % self._href_timing != 0 and len(line) >= self._w:
                        screens.append(line)
                        line = []
                    if time.clock() % self._vref_timing != 0 and len(screens) >= self._h:
                        self._SaveImage(screens,photo)
                        photo += 1
                        self._loggs.WriteMsg("Screen %d saved..." % (photo))
                        screens = []
                    pos += 1
            f.close()