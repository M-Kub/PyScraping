from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen('https://cdn1.spiegel.de')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img',
    {'src': re.compile('/images/image.*.jpg')})

for image in images:
    print(image['src'])
print(len(images))

