import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin


ROOT_URL = "https://books.toscrape.com/"
BASE_CATALOGUE_URL = "https://books.toscrape.com/catalogue/"
rows = []
page_num = 1

print("Starting scraper...")

while True:
    page_url = f"{BASE_CATALOGUE_URL}page-{page_num}.html"
    response = requests.get(page_url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    print(f"Scraping page {page_num}...")

    articles = soup.find_all("article", class_="product_pod")
    
    for tag in articles:
        relative_link = tag.find("h3").find("a")["href"]
        
        book_url = urljoin(page_url, relative_link)
        
        book_response = requests.get(book_url)
        book_soup = BeautifulSoup(book_response.text, "html.parser")
        
        main_content = book_soup.find("article", class_="product_page")
        
        data = {}

        data["Book name"] = main_content.find("h1").text.strip()

        rating_tag = main_content.find("p", class_="star-rating")
        if rating_tag:
            data["Star-rating"] = rating_tag["class"][1]

        desc_header = main_content.find("div", id="product_description")
        if desc_header:
            data["Product description"] = desc_header.find_next_sibling("p").text.strip()
        else:
            data["Product description"] = "No description available"

        table = main_content.find("table", class_="table-striped")
        if table:
            rows_table = table.find_all("tr")
            for row in rows_table:
                header = row.find("th").text.strip()
                value = row.find("td").text.strip()
                data[header] = value

        rows.append(data)

    page_num += 1

if rows:
    keys = [
        "Book name", "Star-rating", "Product description", 
        "UPC", "Product Type", "Price (excl. tax)", 
        "Price (incl. tax)", "Tax", "Availability", "Number of reviews"
    ]
    
    with open("book_pagination_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Success! Scraped {len(rows)} books into 'book_pagination_data.csv'.")
else:
    print("No data found.")
