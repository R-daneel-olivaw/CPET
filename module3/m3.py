'''
Created on Mar 19, 2015

@author: Akshat
'''

def run_m3():
    clf = CloudlooFetcher()
    table_html = clf.fetch_html()
    
    table_html = table_html.replace("\n", "").replace("\t", "").strip()
    
    clp = CloudlookParser(table_html).start()
    print(clp)

if __name__ == '__main__':
    from module3.ec2bncmrk.benchmark_parser import CloudlookParser
    from module3.ec2bncmrk.benchmark_fetcher import CloudlooFetcher
    run_m3()
