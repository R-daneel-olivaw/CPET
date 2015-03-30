'''
Created on Mar 29, 2015

@author: Akshat
'''

class ProcessReportDitionary(object):
    '''
    classdocs
    '''
    
    multi_process_report_dict = None

    def __init__(self):
        '''
        Constructor
        '''
        self.multi_process_report_dict = {}
    
    def addProcessReport(self, single_process_report, process_name):
        
        self.multi_process_report_dict[process_name] = single_process_report
    
    def getProcessReport(self, process_name):
        
        return self.multi_process_report_dict[process_name]
    
    def getAllProcessReport(self):
        
        return self.multi_process_report_dict
#--------------------------------------------

class SingleProcessReport:
    
    def __init__(self, peak_value_dict, percentile_50_dict, percentile_90_dict, percentile_95_dict):
        self.peak_value_dict = peak_value_dict
        self.percentile_50_dict = percentile_50_dict
        self.percentile_90_dict = percentile_90_dict
        self.percentile_95_dict = percentile_95_dict
        
        