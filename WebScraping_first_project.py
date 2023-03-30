import requests
from bs4 import BeautifulSoup

# Steps to scrape the webpage using Beautiful Soup
# 1. use requests.get to get the response from the webpage
# 2. save the text as content
# 3. Use Beautiful Soup to download the html content using html.parser
# 4. Find the element of the webpage using the BeautifulSoup parser using find()
# 5. Save the data in the form of txt/csv using with open function.


# Scrape a Website - https://subslikescript.com/movie/Titanic-120338
# Lets use requests library to download the website html structure

response = requests.get("https://subslikescript.com/movie/Titanic-120338")
#print(response) # We see that the response is 200 which means it is a success
content = response.text # this is the page content
headers = response.headers # get the headers
#print(headers)

# Now we want to download the html structure of the page..
# For this we will use Beautiful Soup to scrap the website.
soup = BeautifulSoup(content, 'html.parser')
#print(soup.prettify()) # returns html content in a readable format

# Finding an element ~ (name of the element, type of parser)
box = soup.find('article', class_= "main-article")

# We will go inside the box to find the title - On the webpage we see that h1 is under
# the article. So now, we will use box to find the h1 tag and get the text from there
title = box.find("h1").get_text()
print(title)

# paragraph
upper = box.find("p", class_="plot").get_text(separator = " ", strip  =True)
print(upper)

# Similarly, we will go and extract the text from the webpage..the dialogues.
pg = box.find("div", class_= "full-script").get_text(separator = ' ', strip = True)
#print(pg)

# write the text in a txt file
with open(f'{title}.txt', "w") as file: # just write .csv instead of txt to get csv files
    file.write(pg)




