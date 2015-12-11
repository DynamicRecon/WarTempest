'''

@author: technoAnarchist
'''
import os
import shutil
import ntpath

class Process(object):
    '''
    Process Object is varouis file operations.
    getallwaves() -> Gets all waves in the wave cache.
    copywave() -> moves wave file to the wave cache.
    getwavesize() -> gets total size of waves.
    '''
    def __init__(self):
        pass

    def getallwaves(self,path=""):
        "GetAllWaves(path): returns list of wave files in a folder."
        wav_file_list = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            for filename in filenames:
                if filename.endswith(".wav"):
                    wav_file_list.append(os.sep.join([dirpath, filename]))
        return wav_file_list

    def copywave(self,path=""):
        "CopyWave(filepath): copies wave file to another directory."
        shutil.copyfile(path, os.path.join(os.getcwd(),"waves",ntpath.basename(path)))

    def getwavesize(self,path=""):
        "GetWaveSize(path): returns total size of all wave files in a directory."
        total_size = 0
        start_path = path
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                if f.endswith(".wav"):
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
        return total_size
    