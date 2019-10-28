from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


def getLink(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        links = bs.find_all('a', {'href': re.compile('https://*')})
    except AttributeError:
        return None
    return links


def adresse(self):
    liste = getLink(self)
    for link in liste:
        print(link.get('href'))
    print(len(liste))


adresse('https://www.zeit.de/index')
