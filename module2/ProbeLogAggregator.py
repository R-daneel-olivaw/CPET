'''
Created on Feb 26, 2015

@author: Akshat
'''
import pandas as pd
import matplotlib.pyplot as plt
import ntpath

class PrbLogAgg:
    '''
    classdocs
    '''
    
    dataFrame = {}
    csv = []

    def __init__(self, output_directory, csvFilePath):
        self.output_directory = output_directory
        self.csv = csvFilePath
        
    def plotGraph(self, df, file_name):
        
        # Set some Pandas options
        pd.set_option('display.notebook_repr_html', False)
        pd.set_option('display.max_columns', 20)
        pd.set_option('display.max_rows', 25)
        
        # For Graph Plot
        df.plot(subplots=True, figsize=(20, 60)); plt.legend(loc='best')
        plt.savefig(self.output_directory + file_name + '.png', bbox_inches='tight')
        
    def loadDataFrame(self):
        for path in self.csv:
            df = pd.read_csv(path)
            self.dataFrame[self.path_leaf(path)] = df
            
        for f_name, i_df in self.dataFrame.items():
            
            i_df.columns = ['time', 'cpuperc', 'memmb', 'readcount', 'writecount', 'readbytes', 'writebyte', 'netConnCount', 'childProcCount']
            
            self.plotGraph(i_df, 'test')
        
    def getDataFrame(self, logfile_name):
        
        return self.dataFrame[logfile_name]
    
    def getDataFrames(self):
        
        return self.dataFrame
    
    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
