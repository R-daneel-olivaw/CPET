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
        
    def plotGraph(self, df, clm, collumn_name, file_name):
        
        # Set some Pandas options
        pd.set_option('display.notebook_repr_html', False)
        pd.set_option('display.max_columns', 20)
        pd.set_option('display.max_rows', 25)
        
        # For Graph Plot
        # df.plot(subplots=True, figsize=(20, 60)); plt.legend(loc='best')
        
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)  # one row, one column, first plot
        ax.set_title(collumn_name + " vs. Time")
        ax.set_xlabel("Time")
        ax.set_ylabel(collumn_name)
        ax.scatter(df.time, clm, alpha=0.5, edgecolors='none') 
        ax.set_ylim(1)
        ax.set_xlim(df.time.max(), df.time.min())
        ax.invert_xaxis()
        fig.savefig(self.output_directory + file_name + '.png', bbox_inches='tight')
        
    def loadDataFrame(self):
        for path in self.csv:
            df = pd.read_csv(path)
            self.dataFrame[self.path_leaf(path)] = df
            
        for f_name, i_df in self.dataFrame.items():
            
            i_df.columns = ['time', 'cpuperc', 'memmb', 'readcount', 'writecount', 'readbytes', 'writebyte', 'netConnCount', 'childProcCount']
            
            self.plotGraph(i_df, i_df.cpuperc, 'CPU', 'test_cpu')
            self.plotGraph(i_df, i_df.memmb, 'RAM', 'test_mem')
            self.plotGraph(i_df, i_df.readcount, 'Disk-read-count', 'test_dskRc')
            self.plotGraph(i_df, i_df.writecount, 'Disk-write-count', 'test_dskWc')
            self.plotGraph(i_df, i_df.readbytes, 'Disk-read-bytes', 'test_dskRb')
            self.plotGraph(i_df, i_df.writebyte, 'Disk-write-bytes', 'test_dskWb')
            self.plotGraph(i_df, i_df.netConnCount, 'Net-connection-count', 'test_netCon')
            self.plotGraph(i_df, i_df.childProcCount, 'Child-proc-count', 'test_childProc')
        
    def getDataFrame(self, logfile_name):
        
        return self.dataFrame[logfile_name]
    
    def getDataFrames(self):
        
        return self.dataFrame
    
    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
