import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://en.wikipedia.org/wiki/'
        'List_of_United_States_cities_by_population')
bs = BeautifulSoup(html, 'html.parser')
table = bs.findAll('table', {'class': 'wikitable'})[1]
rows = table.findAll('tr')

csvFile = open('cities.csv', 'wt+')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['tr', 'td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)

finally:
    csvFile.close()
