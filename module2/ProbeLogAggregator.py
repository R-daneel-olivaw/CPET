'''
Created on Feb 26, 2015

@author: Akshat
'''
import pandas as pd

class PrbLogAgg:
    '''
    classdocs
    '''
    
    dataFrame = -1
    csv = -1

    def __init__(self, csvFilePath):
        self.csv = csvFilePath
        
    def loadDataFrame(self):
        self.dataFrame = pd.read_csv(self.csv)
        
    def getDataFrame(self):
        return self.dataFrame
        