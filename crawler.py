'''
Autor: socket8088
Date: 30/01/2017
Main crawler file
'''
from general import *
import requests
from bs4 import BeautifulSoup
import re


PROJECT_NAME = 'domain'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
OUTPUT_FILE = PROJECT_NAME + '/results.txt'
keyword = 'password'



def xcrawler(URL, keyword):
    source_code = requests.get(URL)
    if source_code.headers['content-type'] == 'text/html; charset=UTF-8':
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        code = soup.get_text()

        if re.search (keyword, code):
            print ('Keyword found! Match in URL: ' + URL)
            g.write(URL + '\n')


f = open (CRAWLED_FILE, 'r')
g = open (OUTPUT_FILE, 'w')
for line in f:
    URL = line.rstrip('\n')
    print ('Searching in ' + URL)
    xcrawler(URL, keyword)


f.close()
g.close()
print('Crawl process completed.')