import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "http://books.toscrape.com/"


response = requests.get(url)
html_content = response.content


soup = BeautifulSoup(html_content, 'html.parser')


book_names = []
book_prices = []
book_ratings = []


books = soup.find_all('article', class_='product_pod')

for book in books:
    
    name = book.h3.a['title']
    book_names.append(name)

    
    price = book.find('p', class_='price_color').text
    book_prices.append(price)

    
    rating = book.p['class'][1]
    book_ratings.append(rating)


books_data = pd.DataFrame({
    'Book Name': book_names,
    'Price': book_prices,
    'Rating': book_ratings
})


books_data.to_csv('books_data.csv', index=False)

print("Scraping completed. Data saved to 'books_data.csv'.")
