'''
Created on Mar 3, 2015

@author: Akshat
'''
from pandas.core.frame import DataFrame

class Analyst(object):
    '''
    classdocs
    '''

    prbArgLogs = None

    def __init__(self, prbLogs):
        '''
        Constructor
        '''
        
        self.prbArgLogs = prbLogs
    
    
    def getPeakCpu(self):
        
        maxCpu = self.concatenated['cpuperc'].max()
        
        return maxCpu
    
    def getPeakMem(self):
        
        memMax = self.concatenated['memmb'].max()
        
        return memMax
    
    def getPercentile(self, trg_percentile):
        
        percentile = self.concatenated.quantile(trg_percentile, axis=0)
        
        
        percentile_df = DataFrame(percentile)
        
        column_name = trg_percentile * 100
        percentile_df.columns = [str(column_name)]
        
        return percentile_df
