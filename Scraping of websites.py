# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:18:51 2024

@author: User
"""


import requests 
from bs4 import BeautifulSoup 
  
def scraping(url):
    
    # Making a GET request 
    r = requests.get(url) 
      
    # Parsing the HTML 
    soup = BeautifulSoup(r.content, 'html.parser') 
      
    s = soup.find('h1', class_='entry-title')
    #In case of error trying different way
    if s is None:
        s=soup.find('h1', class_='tdb-title-text')
        # in some cases there is URL error
        if s is None:
            S="URL ERROR"
        else:
            S=s.text    
    else:
        S=s.text
    #print(s.text)
    
    #title over
    
    t=soup.find('div', class_='td-post-content tagdiv-type')
    if t is None:
        t=soup.find('div', class_='tdb-block-inner td-fix-index')
        if t is None:
            T="URL DOESN'T EXIST"
        else:
            T=t.text
    else:
        T=t.text
    #print(t.text)
    
    Lst=[S,T]
    return Lst

import pandas

csvFile = pandas.read_csv(r"C:\Users\User\Downloads\Input.xlsx - Sheet1.csv")
#print(csvFile)
#Creating 100 text files with the scraped data
for i in range(0,len(csvFile)):
    string='C:\\Users\\User\\Downloads\\Text Files\\'+csvFile['URL_ID'][i]
    file=open(string,"w",encoding="utf-8")
    file.writelines(scraping(csvFile['URL'][i]))
    file.close()