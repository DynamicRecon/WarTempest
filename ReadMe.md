#WarTempest v0.1.2 Alpha 

##Description

WarTempest is a python based command line program that takes the information from a wave file recorded from either
a Software Defined Radio setup like SDR# or GNU Radio. Then it tries to create screen shots from the wave file data
into a set of png files. 

PLEASE NOTE THIS PROJECT IS EXPERIMENTAL. RESULTS MAY VARY.

##Usage

WarTempest.py --briefcase-folder <path to folder with wave files> --width <screenheight> --height <screenwidth>
 --refresh-rate <refresh rate in hertz> --saturation <decimal value of saturation per pixel>
 --contrast-red <integer value for red pixel: 0-255> --contrast-green <integer value for green pixel: 0-255>
 --contrast-blue <integer value for blue pixel: 0-255>
##Requirements
 
 Python 3.4
 
##PLEASE NOTE
 
 This package is entirely experimental and results may vary. I am still experimenting with the software and will
 provide updates as I go along.