import requests
from bs4 import BeautifulSoup
import json


def fetch_books(page_number):
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())


def main():
    fetch_books(1)


if __name__ == "__main__":
    main()
