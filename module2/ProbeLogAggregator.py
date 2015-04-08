'''
Created on Feb 26, 2015

@author: Akshat
'''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as mgrid
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
        
    def plotGraph(self, ax, df, clm, collumn_name):

        ax.set_title(collumn_name + " vs. Time")
        ax.set_xlabel("Time")
        ax.set_ylabel(collumn_name)
        ax.scatter(df.time, clm, alpha=0.5, edgecolors='none', s=5) 
        ax.set_ylim(1)
        ax.set_xlim(df.time.max(), df.time.min())
        ax.invert_xaxis()
        
    def big_plot(self, i_df, file_name):
        
        # Set some Pandas options
        pd.set_option('display.notebook_repr_html', False)
        pd.set_option('display.max_columns', 20)
        pd.set_option('display.max_rows', 25)
        
        # For Graph Plot
        # df.plot(subplots=True, figsize=(20, 60)); plt.legend(loc='best')
        plt.close('all')
        fig, ((ax0, ax1, ax2), (ax3, ax4, ax5)) = plt.subplots(nrows=2, ncols=3)
        
        fig.set_size_inches(15,5)
        gs = mgrid.GridSpec(2, 3) 

        ax0 = plt.subplot(gs[0, 0])
        ax1 = plt.subplot(gs[0, 1])
        ax2 = plt.subplot(gs[0, 2])
        ax3 = plt.subplot(gs[1, 0])
        ax4 = plt.subplot(gs[1, 1])
        ax5 = plt.subplot(gs[1, 2])
        
        self.plotGraph(ax0, i_df, i_df.cpuperc, 'CPU')
        
        self.plotGraph(ax1, i_df, i_df.memmb, 'RAM')
        
        self.plotGraph(ax2, i_df, i_df.readcount, 'Disk-read-count')
        
        self.plotGraph(ax3, i_df, i_df.writecount, 'Disk-write-count')
        
        self.plotGraph(ax4, i_df, i_df.readbytes, 'Disk-read-bytes')
        
        self.plotGraph(ax5, i_df, i_df.writebyte, 'Disk-write-bytes')
        
        # self.plotGraph(ax7, i_df, i_df.netConnCount, 'Net-connection-count')
        
        # self.plotGraph(ax0, i_df, i_df.childProcCount, 'Child-proc-count')
        
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        
        fig.savefig(self.output_directory + file_name + '.png', bbox_inches='tight')
        
    def loadDataFrame(self):
        for path in self.csv:
            df = pd.read_csv(path)
            self.dataFrame[self.path_leaf(path)] = df
            
        for f_name, i_df in self.dataFrame.items():
            
            i_df.columns = ['time', 'cpuperc', 'memmb', 'readcount', 'writecount', 'readbytes', 'writebyte', 'netConnCount', 'childProcCount']
            
        
        self.big_plot(i_df, 'big_plot')
            
    def getDataFrame(self, logfile_name):
        
        return self.dataFrame[logfile_name]
    
    def getDataFrames(self):
        
        return self.dataFrame
    
    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
