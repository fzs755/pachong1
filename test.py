import requests

#headers = {'cookie':'', # 传入你的cookies
#           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

def get_page():
    r = requests.get('https://sellercentral.amazon.com/forums/c/selling-on-amazon/general-selling-questions/l/latest?no_subcategories=false&page=3&slow_platform=20&_=1547707269919')
    d = r.json()
    articles = d['articles']
    print(len(articles)) # 每次看抓取到了多少信息
    for article in articles:
        yield article['title']

def get_pages():
   for i in range(20):
       yield from get_page()

l = list(get_pages())
len(l)