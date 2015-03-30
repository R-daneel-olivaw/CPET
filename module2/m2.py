'''
Created on Mar 6, 2015

@author: Akshat
'''
output_directory_path = 'C:/Users/Akshat/git/CPET/output/m2'

def exem2():
    probeAgg = PrbLogAgg(output_directory_path, csvFilePath=['C:/Users/Akshat/git/CPET/output/m1/chrome.exe.csv', 'C:/Users/Akshat/git/CPET/output/m1/thunderbird.exe.csv','C:/Users/Akshat/git/CPET/output/m1/eclipse.exe.csv'])
    probeAgg.loadDataFrame()

    a = Analyst(probeAgg)
    # print(df)

    report_dict = a.calculate_percentiles()
    dom = parseString(report_dict)
    print(dom.toprettyxml())
    
    with open(output_directory_path + "/Output.xml", "w+") as text_file:
        print(dom.toprettyxml(), file=text_file)
    # print(percentile_df.describe())
    # print('Percentile = /n', percentile_df)

if __name__ == '__main__':
    from module2.ProbeLogAggregator import PrbLogAgg
    from module2.toolkit.dfAnalyst1 import Analyst
    from xml.dom.minidom import parseString
    exem2()
