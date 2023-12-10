import requests
from bs4 import BeautifulSoup

def scrape_gutenberg_india():
    base_url = "http://www.gutenberg.org/1/1/3/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    for link in soup.find_all('a', {'class': 'extiw'}):
        title = link.get_text()
        href = link.get('href')
        if "/ebooks/" in href:
            books.append({'title': title, 'url': f"http://www.gutenberg.org{href}"})

    return books
