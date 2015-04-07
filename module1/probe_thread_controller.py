'''
Created on Mar 28, 2015

@author: Akshat
'''

from module1.probes.Pobe import ProcessProbe
from threading import Thread

class ProbeThreadController(object):
    '''
    classdocs
    '''
    worker_list = []

    def __init__(self, process_names, process_pid, output_path):
        '''
        Constructor
        '''
        self.process_pid = process_pid
        self.process_names = process_names
        self.output_path = output_path
    
    def start_probes(self):
        
        for process in self.process_names:      
        
            print(process)  
        
            probe1 = ProcessProbe(process, pid=None, output_path=self.output_path, stepDelay=0.5)
            worker = Thread(target=probe1.startProbe)
            worker.start()
            
            self.worker_list.append(worker)
            
        for process in self.process_pid:
            
            print(process)  
        
            probe1 = ProcessProbe(processName=None, pid=process, output_path=self.output_path, stepDelay=0.5)
            worker = Thread(target=probe1.startProbe)
            worker.start()
            
            self.worker_list.append(worker)
        
        for worker in self.worker_list:
            worker.join()
        
