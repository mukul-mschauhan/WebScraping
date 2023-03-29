# In this project, We will scrap books from https://books.toscrape.com/ using BeautifulSoup Library

# importing the required libraries
# Requests module allows you to send HTTP requests using Python. 
# Defacto standard for making HTTP requests in Python
import requests 

# Beautiful Soup is a Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup

# Step 1: use requests to pull the text content of the website
webpage = "https://books.toscrape.com/"
response = requests.get(webpage)

# Step 2: Use Beautiful Soup to download the HTML content structure
soup = BeautifulSoup(response.content, "html.parser")
#print(soup.prettify())

# Step 3" Lets find the Book Names, Price and Instock or Not.
books = soup.find_all("li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")

# We will use csv library to export the data in the form of csv file
import csv

# Create the Dataset with the Feature Names as - Name, Price, In Stock and Link
with open("books.csv", "w", newline = "") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Price", "In Stock", "Link"])

# We will then append in the data into the books.csv created above.
with open("books.csv", "a") as csv_file:
    writer = csv.writer(csv_file)
    
    # We will now run the loop to extract the data for all pages.
    for book in books:
        title = book.find("h3").a["title"].strip()

        # Extracting Price of a Book:
        # Simple Approach::div>>product_price>>p>>price_color>>price
        #price_html_tag = book.find("div", class_="product_price")
        #print(price_html_tag.find("p", class_="price_color").text)

        # Direct Approach - Extracting Price of a Book
        price = book.select_one("div.product_price>p.price_color").text.strip()

        # Extracting In Stock or Not
        #print(price_html_tag.select_one("p.instock.availability").text.strip())
        in_stock = book.select_one("div.product_price>p.instock.availability").text.strip()

        # Link of the Book
        link = book.find("h3").a["href"].strip()
        
        # Writing the data into csv file.
        writer.writerow([title, price, in_stock, link])
