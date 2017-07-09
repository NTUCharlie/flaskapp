from bs4 import BeautifulSoup
import urllib.request
import urllib
from http.cookiejar import CookieJar
url = 'https://www.pornhub.com/video'

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
alllink=[]
for link in all_a:
    strlink = link.get('href')
    a_string = link.string
    if link.string!= None:
        alllink.append([strlink,a_string])
    else:
        continue

def purify(list):
    newlink=[]
    for pair in list:
        if "/view_video.php?" in str(pair[0]):
            newlink.append(pair)
        else:
            continue
    return newlink



def get_id(strlink):
    temlist=[]
    temlist=strlink.split('=')
    return str(temlist[-1])

finallist=[]
for item in purify(alllink):
    finallist.append([get_id(item[0]),item[1]])
print(finallist)




