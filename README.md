# Book Scraper

A simple web scraper that extracts book details (title, price, and rating) from [Books to Scrape](http://books.toscrape.com/) and saves the data in a CSV file.

## Features
- Scrapes book names, prices, and ratings.
- Saves data into `books_data.csv`.
- Uses **requests**, **BeautifulSoup**, and **pandas**.

## Prerequisites
Ensure you have Python installed (>=3.7). You will also need the following libraries:

```bash
pip install requests beautifulsoup4 pandas
```

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/book-scraper.git
   cd book-scraper
   ```
2. Run the script:
   ```bash
   python scraper.py
   ```
3. The extracted data will be saved in `books_data.csv`.

## Code Overview
The script performs the following:
1. Fetches the webpage `http://books.toscrape.com/`.
2. Parses the HTML content using **BeautifulSoup**.
3. Extracts book names, prices, and ratings.
4. Stores the data in a **pandas DataFrame**.
5. Saves the data into a CSV file.

## Example Output (books_data.csv)
```
Book Name,Price,Rating
"The Grand Design","£13.76","Three"
"The Catcher in the Rye","£39.49","Five"
...
```

## Contributing
Feel free to fork this repository and enhance the script with:
- **Pagination support** (scraping multiple pages)
- **Error handling** for robustness
- **Data visualization** for insights

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contact
For any issues or suggestions, reach out via GitHub Issues.

Ankit kumar

Email: your-ankitrajj1068@gmail.com

GitHub: ankit1068

