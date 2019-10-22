from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://www.spiegel.de')
bs = BeautifulSoup(html.read(), 'html.parser')
tagList = bs.find_all(['h3'])
for tag in tagList:
    print(tag.get_text())
print(len(tagList))
