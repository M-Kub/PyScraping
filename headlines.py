from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.spiegel.de')
bs = BeautifulSoup(html, 'html.parser')

"""for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)"""
titels = bs.find_all('span', {'class': 'headline'})

for titel in titels:
    print(titel.text)
print(len(titels))
