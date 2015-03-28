'''
Created on Feb 25, 2015

@author: Akshat
'''

import psutil
from module1.ds.procRecord import ProcRecord
from time import sleep
import csv
import os, platform, subprocess, re
from subprocess import check_output

class ProcessProbe:
    
    PROCNAME = None
    p_map = {}
    k_list = [0]
    o_map = {}
    
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


    def appendChildProcesses(self, proc_id):
        
        for p in proc_id:
            # try:
            c_process = psutil.Process(p)
            childs = c_process.children(recursive=True)
            for chp in childs:
                proc_id[p].append(chp.pid)
            proc_id[p] = list(set(proc_id[p]))
        '''
            except:
                print('process ', p, 'lost')
                continue
        '''    
    

    def get_process(self, p):
        
        if p not in self.o_map:
            pr = psutil.Process(p)
            self.o_map[p] = pr            
        
        return self.o_map[p]
    
    def get_processor_speed(self):
        if platform.system() == "Windows":
            pro_info = check_output("wmic cpu get name,CurrentClockSpeed,MaxClockSpeed", shell=True)
            pro_info = str(pro_info, "utf-8")
            pro_info = pro_info.splitlines()[2]
            
            pro_info = pro_info.split(sep=None, maxsplit=1)[0].strip()
            return int(pro_info)
        elif platform.system() == "Darwin":
            import os
            os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
            command = "sysctl -n machdep.cpu.brand_string"
            print('os not supported')
            print(subprocess.check_output(command).strip())
            return 100
        elif platform.system() == "Linux":
            command = "cat /proc/cpuinfo"
            all_info = subprocess.check_output(command, shell=True).strip()
            for line in all_info.split("\n"):
                if "model name" in line:
                    print('os not supported')
                    print(re.sub(".*model name.*:", "", line, 1))
                    return 100
        print('os not supported')
        return 100
    
    
    def probe_process(self, p, rec):
        # TODO: implement
        
        proc = self.get_process(p)
        try:                                    
            cpu = proc.get_cpu_percent(interval=0)
            cpu_speed = self.get_processor_speed()
            cpu = float("{0:.2f}".format(cpu_speed * (cpu / 100)))
            
            mem = proc.get_memory_info()[0] / float(2 ** 20)    
                            
            diskIo = proc.get_io_counters()
            disk_rc = diskIo[0]
            disk_wc = diskIo[1]
            disk_rb = diskIo[2]
            disk_wb = diskIo[3]
            
            netc = len(proc.connections())
            
            if not rec:
                rec = ProcRecord(cpu, mem, disk_rc, disk_wc, disk_rb, disk_wb, netc, 0)
            else:
                rec.addCpu(cpu)
                rec.addMem(mem)
                rec.addReadc(disk_rc)
                rec.addWritec(disk_wc)
                rec.addReadb(disk_rb)
                rec.addWriteb(disk_wb)
                rec.addConnectionCount(netc)
                rec.addChildCount(1)
                                    
            print(p, 'cpu = ', cpu)
            print(p, 'memory = ', mem)
            print(p, 'disk_read_count = ', diskIo[0])
            print(p, 'disk_write_count = ', diskIo[1])
            print(p, 'disk_read_bytes = ', diskIo[2])
            print(p, 'disk_write_bytes = ', diskIo[3])
            print(p, 'network counters = ', netc)
            print()
                
        except:
            print("process lost..")
            self.k_list.append(p)
        
        return rec
    
    
    def startProbe(self):
        
        print('STARTING PROBE FOR ',self.PROCNAME)
        
        parent_id = self.getPidForProcessName(self.PROCNAME)
        # parent_id = 7832
        self.p_map[parent_id] = [parent_id]
        
        # self.procId.append(self.getPidForProcessName(self.PROCNAME))
        
        print(self.p_map)
                
                # print(proc)
                # print(proc.cpu_times())
        try:
            
            fileCsv = None
            while True:
                
                self.appendChildProcesses(self.p_map)
                
                buffer = {}
                for parent in self.p_map:
                    if psutil.pid_exists(parent) and parent != 0:
                        buffer[parent] = self.p_map[parent]
                
                self.p_map = buffer
                
                if not self.p_map:
                    break
                
                for parent in self.p_map:
                    
                    fileCsv = open('D:/Lectures/Winter2015/CS854/project/PickelTest/' + self.PROCNAME + '.csv', 'a')
                    writer = csv.writer(fileCsv, delimiter=',', quoting=csv.QUOTE_NONE, lineterminator='\n')
                    
                    
                    if(parent not in self.k_list):
                        
                        if psutil.pid_exists(parent):                            
                            p_childs = self.p_map[parent]                            
                            rec = None
                            for p in p_childs:                                 
                                if(p not in self.k_list):                                                             
                                    rec = self.probe_process(p, rec)                            
                            self.addToCSV(writer, rec)
                                    
                        else:
                            print('parent lost')
                            self.k_list.append(parent)
                            continue
                        
                sleep(self.stepDelay)
        
        finally:
            if fileCsv:
                fileCsv.close()
        print("Terminating...")
        
    
