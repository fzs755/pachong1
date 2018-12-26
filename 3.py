from bs4 import BeautifulSoup
from urllib import request
import sys
import time
import urllib
user_headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36}'}
opener=urllib.request.build_opener()
y=[]
x=[]
with open('d:\\nodejs\\pachong\\pachong1\\a.txt','r') as f:
  y=f.readlines()
  s='/article/sqfb'
  for i in range(0,len(y)-1):
   y[i]=y[i].strip('\n')+s
   x.append(y[i])
#print(x)
f2 = open('c.txt','a+',encoding='utf-8')
for j in x:
  try:
    opener.open(j)
    print(j+'没问题')
    f2.write(j+'\n')
  except urllib.error.HTTPError:
    print(j+'无法访问')
    time.sleep(2)
  except urllib.error.URLError:
    print(j+'链接不存在')  
    time.sleep(2)
f2.close()
#with open('c.txt','a+') as f1:
  #for i in y[i]:
    #f1.write (y[i]+'\n')   