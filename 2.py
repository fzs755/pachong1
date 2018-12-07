
from bs4 import BeautifulSoup
from urllib import request
import sys
a= 'http://www.mofcom.gov.cn/mofcom/'
b= 'guobie.shtml'
response = request.urlopen(a+b)
html_doc = response.read()
soup = BeautifulSoup(html_doc,"html.parser")
x1 = '/article/sqfb/'
f = open('a.txt','a+',encoding='utf-8')
for link in soup.find_all('a', attrs={"target":"_blank"}):
    print(link.get('href'))
    f.write (link.get('href')+'\n')     
f.close()
