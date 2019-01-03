
from bs4 import BeautifulSoup
from urllib import request
import sys
import urllib
import time

y=[]
f = open('c.txt','r',encoding='utf-8')
y = f.readlines()
i=0
for x in y:
  i=i+1
  response = request.urlopen(x,timeout=60)
  html_doc = response.read()
  soup = BeautifulSoup(html_doc,"html.parser")  
  #print(response.getcode())
  if (i%100==0):
    time.sleep(100)
  if ('404') in response.geturl():
      with open ('f.txt','a+', encoding='utf-8') as g2:
          g2.write(x+'\n') 
      continue
  else:  
    for link in soup.find_all('a', attrs={"target":"_blank"}):
      x=x.strip()
      l=link.get('href')
      t=link.get_text()
      z=""
    #print(urllib.request.urlopen(x).getcode())         
      if (response.getcode()==200) :
        if (l.find("2019")!=-1):
          z=x+l.replace("/article/sqfb","",1)+t
          with open ('2019.txt','a+', encoding='utf-8') as g1:
            g1.write(z+'\n')
      else:
        print(response.getcode())
         
  #  if(l+x1):
   #   soup1=BeautifulSoup(request.urlopen(l+x1),"html.parser")
    #  for link1 in soup1.find_all('a', attrs={"target":"_blank"}):
     #   print(link1.get_text())
        #f.write (link1.get('href')+'\n')     
f.close()