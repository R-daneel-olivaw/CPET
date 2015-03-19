import urllib.request
from lxml import html

class CloudlooFetcher(object):
    
    def __init__(self):
        self.cloud_look_aws_url = 'http://www.cloudlook.com/amazon-ec2-instance-types'

    def fetch_html(self):
           
        response = urllib.request.urlopen(self.cloud_look_aws_url)
        html_text = response.read()
        
        tree = html.fromstring(html_text, self.cloud_look_aws_url)
        table_html = tree.xpath('//table[@class="table table-condensed front-stats"]')
        
        return str(html.tostring(table_html[0]), 'UTF8')