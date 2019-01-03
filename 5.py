from bs4 import BeautifulSoup
from urllib import request
import sys

y=[]
f = open('f.txt','r',encoding='utf-8')
y = f.readlines()
_headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"}
for x in y:
  req=request.Request(x,headers=_headers)
  response = request.urlopen(req,timeout=240)
  html_doc = response.read()
  #soup = BeautifulSoup(html_doc,"html.parser")
  if ('404') in response.geturl():
   print(x+'error')  
f.close()