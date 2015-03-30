'''
Created on Mar 3, 2015

@author: Akshat
'''
from pandas.core.frame import DataFrame
from module2.ds.process_report import SingleProcessReport, ProcessReportDitionary
import module2.dicttoxml.dicttoxml as dicttoxml

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
        
        rep_dict = ProcessReportDitionary()
        
        for prs_name, df in self.prbArgLogs.getDataFrames().items():
            
            percentile_df = self.getPercentileLst(df, [0.5, 0.75, 0.9, 0.95, 1])
            percentile_dict = percentile_df.T.to_dict('dict')
            
            peak_dict = percentile_dict[1]
            percentile_50_dict = percentile_dict[0.5]
            percentile_75_dict = percentile_dict[0.75]
            percentile_90_dict = percentile_dict[0.9]
            percentile_95_dict = percentile_dict[0.95]
           
            s_rep = {}
            s_rep['peak'] = peak_dict
            s_rep['percentile_50'] = percentile_50_dict
            s_rep['percentile_75'] = percentile_75_dict
            s_rep['percentile_90'] = percentile_90_dict
            s_rep['percentile_95'] = percentile_95_dict
            
            rep_dict.addProcessReport(s_rep, prs_name)
        
        xml = str(dicttoxml.dicttoxml(rep_dict.getAllProcessReport(), attr_type=False), 'utf-8')
        
        return xml
            
            
            
