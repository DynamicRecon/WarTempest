'''

@author: technoAnarchist
'''
import os
import shutil
import ntpath

class Process(object):
    '''
    Process Object is varouis file operations.
    getAllWaves() -> Gets all waves in the wave cache.
    copyWave() -> moves wave file to the wave cache.
    getWaveSize() -> gets total size of waves.
    '''
    def __init__(self):
        pass
    "GetAllWaves(path): returns list of wave files in a folder."
    def GetAllWaves(self,path=""):
        wavFileList = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            for filename in filenames:
                if filename.endswith(".wav"):
                    wavFileList.append(os.sep.join([dirpath, filename]))
        return wavFileList
    "CopyWave(filepath): copies wave file to another directory."
    def CopyWave(self,path=""):
        shutil.copyfile(path, os.path.join(os.getcwd(),"waves",ntpath.basename(path)))
    "GetWaveSize(path): returns total size of all wave files in a directory."
    def getWaveSize(self,path=""):
        total_size = 0
        start_path = path
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                if f.endswith(".wav"):
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
        return total_size
    