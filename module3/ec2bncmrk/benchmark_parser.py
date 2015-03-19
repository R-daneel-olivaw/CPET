'''
Created on Mar 19, 2015

@author: Akshat
'''
from lxml import etree

class CloudlookParser(object):
    '''
    classdocs
    '''
    
    def start(self):
        
        s = '<table><tr><th>Event</th><th>Start Date</th><th>End Date</th></tr><tr><td>a</td><td>b</td><td>c</td></tr><tr><td>d</td><td>e</td><td>f</td></tr><tr><td>g</td><td>h</td><td>i</td></tr></table>'
        table = etree.XML(s)
        rows = iter(table)
        headers = [col.text for col in next(rows)]
        for row in rows:
            values = [col.text for col in row]
            print(dict(zip(headers, values)))

    def __init__(self):
        '''
        Constructor
        '''        