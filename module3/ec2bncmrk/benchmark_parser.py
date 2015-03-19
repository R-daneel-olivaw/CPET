'''
Created on Mar 19, 2015

@author: Akshat
'''
from lxml import etree
from bs4 import BeautifulSoup

class CloudlookParser(object):
    '''
    classdocs
    '''
    
    def start(self):
        
        # Get table
        try:
            soup = BeautifulSoup(self.html_table)
            table = soup.find('table', {"class" : "table table-condensed front-stats"})
        except AttributeError as e:
            print ('No tables found, exiting')
            return 1
        
        # Get rows
        try:
            rows = table.find_all('tr')
            
        except AttributeError as e:
            print ('No table rows found, exiting')
            return 1
        
        for row in rows:
            try:
                cells = table.find_all('td')
                
                for cell in cells:
                    print(cell)
                
            except AttributeError as e:
                print ('No table cells found, exiting')
                return 1
        
        return 

    def __init__(self, html_table):
        '''
        Constructor
        '''        
        self.html_table = html_table
