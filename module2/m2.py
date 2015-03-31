'''
Created on Mar 6, 2015

@author: Akshat
'''
output_file_path = None
input_log_file_path_list = None


def parse_config(ini_path):
    
    config = configparser.ConfigParser()
    config.sections()
    config.read(ini_path)
    
    m2_config = config['m2']
    
    global output_file_path
    output_file_path = m2_config['output_path']
    
    global input_log_file_path_list
    input_log_file_path_list = m2_config['input_log_file_path_list'].split(',')

def exem2():
    
    parse_config('../cpet_config.ini')
    
    print('output_file_path = ',output_file_path)
    print('input_log_file_path_list = ',input_log_file_path_list)
    
    probeAgg = PrbLogAgg(output_file_path, csvFilePath= input_log_file_path_list)
    probeAgg.loadDataFrame()

    a = Analyst(probeAgg)
    # print(df)

    report_dict = a.calculate_percentiles()
    
    m2o.generate_op(report_dict, output_file_path)
    
    # print(percentile_df.describe())
    # print('Percentile = /n', percentile_df)

if __name__ == '__main__':
    from module2.ProbeLogAggregator import PrbLogAgg
    from module2.toolkit.dfAnalyst1 import Analyst
    import module2.toolkit.m2_output as m2o
    import configparser
    exem2()
