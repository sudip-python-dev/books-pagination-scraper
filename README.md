# Books Pagination Scraper

This project is an advanced Python web scraping script that extracts detailed book information from multiple pages of the website:

https://books.toscrape.com

The script automatically navigates through all catalogue pages and collects structured data from individual book detail pages.

---

## Features

- Pagination scraping
- Multi-page data extraction
- Scrapes individual book detail pages
- Extracts structured product information
- Handles missing descriptions safely
- Saves all data into CSV format
- Uses urljoin for safe URL handling

---

## Data Extracted

This script extracts:

- Book Name
- Star Rating
- Product Description
- UPC
- Product Type
- Price (excl. tax)
- Price (incl. tax)
- Tax
- Availability
- Number of Reviews

---

## Tools Used

- Python
- Requests
- BeautifulSoup
- CSV Module
- urllib.parse (urljoin)

---

## Output

The script generates:

book_pagination_data.csv

This CSV file contains structured information about all books from the website.

---

## How to Run

Install required libraries:

pip install requests beautifulsoup4

Run the script:

python books_pagination_scraper.py

---

## Project Purpose

This project demonstrates advanced web scraping techniques including:

- Pagination scraping
- Nested page scraping
- Structured table data extraction

It was created as part of learning real-world data extraction workflows.
