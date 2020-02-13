import requests
from bs4 import BeautifulSoup

val_temp = []
term_temp = []
contents = []
name_arr = []
c = []
vals = []

page = requests.get('https://brickset.com/sets/year-2016')

soup = BeautifulSoup(page.text, 'html.parser')

links = soup.find('section',{'class' : 'setlist'})

Lists = links.find_all('h1')

Terms = links.find_all('dl')
Values = links.find_all('dl')

for ter in Terms:
    term = ter.find_all('dt')
    term_temp.append(term)
    
for val in Values:
    value = val.find_all('dd')
    val_temp.append(value)

for i in range (len(term_temp)):
    for k in term_temp[i]:
        contents.append(k.text)

for i in range (len(val_temp)):
    for v in val_temp[i]:
        vals.append(v.text)

for names in Lists:
    n = (names.find_all('a'))
    for j in n:
        print(j.text)