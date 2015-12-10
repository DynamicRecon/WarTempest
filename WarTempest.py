
import optparse
import decoder

__author__ = 'Scott'

"""
main WarTempest File. Takes in command line arguments and starts the VanEck threaded
object.
"""


if __name__ == "__main__":
      parser = optparse.OptionParser(usage="Usage: %prog [options] arguments")
      #parser options
      parser.add_option("--briefcase", dest="brief_case_folder",
                        action="store",default='',
                        help="Points to the folder were the wav files are.")
      parser.add_option("--screenshot-filename",dest="screenName",action="store",default="screen",
                        help="name of your screenshots")
      parser.add_option("--width", dest="screen_width",action="store",default=600,type="int",
                        help="overall screen width")
      parser.add_option("--height", dest="screen_height",action="store",default=800,type="int",
                        help="overall screen height")
      parser.add_option("--hertz", dest="refresh_rate",action="store",default=60,type="int",
                        help="refresh rate in hertz")
      parser.add_option("--saturation",dest="saturation",action="store",default=0.65,type="float",
                        help="color saturation value default: 0.65")
      options, args = parser.parse_args()
      #thread creation and start
      if options.brief_case_folder == "":
          parser.error("please set your briefcase folder that stores your wav files...")
      else:
          van = decoder.VanEck(options.brief_case_folder,
            options.screenName,options.refresh_rate,options.screen_height, options.screen_width,
            options.saturation)
          van.start()




