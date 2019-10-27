from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://news.ycombinator.com/news')
bs = BeautifulSoup(html, 'html.parser')


for titel in titels:
    print(titel.get('href'))
print(len(titels))
