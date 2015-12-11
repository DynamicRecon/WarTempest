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
    _deltaTime(): returns change in time
    _deltaVolume(): returns a change in amplitude of the recording
    _deltaPoint(): returns a change in position from a step in file
    _buildFrame(): generates a png file from the wave file.
    run(): loop through the wav file and build each file with buildFrame().
    """
    def __init__(self,**kwargs):
        threading.Thread.__init__(self)
        self._audio = []
        self._path = kwargs["path"]
        self._title = kwargs["title"]
        self._loggs = Files.TempestLogs(self._path)
        self._rate = kwargs["framerate"]
        #basic height and width
        self._h = kwargs["height"]
        self._w = kwargs["width"]
        self._fProc = Files.Process()
        self._saturation = kwargs["saturation"]
        self._r = kwargs["contrastred"]
        self._g = kwargs["contrastgreen"]
        self._b = kwargs["contrastblue"]
        #timing values.
        self._href_timing = (self._DeltaTime() / (self._w * self._rate))
        self._vref_timing = (self._DeltaTime() / self._rate)
        self._pixel_timing = (self._DeltaTime() / (self._h * self._w * self._rate))

    #measure overall change in time based on system clock.
    def _DeltaTime(self):
        seconds = 1/self._rate
        timeOne = time.clock()
        time.sleep(seconds/1000)
        timeTwo = time.clock()
        return abs(timeTwo - timeOne)

    #save Image
    def _SaveImage(self,screen=[],index=0):
        print("Saving Screenshot: " + str(index))
        pixel_out = []
        for i in range(len(screen)):
            for j in range(len(screen[i])):
                pixel_out.append(screen[i][j])
        im = Image.new('RGB',(self._w,self._h),None)
        im.putdata(pixel_out)
        im.save(os.path.join(self._path,self._title + str(index) +".bmp"))
        print("Saved: %s" % os.path.join(self._path,self._title + str(index) +".bmp"))

    #gets the lines from the wave files.
    #stores them in a scans array to run the draw method.
    def run(self):
        #audio and drawing increment values
        pos = 0
        photo = 0
        screens = []
        line = []
        #wave file data stored in self.audio array.
        for wav in self._fProc.GetAllWaves(self._path):
            print("Parsing Audio file: %s" % wav)
            self._loggs.WriteMsg("Parsing Audio file %s" % wav)
            f = wave.open(wav, 'r')
            for i in range(f.getnframes()):
                for x in f.readframes(i):
                    #individual pixel timing
                    #shift pixel
                    #convert
                    #add to array of line
                    if time.clock() % self._pixel_timing != 0:
                        hue = PixelShift.HueShift(self._r,self._g,self._b,self._saturation,x)
                        line.append(hue.ColorOut())
                    #time with horizontal refresh
                    #append to array of screens
                    if time.clock() % self._href_timing != 0 and len(line) >= self._w:
                        screens.append(line)
                        line = []
                    #overall screen refresh
                    #save image
                    if time.clock() % self._vref_timing != 0 and len(screens) >= self._h:
                        self._SaveImage(screens,photo)
                        photo += 1
                        self._loggs.WriteMsg("Screen %d saved..." % (photo))
                        screens = []
                    pos += 1
            f.close()