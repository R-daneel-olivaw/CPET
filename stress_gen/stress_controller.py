'''
Created on Apr 6, 2015

@author: Akshat
'''
import multiprocessing
from threading import Thread
import subprocess
import time
import sys

class StressController:
    '''
    classdocs
    '''
    
    process_list = []

    def __init__(self, shell_command, process_count, stress_timeout):
        '''
        Constructor
        '''
        self.shell_command = shell_command
        self.process_count = process_count
        self.stress_timeout = stress_timeout
        
    def i_stress(self, command):
        
        pipe = subprocess.Popen(['bash', command])
        self.process_list.append(pipe.pid)
        
    def start_stress(self):
        
        self.parse_config(self.ini_path)
        
        for i in range(1, self.process_count):
            
            worker = Thread(target=self.i_stress(self.shell_command))   
            worker.start()  
        
        return self.process_list       
        
    def stop_all(self):
        
        for p in self.process_list:
            p.terminate()
        
        
        
