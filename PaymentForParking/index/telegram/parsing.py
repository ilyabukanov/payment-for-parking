import requests
from bs4 import BeautifulSoup

url = 'https://friendly-vampirebat-28.loca.lt'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='adress')

for quote in quotes:
    print(quote.text)