from bs4 import BeautifulSoup
import urllib.request
import urllib
from http.cookiejar import CookieJar
url = 'https://www.pornhub.com'

req = urllib.request.Request(url, headers={'ACCEPT':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                                         'ACCEPT_ENCODING' : 'gzip, deflate, sdch, br',
                                         'ACCEPT_LANGUAGE' : 'zh-CN,zh;q=0.8,en;q=0.6',
                                         'cache-control':'max-age=0',
                                         'CONNECTION' : 'keep-alive',
                                         'REFERER' : 'https://www.google.com/',
                                         'HOST' : 'www.pornhub.com',
                                         'upgrade-insecure-requests' :'1',
                                        })
cj=CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
f=opener.open(req)
html_content = f.read().decode('utf-8')

soup=BeautifulSoup(html_content,"lxml")
all_a=soup.find_all('a')
for link in all_a:
    try:
        if 'view_video' in link.get('href'):
            print(link.get('href')+'\n')
    except:
        continue
