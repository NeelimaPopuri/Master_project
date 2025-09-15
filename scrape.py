import requests
from bs4 import BeautifulSoup
import json


def fetch_books(page_number):
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    book_elements = soup.find_all('article', class_='product_pod')

    for book in book_elements:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text
        print(price)


def main():
    fetch_books(1)


if __name__ == "__main__":
    main()
