from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())


def getLinks(articleURL):
    html = urlopen('https://en.wikipedia.org{}'.format(articleURL))
    bs = BeautifulSoup(html, 'html.parser')
    article = bs.find_all('a', {'href': re.compile('^(/wiki/)((?!:).)*$')})
    return article


def adresse(self):
    links = getLinks(self)
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)


adresse('/wiki/Kevin_Bacon')
