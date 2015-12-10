'''


@author: technoAnarchist
'''

import logging
import os
'''
*SUMMARY*
Basic File logging.

*METHODS*
writemsg(msg) writes log.
readmsg() reads log.

'''
class TempestLogs(object):
    '''
    Simple log object that logs any messages from the VanEck Thread and 
    the overall application.
    '''
    def __init__(self,path=""):
        self.log_file = os.path.join(path,"tempest.log")
        logging.basicConfig(filename=self.log_file,level=logging.DEBUG)
    def WriteMsg(self,msg):
        logging.debug(msg)
        return 0
    def ReadLog(self):
        f = open(self.log_file,'r')
        body = ""
        try:
            body = f.read()
        finally:
            f.close()
        return body
    
        