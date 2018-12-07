
from bs4 import BeautifulSoup
from urllib import request
import sys

response = request.urlopen('http://www.mofcom.gov.cn/mofcom/guobie.shtml')
html_doc = response.read()
soup = BeautifulSoup(html_doc,"html.parser")
x1 = '/article/sqfb/'
f = open('a.txt','a+',encoding='utf-8')
for link in soup.find_all('a', attrs={"target":"_blank"}):
    l=link.get('href')
    #t=link.get_text()    
    if(l+x1):
      soup1=BeautifulSoup(request.urlopen(l+x1),"html.parser")
      for link1 in soup1.find_all('a', attrs={"target":"_blank"}):
        print(link1.get_text())
        #f.write (link1.get('href')+'\n')     
f.close()
