'''
Created on Mar 6, 2015

@author: Akshat
'''
def exem1():
    probe1 = ProcessProbe('vlc.exe',0.2)
    probe1.startProbe()

if __name__ == '__main__':
    from module1.probes.Pobe import ProcessProbe
    exem1()
