'''
Created on Feb 25, 2015

@author: Akshat
'''

import psutil
from module1.ds.procRecord import ProcRecord
from time import sleep
import csv

class ProcessProbe:
    
    PROCNAME = "vlc.exe"
    procId = 0;
    
    def __init__(self, processName, stepDelay=0.5):
        self.PROCNAME = processName
        self.stepDelay = stepDelay

    def isMatch(self, proc, name):
        return name in repr(proc)
        
    def addToCSV(self, writer, mango):
        # writer.appe(mango.getTime(), mango.getCpu(), mango.getMem())
        seq = mango.toSequence()
        writer.writerow(seq)
        return
    
    def getPidForProcessName(self, procName):
        for proc in psutil.process_iter():
            if self.isMatch(proc, self.PROCNAME):
                # print(proc)
                procId = proc.pid
                return procId  
        return 0      
    
    def getProbeTargetName(self):
        return self.PROCNAME   

    def startProbe(self):
        procId = self.getPidForProcessName(self.PROCNAME)
        print(procId)
                
                # print(proc)
                # print(proc.cpu_times())
        if(procId != 0): 
            
            fileCsv = open('D:/Lectures/Winter2015/CS854/project/PickelTest/' + self.PROCNAME + '.csv', 'a')
            writer = csv.writer(fileCsv, delimiter=',', quoting=csv.QUOTE_NONE, lineterminator='\n')
            
            proc = psutil.Process(procId)
            
            try:
                for i in range(0, 150):
                    
                    cpu = proc.get_cpu_percent(interval=0)
                    mem = proc.get_memory_info()[0] / float(2 ** 20)                    
                    diskIo = proc.get_io_counters()
                    netc = len(proc.connections())
                                        
                    print(procId, 'cpu = ', cpu)
                    print(procId, 'memory = ', mem)
                    print(procId, 'disk_read_count = ', diskIo[0])
                    print(procId, 'disk_write_count = ', diskIo[1])
                    print(procId, 'disk_read_bytes = ', diskIo[2])
                    print(procId, 'disk_write_bytes = ', diskIo[3])
                    print(procId, 'network counters = ', netc)
                    print()
                    
                    rec = ProcRecord(cpu, mem, diskIo[0], diskIo[1], diskIo[2], diskIo[3],netc)
                    
                    sleep(self.stepDelay)
                    
                    self.addToCSV(writer, rec)
            except:
                print("process lost..")
            finally:
                if fileCsv:
                    fileCsv.close()
        print("Terminating...")


    
