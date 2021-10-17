import requests
from bs4 import BeautifulSoup as Bs
DATA_URL = 'https://habr.com/ru'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
SOURCE = requests.get(DATA_URL).text

soup = Bs(SOURCE, features='lxml')

articles = soup.find_all('article')
for article in articles:
    title = article.find(class_="tm-article-snippet__title-link").text
    link = article.find(class_="tm-article-snippet__title-link").attrs['href']
    text = article.find_all(class_="tm-article-body tm-article-snippet__lead")
    for el in text:
        for word in KEYWORDS:
            if word in el.text.lower():
                print(article.find('time').text, '-', title, '-', DATA_URL[0:16] + link)
