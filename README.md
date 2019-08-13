# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:40:26 2019

@author: Stephen
"""








import requests
import re
import time
from bs4 import BeautifulSoup

count = 0
i = 0
s,count_s,count_del = 0, 0, 0
lst_stars = []
while count <50:
    print('*****')
    try:
        r = requests.get('https://book.douban.com/subject/1084336/comments/')
    except Exception as err:
        print(err)
        break
    soup = BeautifulSoup(r.text,'lxml')
    comments = soup.find_all('span','short')
    pattern = re.compile('<span class="user-stars allstar(.*?) rating"')
    p = re.findall(pattern,r.text)
    
    for item in comments:
        count+=1
        if count>50:
            count_del+=1
        else:
            print(count,item.string)
    for star in p:
        lst_stars.append(int(star))
    time.sleep(5)
    i+=1
    for star in lst_stars[:-count_del]:
        s+=int(star)
    if count>=50:
        print(s//(len(lst_stars)-count_del))
        
    
