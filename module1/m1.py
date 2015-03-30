'''
Created on Mar 6, 2015

@author: Akshat
'''
process_names = ['chrome.exe', 'thunderbird.exe', 'eclipse.exe']

output_path = 'C:/Users/Akshat/git/CPET/output/m1/'

def exem1():
    
    ProbeThreadController(process_names, output_path).start_probes()
    

if __name__ == '__main__':
    from module1.probe_thread_controller import ProbeThreadController
    exem1()
