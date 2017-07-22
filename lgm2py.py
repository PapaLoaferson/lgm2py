import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import re
import urllib.request as u
import os

def clickMe():
    action.configure(text='****DOWNLOADING****')
    download_list=[]
    for count,col in enumerate(range(len(links))):
        #exec('print(v'+str(count)+'.get())')
        exec('download_list.append(v'+str(count)+'.get())')
        #exec('print(v'+str(count)+'.get())')
    for count,i in enumerate(download_list):
        if i==1:
            lgmlookup(count)
#    
def lgmlookup(item):
    i=item
    httpnames=url2.split('index')[0]+links[i]
    result=requests.get(httpnames)
    c2 = result.content
    soup=BeautifulSoup(c2,"html5lib")
    linkers = [a['href'] for a in soup.find_all('a',href=re.compile('\.mp3'))]
    outfilename='C:/Users/ea696c/Desktop/lgm/lgm2py-master/lgm2py-master/'

    for jj in linkers: 
        print(outfilename+jj.split('/')[-1])
        u.urlretrieve('http://www.livinggodministries.net/living_god_ministries/radio_archive/'+jj,outfilename+jj.split('/')[-1])
    
    
    #http://www.newcovenantinstitute.net/living_god_ministries/radio_archive/index.htm
#      http://www.newcovenantinstitute.net/living_god_ministries/radio_archive/index.htm
url2='http://www.livinggodministries.net/living_god_ministries/radio_archive/index.htm'     
#url2='http:\\www.newcovenantinstitute.net\living_god_ministries\radio_archive\index.htm'  
result2=requests.get(url2)
c2 = result2.content
soup2=BeautifulSoup(c2,"html5lib")
links = [a['href'] for a in soup2.find_all('a',href=re.compile('\.htm')) if str(a['href']).startswith('http://www.')!=True]

link_names=[i.split('.')[0] for i in links]
link_names_pretty=tuple([i.split('.')[0].capitalize().replace('_',' ') for i in links])

win=tk.Tk()
win.title('Living God Ministries Download GUI')
number=tk.StringVar()
action=ttk.Button(win, text='Start Download',command=clickMe)
action.grid(column=0,row=2)

ttk.Label(win,text='Pick a Program Series from List Below:').grid(column=0,row=0)


for count,col in enumerate(range(len(links))):
    exec('v'+str(count)+'=tk.IntVar()')
    exec('v=tk.Checkbutton(win,text=link_names_pretty[col],variable=v'+str(count)+').grid(column=0,row=col+3,sticky=tk.W)')

win.mainloop()


#    
#  