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
    
    
    def getPeakCpu(self, df):
        
        maxCpu = df['cpuperc'].max()
        
        return maxCpu
    
    def getPeakMem(self, df):
        
        memMax = df['memmb'].max()
        
        return memMax
    
    def getPercentile(self, df, trg_percentile):
        
        percentile = df.quantile(trg_percentile, axis=0)
        
        percentile_df = DataFrame(percentile)
        
        column_name = trg_percentile * 100
        percentile_df.columns = [str(column_name)]
        
        return percentile_df
    
    def getPercentileLst(self, df, trg_percentile):
        
        percentile_df = df.quantile(trg_percentile, axis=0)
        
        return percentile_df
    
    def calculate_percentiles(self):
        
        for prs_name, df in self.prbArgLogs.getDataFrames().items():
            
            peak_cpu = self.getPeakCpu(df)
            peak_mem = self.getPeakMem(df)
            
            percentile_df = self.getPercentileLst(df, [0.5, 0.9, 0.95])
            
            print(percentile_df)
            
            
            
