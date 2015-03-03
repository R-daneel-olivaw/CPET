'''
Created on Feb 26, 2015

@author: Akshat
'''
import pandas as pd
import numpy as np

class PrbLogAgg:
    '''
    classdocs
    '''
    
    dataFrame = []
    csv = []
    concatenated = None

    def __init__(self, *csvFilePath):
        self.csv = csvFilePath
        
    def loadDataFrame(self):
        for path in self.csv:
            df = pd.read_csv(path)
            self.dataFrame.append(df)
            
            self.concatenated = pd.concat(self.dataFrame, ignore_index=True)
            self.concatenated.columns = ['time', 'cpuperc', 'memmb', 'readcount', 'writecount', 'readbytes', 'writebyte']
        
    def getDataFrame(self):
        
        return self.concatenated