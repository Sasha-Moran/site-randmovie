import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

def get_rating(html):
    soup = BeautifulSoup(html, 'lxml')
    rating = soup.find('div', class_='ratingValue').find('span').get_text()
    return rating

def imdb_rating(id):
    URL = f'https://www.imdb.com/title/tt{id}/'
    return get_rating(get_html(URL))

if __name__ == '__main__':
    imdb_rating('0099785')
