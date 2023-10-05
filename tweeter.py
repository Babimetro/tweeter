# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:32:33 2023

@author: babimetro
"""

import requests
import re
import time
from bs4 import BeautifulSoup as bs

url='https://basalam.com/search/subcategory/rice?page=1'




url1='''https://twitter.com/search?q=iran'''
url2='''https://yahoo.com'''
url3='''https://www.digikala.com/'''
http_proxy = "http://127.0.0.1:65222"
https_proxy = "http://127.0.0.1:65222"
socks='''127.0.0.1:65223'''

proxies = {
"http" : http_proxy,
"https" : https_proxy
}


r1=requests.get(url1,proxies=proxies)
print(r1)
soup=bs(r1.text,'html.parser')
tweets=[p.text for p in soup.findAll('p',calss_='tweet-text')]
print(tweets)


'''url=u'https://twitter.com/search?q='
query=u'salam&page=1'
urlll=url+query
 
#http=127.0.0.1:58608;https=127.0.0.1:58608;socks=127.0.0.1:58607
http_proxy = "http://127.0.0.1:62115"
https_proxy = "https://127.0.0.1:58608"


proxies = {
"http" : http_proxy
}
r=requests.get()
soup=bss(r.text,'html.parser')
tweets=[p.text for p in soup.findAll('p',class_='tweet-text')]
print(tweets)
'''


'''If you'd like to persisist cookies and session data, you'd best do it like this:

import requests

proxies = {
    'http': 'http://user:pass@10.10.1.0:3128',
    'https': 'https://user:pass@10.10.1.0:3128',
}

# Create the session and set the proxies.
s = requests.Session()
s.proxies = proxies

# Make the HTTP request through the session.
r = s.get('http://www.showmemyip.com/')'''