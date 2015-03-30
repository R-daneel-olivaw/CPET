'''
Created on Mar 6, 2015

@author: Akshat
'''
output_directory = 'C:\Users\Akshat\git\CPET\output\m2'

def exem2():
    probeAgg = PrbLogAgg(output_directory=output_directory, 'D:/Lectures/Winter2015/CS854/project/PickelTest/chrome.exe.csv', 'D:/Lectures/Winter2015/CS854/project/PickelTest/thunderbird.exe.csv')
    probeAgg.loadDataFrame()
    df = probeAgg.getDataFrame()

    a = Analyst(probeAgg)
    # print(df)
    print('Peak CPU = ', a.getPeakCpu())
    print('Peak Mem = ', a.getPeakMem())

    percentile_df = a.getPercentile(0.95)
    # print(percentile_df.describe())
    print('Percentile = \n', percentile_df)

if __name__ == '__main__':
    from module2.ProbeLogAggregator import PrbLogAgg
    from module2.toolkit.dfAnalyst1 import Analyst
    exem2()
