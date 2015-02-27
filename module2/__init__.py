from module2.ProbeLogAggregator import PrbLogAgg

probeAgg = PrbLogAgg('D:/Lectures/Winter2015/CS854/project/PickelTest/vlc.exe.csv')
probeAgg.loadDataFrame()
df = probeAgg.getDataFrame()

print(df)
