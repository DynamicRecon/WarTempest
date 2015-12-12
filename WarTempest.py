
import optparse
import decoder

__author__ = 'Scott <crazyhousethinker@gmail.com>'
__version__ = "0.1.3alpha"

__doc__ = """

Usage %prog [options] arguments
    Options:
        --briefcase: location of folder where wave files are stored (required)
        --screenshot-filename: file name of images created default: screen
        --width: screen width default: 600
        --height: screen height default: 800
        --hertz: refresh rate default: 60
        --saturation: image saturation percentage between 0 to 100 default: 65
        --contrast-red: hue red value 0-255 default: 100
        --constrast-blue: hue blue value 0-255 default: 0
        --contrast-green: hue green value 0-255 default: 0

"""


if __name__ == "__main__":
      parser = optparse.OptionParser(usage=__doc__)
      #parser options
      parser.add_option("--briefcase", dest="brief_case_folder",
                        action="store",default="",
                        help="Points to the folder were the wav files are. Required no default value.")
      parser.add_option("--screenshot-filename",dest="screenName",action="store",default="screen",
                        help="name of your screenshots default: screen")
      parser.add_option("--width", dest="screen_width",action="store",default=600,type="int",
                        help="overall screen width default: 600")
      parser.add_option("--height", dest="screen_height",action="store",default=800,type="int",
                        help="overall screen height default: 800")
      parser.add_option("--hertz", dest="refresh_rate",action="store",default=60,type="int",
                        help="refresh rate in hertz default: 60")
      parser.add_option("--saturation",dest="saturation",action="store",default=65,type="float",
                        help="color saturation value default: 65")
      parser.add_option("--contrast-red", dest="contrast_red",action="store",default=100,type="int",
                        help="sets red pixel contrast default: 100")
      parser.add_option("--contrast-green", dest="contrast_green",action="store",default=0,type="int",
                        help="sets green pixel contrast default: 0")
      parser.add_option("--contrast-blue", dest="contrast_blue",action="store",default=0,type="int",
                        help="sets blue pixel contrast default: 0")

      options, args = parser.parse_args()
      #thread creation and start
      if options.brief_case_folder == "":
          parser.error("please set your briefcase folder that stores your wav files...")
      else:
          van = decoder.VanEck(path=options.brief_case_folder,title=options.screenName,
            framerate=options.refresh_rate,height=options.screen_height, width=options.screen_width,
            saturation=options.saturation, contrastred=options.contrast_red, contrastgreen=options.contrast_green,
            contrastblue=options.contrast_blue)
          van.start()




