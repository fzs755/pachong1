# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
import sys
a= 'https://sellercentral.amazon.com/forums/c/selling-on-amazon/general-selling-questions'
# p = __import__('selenium.webdriver.chrome.webdriver',fromlist=('WebDriver'))
# b= 'guobie.shtml'
response = request.urlopen(a)
html_doc = response.read()
soup = BeautifulSoup(html_doc,"html.parser")

browser=webdriver.Firefox()
browser.get("http://www.baidu.com")
print (browser.page_source)
#browser.close()

#f = open('amazon.txt','a+',encoding='utf-8')
#for link in soup.find_all('a',):
#    print(link.get('href'))
#    f.write (link.get('href')+'\n')     
#f.close()