'''
Created on Feb 25, 2015

@author: Akshat
'''

import psutil
from module1.ds.procRecord import ProcRecord
from time import sleep
import csv

class ProcessProbe:
    
    PROCNAME = None
    procId = [];
    
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


    def getChildProcesses(self, proc_id):
        
        child_id = []
        for p in proc_id:
            try:
                c_process = psutil.Process(p)
                childs = c_process.children(recursive=True)
                for chp in childs:
                    child_id.append(chp.pid)
            except:
                print('process ', p, 'lost')
                continue
        
        return child_id
    
    
    def startProbe(self):
        self.procId.append(self.getPidForProcessName(self.PROCNAME))
        
        self.procId.append(self.getChildProcesses(self.procId))
        
        print(self.procId)
                
                # print(proc)
                # print(proc.cpu_times())
        for p in self.procId: 
            
            if(p==0):
                self.procId.remove(0)
                continue
            
            fileCsv = open('D:/Lectures/Winter2015/CS854/project/PickelTest/' + self.PROCNAME + '.csv', 'a')
            writer = csv.writer(fileCsv, delimiter=',', quoting=csv.QUOTE_NONE, lineterminator='\n')
            
            proc = psutil.Process(p)
            
            try:
                for i in range(0, 150):
                    
                    cpu = proc.get_cpu_percent(interval=0)
                    mem = proc.get_memory_info()[0] / float(2 ** 20)                    
                    diskIo = proc.get_io_counters()
                    netc = len(proc.connections())
                                        
                    print(p, 'cpu = ', cpu)
                    print(p, 'memory = ', mem)
                    print(p, 'disk_read_count = ', diskIo[0])
                    print(p, 'disk_write_count = ', diskIo[1])
                    print(p, 'disk_read_bytes = ', diskIo[2])
                    print(p, 'disk_write_bytes = ', diskIo[3])
                    print(p, 'network counters = ', netc)
                    print()
                    
                    rec = ProcRecord(cpu, mem, diskIo[0], diskIo[1], diskIo[2], diskIo[3], netc)
                    
                    sleep(self.stepDelay)
                    
                    self.addToCSV(writer, rec)
            except:
                print("process lost..")
                self.procId.remove(p)
            finally:
                if fileCsv:
                    fileCsv.close()
        print("Terminating...")


    
