import re
import requests
from bs4 import BeautifulSoup
import urllib.request as u
import os
import shutil
import urllib.parse as p
import urllib.request as req

url='http://www.newcovenantinstitute.net/living_god_ministries/radio_archive/choosing_the_disciples.htm'
outfiledir='F:/'
outfiledir='C:/Users/Administrator/Desktop/lgm temp/'

url_store_path=os.path.dirname(url)

result=requests.get(url)
c = result.content
soup=BeautifulSoup(c)

links = [a['href'] for a in soup.find_all('a',href=re.compile('\.mp3'))]
total=len(links)
for count,i in enumerate(links):
    httpname=url_store_path+'/'+i
    outfilename=os.path.join(outfiledir,i.split('/')[-1])
    u.urlretrieve(httpname,outfilename)
    print(str(count+1)+' out of '+str(total))

    
    
url2='http://www.newcovenantinstitute.net/living_god_ministries/radio_archive/index.htm'  
result2=requests.get(url2)
c2 = result2.content
soup2=BeautifulSoup(c2)
links = [a['href'] for a in soup2.find_all('a',href=re.compile('\.htm')) if str(a['href']).startswith('http://www.')!=True]
