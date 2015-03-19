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
        
        s = self.html_table
        bm_rows=[]
        table = etree.XML(s)
        rows = iter(table)
        headers = [col.text for col in next(rows)]
        for row in rows:
            values = [col.text for col in row]
            bm_rows.append(dict(zip(headers, values)))
        
        return bm_rows

    def __init__(self, html_table):
        '''
        Constructor
        '''        
        self.html_table = html_table
