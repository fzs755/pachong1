
from bs4 import BeautifulSoup
from urllib import request
import sys
import urllib

y=[]
f = open('c.txt','r',encoding='utf-8')
y = f.readlines()
for x in y:
  #  print (x)
  response = request.urlopen(x)
  html_doc = response.read()
  soup = BeautifulSoup(html_doc,"html.parser")
  for link in soup.find_all('a', attrs={"target":"_blank"}):
    x=x.strip()
    l=link.get('href').replace("/article/sqfb","",1)
    t=link.get_text()
    z=""
    #print(urllib.request.urlopen(x).getcode())
    if (response.getcode()==200):
      #print(x+'有问题')
      #break
      if (l.find("2018")!=-1):
        z=x+l+t
      #print(z)
        with open ('d.txt','a+', encoding='utf-8') as g:
          if (z!=""):
            g.write(z+'\n')
    else:
      print(x+'有问题')    
  #  if(l+x1):
   #   soup1=BeautifulSoup(request.urlopen(l+x1),"html.parser")
    #  for link1 in soup1.find_all('a', attrs={"target":"_blank"}):
     #   print(link1.get_text())
        #f.write (link1.get('href')+'\n')     
f.close()