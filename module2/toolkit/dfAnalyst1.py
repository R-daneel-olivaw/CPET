'''
Created on Mar 3, 2015

@author: Akshat
'''

class Analyst(object):
    '''
    classdocs
    '''

    prbArgLogs = None
    concatenated = None

    def __init__(self, prbLogs):
        '''
        Constructor
        '''
        
        self.prbArgLogs = prbLogs
        self.concatenated = self.prbArgLogs.concatenated
    
    
    def getPeakCpu(self):
        
        maxCpu = self.concatenated['cpuperc'].max()
        
        return maxCpu
    
    def getPeakMem(self):
        
        memMax = self.concatenated['memmb'].max()
        
        return memMax
    
    def get90thpercentile(self):
        
        percentile = self.concatenated.quantile(0.9, axis=0)
        
        return percentile