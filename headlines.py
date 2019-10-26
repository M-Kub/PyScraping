from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://news.ycombinator.com/news')
bs = BeautifulSoup(html, 'html.parser')

"""for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)"""
titels = bs.find_all('a',
    {'href': re.compile('https://*')})

for titel in titels:
    print(titel.get('href'))
print(len(titels))
