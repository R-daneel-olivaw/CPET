'''
Created on Mar 19, 2015

@author: Akshat
'''

def run_m3():
    clp = CloudlookParser('<table><tr><th>Event</th><th>Start Date</th><th>End Date</th></tr><tr><td>a</td><td>b</td><td>c</td></tr><tr><td>d</td><td>e</td><td>f</td></tr><tr><td>g</td><td>h</td><td>i</td></tr><tr><td>a</td><td>b</td><td>c</td></tr><tr><td>d</td><td>e</td><td>f</td></tr><tr><td>g</td><td>h</td><td>i</td></tr></table>').start()
    print(clp)

if __name__ == '__main__':
    from module3.ec2bncmrk.benchmark_parser import CloudlookParser
    run_m3()