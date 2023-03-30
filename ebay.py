# Objective: Scrap ebay.com using the link below & generate the following info: ProductName, Price, Shipping_Cost
# Image URL, Number of Watchers & Product Condition(Brand New, Opened Box or Pre-Owned).

# Importing the Required Libraries
import requests # Sends requests...
from bs4 import BeautifulSoup # Used for scraping data out of HTML and XML files
import pandas as pd # Used to construct a DataFrame

# Requests module allows you to send HTTP requests using Python. 
# Defacto standard for making HTTP requests in Python

user_agent ={"User-Agent":"chrome"} 
link = "https://www.ebay.com/sch/i.html?_nkw=table"
page = requests.get(link,headers=user_agent)

root = "www.ebay.com"

# We will use Beautiful Soup to Generate the HTML Structure of the Page & is Saved in "soup" variable.
soup = BeautifulSoup(page.content, features="html.parser")

# Generating a Parent Structure from which the desired items will be scraped. 
products = soup.find_all("li", class_="s-item s-item__pl-on-bottom")

#Now, we will extract the following items:- ProductName, Price, Link, 
# Image URL, Number of Watchers & Product Condition(Brand New, Opened Box or Pre-Owned)

# Creating list where the data will be stored...
product_name = [] 
links = [] # website link
price = [] 
img_url =[] # Image Link
no_watchers =[]
prod_condition =[]
shipping_cost=[]

for prod in products:
    # Finding Product Name & saving it in var 'name'
    name = prod.find("div", class_="s-item__title").find("span").text.strip().replace(",", "")
    # Appending the Product Name in 'product_name' list.
    product_name.append(name)
    # Print the Product Names...
    print(f"Product Name:{name}\n")
    
    # Product Condition(Brand New, Opened Box or Pre-Owned)
    status = prod.find("div", class_="s-item__subtitle").find_next("span", class_="SECONDARY_INFO").text.strip()
    # Appending the Product Condition Status in the 'prod_condition' list
    prod_condition.append(status)
    # Print the Product Condition Status...
    print(f"Product_Condition:{status}\n")
    
    # Finding Price and saving it in var 'amt'
    amt = prod.find("span", class_="s-item__price").text.strip()
    # Appending it in the 'price' list
    price.append(amt)
    # Print the Price..
    print(f"Price:{amt}\n")
    
    # Finding No of Watchers and saving it in the var 'watchers'
    watchers = prod.find("span", class_="s-item__dynamic s-item__watchCountTotal")
    # Since watcher count is not available and hence saving it in watch_tags where it is NA
    watch_tags = (watchers.text.strip() if watchers else "Not Available")
    # Append the watch_tags in 'no_watchers' list
    no_watchers.append(watch_tags)
    # Print the Watch tags...
    print(f"Watcher Count: {watch_tags}\n")
    
    #Image Links
    img_src=prod.find("div", class_="s-item__image-wrapper image-treatment").find("img").get("src")
    # Append the Image Links in the 'image_url' list
    img_url.append(img_src)
    # Print the Image Source
    print(f"Image Source:{img_src}\n")
    
    # Generating Links and storing it in var 'links'
    link = prod.find("div", class_= "s-item__info clearfix").find("a").get("href")
    # Appending the Links in 'links' list.
    links.append(link)
    # Printing the Link
    print(f"Link:{link}\n")
    
    # Finding Shipping Cost & if the Shipping Cost is N.A., it will generate N/A
    shipping_tag = prod.find("span", class_="s-item__shipping s-item__logisticsCost")
    # saved the shipping cost in var 'tags'
    tags = (shipping_tag.text.strip() if shipping_tag else "N/A")
    # Appending it in the 'shipping_cost' list
    shipping_cost.append(tags)
    # Print the Shipping Cost...
    print(f"Shipping Cost:{tags}\n")
    print("-------------------------")
    

print(len(product_name))
print(len(price))
print(len(links))
print(len(img_url))
print(len(no_watchers))
print(len(prod_condition))
print(len(shipping_cost))

# Create a DataFrame and Generate the tsv file named 'tableList.tsv' as instructed
tableList = pd.DataFrame(product_name, columns=["Product_Name"])
tableList["Product_Condition"] = pd.Series(prod_condition)
tableList["Price"] = pd.Series(price)
tableList["No_Watchers"] = pd.Series(no_watchers)
tableList["Image_URL"] = pd.Series(img_url)
tableList["Webpage_Link"] = pd.Series(links)
tableList["Shipping_Cost"] = pd.Series(shipping_cost)

tableList.to_csv("tableList.tsv", index = False)