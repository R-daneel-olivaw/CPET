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
    worker_list=[]

    def __init__(self, process_names):
        '''
        Constructor
        '''
        self.process_names = process_names
    
    def start_probes(self):
        
        for process in self.process_names:      
        
            print(process)  
        
            probe1 = ProcessProbe(process,1)
            worker = Thread(target=probe1.startProbe)
            worker.start()
            
            self.worker_list.append(worker)
        
        for worker in self.worker_list:
            worker.join()
        