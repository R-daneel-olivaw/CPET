'''
Created on Feb 24, 2015

@author: Akshat
'''

import time

class ProcRecord(object):
    '''
    classdocs
    '''


    def __init__(self, procCpu, procMem):
        self.cpu = procCpu
        self.mem = procMem
        self.recordTime = time.time()
        '''
        Constructor
        '''
    def getCpu(self):
        return self.cpu
    def getMem(self):
        return self.mem;
    def getTime(self):
        return self.recordTime
    def toSequence(self):
        seq = []
        seq.append(self.getTime())
        seq.append(self.getCpu())
        seq.append(self.getMem())
        
        return seq
        