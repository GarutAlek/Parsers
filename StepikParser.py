import requests
from bs4 import BeautifulSoup as BS
import json

headers = {'User-agent': 'Mozilla/5.0'}
url = 'https://stepik.org/catalog/2'
r = requests.get(url, headers = headers)
soup = BS(r.text, 'lxml')
quotes_names = soup.find_all('a', class_='course-card__title')
quotes_authors = soup.find_all('a', class_='course-card__author')
quotes_urls = soup.find_all('a', class_='course-card__title')
quotes_prices = soup.find_all('span', class_='display-price__price display-price__price_default')
result = []

for i in range(len(quotes_names)-2):
    tmp = {}
    tmp["name"] = quotes_names[i].text[7:-5]
    tmp["author"] = quotes_authors[i].text
    tmp["url"] = "stepik.org" + quotes_urls[i].get('href')
    tmp["price"] = quotes_prices[i].text
    result.append(tmp)

with open("res.json", "w", encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)