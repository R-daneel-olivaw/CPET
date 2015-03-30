'''
Created on Feb 26, 2015

@author: Akshat
'''
import pandas as pd
import numpy as np
import ntpath

class PrbLogAgg:
    '''
    classdocs
    '''
    
    dataFrame = {}
    csv = []

    def __init__(self, output_directory, *csvFilePath):
        self.output_directory = output_directory
        self.csv = csvFilePath
        
    def loadDataFrame(self):
        for path in self.csv:
            df = pd.read_csv(path)
            self.dataFrame[self.path_leaf(path)] = df
            
        for i_df in self.dataFrame:
            
            i_df.columns = ['time', 'cpuperc', 'memmb', 'readcount', 'writecount', 'readbytes', 'writebyte', 'netConnCount', 'childProcCount']
        
    def getDataFrame(self, logfile_name):
        
        return self.dataFrame[logfile_name]
    
    def getdataFrames(self):
        
        return self.dataFrame
    
    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
