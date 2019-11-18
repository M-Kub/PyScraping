from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen('https://news.ycombinator.com/')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a', {'class': 'storylink'}):
    if 'href' in link.attrs:
        print(link.attrs['href'])
