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
        self.__audio = []
        self.__path = kwargs["path"]
        self.__title = kwargs["title"]
        self.__loggs = Files.TempestLogs(self.__path)
        self.__rate = kwargs["framerate"]
        self.__h = kwargs["height"]
        self.__w = kwargs["width"]
        self.__fProc = Files.Process()
        self.__saturation = kwargs["saturation"]
        self.__r = kwargs["contrastred"]
        self.__g = kwargs["contrastgreen"]
        self.__b = kwargs["contrastblue"]
        self.__href_timing = (self._deltatime() / (self.__w * self.__rate))
        self.__vref_timing = (self._deltatime() / self.__rate)
        self.__pixel_timing = (self._deltatime() / (self.__h * self.__w * self.__rate))

    def _deltatime(self):
        "gets time difference based on refresh rate."
        seconds = 1/self.__rate
        timeOne = time.clock()
        time.sleep(seconds/1000)
        timeTwo = time.clock()
        return abs(timeTwo - timeOne)

    def __saveimage(self,screen=None,index=0):
        "saves image with Pillow in screenshots folder"
        print("Saving Screenshot: " + str(index))
        pixel_out = []
        for i in range(len(screen)):
            for j in range(len(screen[i])):
                pixel_out.append(screen[i][j])
        im = Image.new('RGB',(self.__w,self.__h),None)
        im.putdata(pixel_out)
        if(os.path.exists(os.path.join(self.__path,"screenshots")) == False):
            os.mkdir(os.path.join(self.__path,"screenshots"))
        im.save(os.path.join(self.__path,"screenshots",self.__title + str(index) +".bmp"))
        print("Saved: %s" % os.path.join(self.__path,"screenshots",self.__title + str(index) +".bmp"))

    def run(self):
        "thread override run method. writes screenshots from audio."
        pos = 0
        photo = 0
        screens = []
        line = []
        for wav in self.__fProc.getallwaves(self.__path):
            print("Parsing Audio file: %s" % wav)
            self.__loggs.writemsg("Parsing Audio file %s" % wav)
            f = wave.open(wav, 'r')
            for i in range(f.getnframes()):
                for x in f.readframes(i):
                    if time.clock() % self.__pixel_timing != 0:
                        hue = PixelShift.HueShift(self.__r,self.__g,self.__b,self.__saturation,x)
                        line.append(hue.colorout())
                    if time.clock() % self.__href_timing != 0 and len(line) >= self.__w:
                        screens.append(line)
                        line = []
                    if time.clock() % self.__vref_timing != 0 and len(screens) >= self.__h:
                        self.__saveimage(screens,photo)
                        photo += 1
                        self.__loggs.writemsg("Screen %d saved..." % (photo))
                        screens = []
                    pos += 1
            f.close()