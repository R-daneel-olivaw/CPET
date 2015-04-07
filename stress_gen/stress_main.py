'''
Created on Apr 6, 2015

@author: Akshat
'''

ini_path = '../cpet_config.ini'
proc_count = None
shell_command  = None

def parse_config(ini_path):
    
    config = configparser.ConfigParser()
    config.sections()
    config.read(ini_path)
    
    stress_config = config['stress_controller']
    
    global proc_count
    proc_count = int(stress_config['proc_count '])
    
    global shell_command 
    shell_command  = stress_config['shell_command ']
#     global output_path
#     output_path = stress_config['output_path']
#     global process_pid
#     process_pid = stress_config['pid_list'].split(',')

def trigg_stress():
    
    parse_config(ini_path)
    
    sc = StressController(shell_command,proc_count, 30)
    pid_list = sc.start_stress()
    
    print(pid_list)

if __name__ == '__main__':
    from stress_gen.stress_controller import StressController
    import configparser
    trigg_stress()
