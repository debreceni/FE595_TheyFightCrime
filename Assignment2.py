# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:24:56 2019

@author: Dave
"""

import requests
from bs4 import BeautifulSoup as bsoup

myurl = 'https://theyfightcrime.org'
hefile = 'hefile.txt'
shefile = 'shefile.txt'

helist = []
shelist = []

#Get 50 Characters
for i in range(50):
    
    response = requests.get(myurl)
    if response.status_code == 200:
        site = bsoup(response.text, 'html.parser')
        tag = site.find_all('p')[1]
        p = "".join([str(item) for item in tag.contents]).split('.')
        helist.append(p[0].lstrip())
        shelist.append(p[1].lstrip())
        
        
with open(hefile,'w') as f:
    f.writelines("%s\n" % c for c in helist)


with open(shefile,'w') as f:
    f.writelines("%s\n" % c for c in shelist)