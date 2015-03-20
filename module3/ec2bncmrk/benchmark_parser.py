'''
Created on Mar 19, 2015

@author: Akshat
'''
from itertools import cycle

from bs4 import BeautifulSoup

import pandas as pd


class CloudlookParser(object):
    '''
    classdocs
    '''
    
    ec2_srv = []
    columns = []
    
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
        
       
        try:
            cells = rows[0].find_all('th')
            
            for cell in cells:
                c_txt = cell.get_text()
                if c_txt:
                    self.columns.append(c_txt)
            
            # print(self.columns)
            self.columns.remove('Cloud Server')
            rows.remove(rows[0])
            
        except AttributeError as e:
            print ('No table cells found, exiting')
            return 1
        
        for row in rows:
            # try:
            srv_name = row.find('th')
            if not srv_name:
                continue
            # print(srv_name.get_text())
            # print(row)
            
            srv_entry = {}
            srv_entry['Cloud Server'] = srv_name.get_text() 
            
            cells = row.find_all('td', text=lambda x: (len(x) > 0) if (x is not None) else False)
            # print(list(zip(self.columns, cells)))
            for di, cell in zip(self.columns, cells):
                
                srv_entry[di] = cell.get_text()
                # print( cell.get_text())
                # print(srv_entry[di])
            
            self.ec2_srv.append(srv_entry)
            # print('------')    
            # except AttributeError as e:
                # print ('No table cells found, exiting')
                # return 1
        df = self.convert_to_df(self.ec2_srv)
        
        return df
    
    def convert_to_df(self, dict_list):
        benchDf = pd.DataFrame()
        
        for rec in dict_list:
            benchDf = benchDf.append(rec, ignore_index=True)
        
        benchDf = benchDf.set_index('Cloud Server')
        
        return benchDf

    def __init__(self, html_table):
        '''
        Constructor
        '''        
        self.html_table = html_table
