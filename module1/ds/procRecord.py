'''
Created on Feb 24, 2015

@author: Akshat
'''

import time

class ProcRecord(object):
    '''
    classdocs
    '''


    def __init__(self, procCpu=None, procMem=None, procReadCount=None, procWriteCount=None, procReadb=None, procWriteb=None, procNetConnCount=None, procChildCount=None):
        self.cpu = procCpu
        self.mem = procMem
        self.readc = procReadCount
        self.writec = procWriteCount
        self.readb = procReadb
        self.writeb = procWriteb
        self.recordTime = time.time()
        self.netConnCount = procNetConnCount
        self.childCount = procChildCount
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
    def getConnectionCount(self):
        return self.netConnCount
    def getChildCount(self):
        return self.childCount
    
    def setCpu(self,cpu):
        self.cpu = cpu
    def setMem(self,mem):
        self.mem = mem
    def setReadc(self,readc):
        self.readc = readc
    def setWritec(self,writec):
        self.writec = writec
    def setReadb(self, readb):
        self.readb = readb
    def setWriteb(self, writeb):
        self.writeb = writeb
    def setTime(self, recordTime):
        self.recordTime = recordTime
    def setConnectionCount(self, netConnnCount):
        self.netConnCount = netConnnCount
    def setChildCount(self, childCount):
        self.childCount = childCount    
        
    def addCpu(self,cpu):
        self.cpu += cpu
    def addMem(self,mem):
        self.mem += mem
    def addReadc(self,readc):
        self.readc += readc
    def addWritec(self,writec):
        self.writec += writec
    def addReadb(self, readb):
        self.readb += readb
    def addWriteb(self, writeb):
        self.writeb += writeb
    def addTime(self, recordTime):
        self.recordTime += recordTime
    def addConnectionCount(self, netConnnCount):
        self.netConnCount += netConnnCount
    def addChildCount(self, childCount):
        self.childCount += childCount  
    
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
        seq.append(self.getConnectionCount())
        seq.append(self.getChildCount())
        # CSV sequence
        
        return seq
        
