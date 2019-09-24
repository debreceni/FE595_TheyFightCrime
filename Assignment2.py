# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:24:56 2019

@author: Dave
"""

import requests
from bs4 import BeautifulSoup as bsoup
import re

regex = r"(?=(He's))(?P<HE>.*)(?=(She's))(?P<SHE>.*)(?=They fight crime!)"
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
        p = "".join([str(item) for item in tag.contents])
        matches = re.search(regex, p, re.MULTILINE)
        helist.append(matches.group('HE').strip())
        shelist.append(matches.group('SHE').strip())
        
        
with open(hefile,'w') as f:
    f.writelines("%s\n" % c for c in helist)


with open(shefile,'w') as f:
    f.writelines("%s\n" % c for c in shelist)