'''
Created on Mar 6, 2015

@author: Akshat
'''
process_names = ['chrome.exe','thunderbird.exe']

def exem1():
    
    ProbeThreadController(process_names).start_probes()
    

if __name__ == '__main__':
    from module1.probe_thread_controller import ProbeThreadController
    exem1()
