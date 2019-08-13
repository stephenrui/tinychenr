
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 00:08:08 2019

@author: Stephen
"""

import requests
import re
from bs4 import BeautifulSoup


r = requests.get('http://money.cnn.com/data/dow30/')
patern_1 = re.compile('class="wsod_symbol">(.*?)<\/a>')
patern_2 = re.compile('<span title="(.*?)">')
patern_3 = re.compile('<span stream="last_[0-9]*?" class="wsod_stream">(.*?)<\/span><\/td>')
symbol = re.findall(patern_1,r.text)
name = re.findall(patern_2,r.text)
price = re.findall(patern_3,r.text)
for result in zip(symbol,name,price):
    print(result)
