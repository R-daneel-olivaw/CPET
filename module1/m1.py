'''
Created on Mar 6, 2015

@author: Akshat
'''
process_names = None

output_path = None

process_pid = None


def parse_config(ini_path):
    
    config = configparser.ConfigParser()
    config.sections()
    config.read(ini_path)
    
    m1_config = config['m1']
    
    global process_names
    process_names = m1_config['process_name_list'].split(',')
    global output_path
    output_path = m1_config['output_path']
    global process_pid
    process_pid = m1_config['pid_list'].split(',')
    
def exem1():
    
    parse_config('../cpet_config.ini')
    print('process_names = ',process_names)
    print('output_path = ',output_path)
    print('pid_list = ', process_pid)
    
    ProbeThreadController(process_names, process_pid, output_path).start_probes()
    

if __name__ == '__main__':
    from module1.probe_thread_controller import ProbeThreadController
    import configparser
    exem1()
