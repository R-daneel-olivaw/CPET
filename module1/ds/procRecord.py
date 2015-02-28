'''
Created on Feb 24, 2015

@author: Akshat
'''

import time

class ProcRecord(object):
    '''
    classdocs
    '''


    def __init__(self, procCpu=None, procMem=None, procReadCount=None, procWriteCount=None, procReadb=None, procWriteb=None):
        self.cpu = procCpu
        self.mem = procMem
        self.readc = procReadCount
        self.writec = procWriteCount
        self.readb = procReadb
        self.writeb = procWriteb
        self.recordTime = time.time()
        '''
        Constructor
        '''
    def getCpu(self):
        return self.cpu
    def getMem(self):
        return self.mem;
    def getReadc(self):
        return self.readc;
    def getWritec(self):
        return self.writec;
    def getReadb(self):
        return self.readb;
    def getWriteb(self):
        return self.writeb;
    def getTime(self):
        return self.recordTime
    def toSequence(self):
        seq = []
        # CSV sequence
        seq.append(self.getTime())
        seq.append(self.getCpu())
        seq.append(self.getMem())
        seq.append(self.getReadc())
        seq.append(self.getWritec())
        seq.append(self.getReadb())
        seq.append(self.getWriteb())
        # CSV sequence
        
        return seq
        
