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

    def __init__(self, process_names, output_path):
        '''
        Constructor
        '''
        self.process_names = process_names
        self.output_path = output_path
    
    def start_probes(self):
        
        for process in self.process_names:      
        
            print(process)  
        
            probe1 = ProcessProbe(process, self.output_path, 0.5)
            worker = Thread(target=probe1.startProbe)
            worker.start()
            
            self.worker_list.append(worker)
        
        for worker in self.worker_list:
            worker.join()
        
