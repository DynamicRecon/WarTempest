'''


@author: technoAnarchist
'''

import logging
import os
'''

'''
class TempestLogs(object):
    """
        *SUMMARY*
            Basic File logging.

        *METHODS*
            writemsg(msg) writes log.
            readmsg() reads log.

    """
    def __init__(self,path=""):
        "constructers parameter: logpath"
        self.log_file = os.path.join(path,"tempest.log")
        logging.basicConfig(filename=self.log_file,level=logging.DEBUG)
    def writemsg(self,msg):
        "writes logs parameters: log message returns 0"
        logging.debug(msg)
        return 0
    def readlog(self):
        "reads logs in the logpath: returns log messages string."
        f = open(self.log_file,'r')
        body = ""
        try:
            body = f.read()
        finally:
            f.close()
        return body
    
        