# We will scrap the information related to Protein Powder for Weight Loss in Women on Amazon.in
# The following information will be scraped from the webpage - Product Name, Flavour, Price & Rating

import requests
from bs4 import BeautifulSoup
import csv

user_agent = {"User-Agent":"sunny_leone"}
page = requests.get("https://www.amazon.in/s?k=protein+powder+for+women+weight+loss&crid=3R3F3MPN0FMUA&sprefix=protein+powder+for+women%2Caps%2C209&ref=nb_sb_ss_ts-doa-p_3_24",
                    headers=user_agent)

# Use Beautifulsoup to download the html structure of the Amazon Page
soup = BeautifulSoup(page.content, features="html.parser") # we need a parser to parse the content

# searching the Parent tag...
products =  soup.find_all("div", class_="sg-col-inner")

# Finding the Product Name
product_name = []
for p in products:
    if(p.find("span", class_="a-size-base-plus a-color-base a-text-normal")):
        product_name.append(p.find("span", class_="a-size-base-plus a-color-base a-text-normal").text.strip().split(",")[0])

# Finding the Flavour
flavour =[]
for p in products:
    if p.find("span", class_="a-color-information a-text-bold"):
        flavour.append(p.find("span", class_="a-color-information a-text-bold").text.strip().split(",")[0])

# Finding the Price
price =[]
for p in products:
    if p.find("span", class_="a-offscreen"):
        price.append(p.find("span", class_="a-offscreen").text)
        
# Finding the Ratings
ratings =[]
for p in products:
    if p.find("div", class_="a-row a-size-small"):
        ratings.append(p.find("div", class_="a-row a-size-small").text)
        
# Store the Following Information in a DataFrame
import pandas as pd
prod_info = pd.DataFrame(product_name, columns = ["Product_Name"])
prod_info["Flavours"] = pd.Series(flavour)
prod_info["Price"] = pd.Series(price)
prod_info["Ratings"] = pd.Series(ratings)

# Generating a csv file.
prod_info.to_csv("Prod_Info.csv", index = False)