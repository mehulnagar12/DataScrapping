import requests
from bs4 import BeautifulSoup

page = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = BeautifulSoup(page.text,'html.parser')

Links = soup.find('table',{'class' : 'wikitable sortable'})
Tag = Links.find_all('tr')[1:]
#print(Tag)

for t in Tag:
    temp = t.find_all('td')[0]
    print(temp.text)