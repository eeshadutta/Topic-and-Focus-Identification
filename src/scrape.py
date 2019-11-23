import requests 
from bs4 import BeautifulSoup 
import csv 
  
URL = "https://timesofindia.indiatimes.com/india/ajit-pawar-sacked-as-ncps-legislature-party-leader/articleshow/72200803.cms"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
  
lines = []
  
table = soup.find('div', attrs = {'id':'container'}) 
  
for row in table.findAll('div', attrs = {'class':'quote'}): 
    quote = {} 
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.h6.text 
    quote['author'] = row.p.text 
    quotes.append(quote) 