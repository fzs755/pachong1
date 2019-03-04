# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
import sys
import time
import json
#headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
a= 'https://sellercentral.amazon.com/forums/c/selling-on-amazon/general-selling-questions/l/latest?no_subcategories=false&page=3&slow_platform=20&_=1547707269919'
# p = __import__('selenium.webdriver.chrome.webdriver',fromlist=('WebDriver'))
# b= 'guobie.shtml'
response = request.urlopen(a)
html_doc = response.read()
soup = BeautifulSoup(html_doc,"html.parser")
data = response.json()
browser=webdriver.Firefox()
browser.get(a)
i=0
for i in range(0,5): 
  browser.execute_script("window.scrollBy(0,3000)")
  i=i+1
  time.sleep(2)
for link in soup.find_all('span',attrs={"itemprop":"name"}):
  z=link.get_text()
  with open ('amazon.txt','a+',encoding='utf-8') as g:
    g.write(z+'\n')

#browser.close()

#f = open('amazon.txt','a+',encoding='utf-8')
#for link in soup.find_all('a',):
#    print(link.get('href'))
#    f.write (link.get('href')+'\n')     
#f.close()