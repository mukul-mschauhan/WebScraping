# In this project, we will scrap machine learning jobs using https://www.timesjobs.com/

# import the required libraries
import requests
from bs4 import BeautifulSoup

# requests the information from the webpage
root = "https://www.timesjobs.com/"
page = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=machine+learning&txtLocation=India")

# Use bs4 to get access to html content
soup = BeautifulSoup(page.content, "html.parser")

# Lets start scraping the content now
# Here we would start by scraping the company Name, Job Title & Key Skills
# Note: The jobs are available under the list (ul) tag followed by class tag - clearfix job-bx wht-shd-bx

# using "find_all" to find the li (list) components in HTML Tree. This is where the job resides...
jobs = soup.find_all("li", {"class":"clearfix job-bx wht-shd-bx"})

# Now we will extract the company Name
for job in jobs:    
    published = job.find("span", class_ = "sim-posted").text.strip().replace(" ", "")
    # Now we will apply a condition to filter only the recent jobs having status - "Posted few days ago"
    if 'few' in published:    
        company = job.find("h3", {"class":"joblist-comp-name"}).text.strip().replace(" ", "")
        joblink = job.find("h2").a["href"].strip()
        title = job.find("span", class_="srp-skills").text.strip().replace(" ", "")
        print(f"Company Name: {company.strip()}")
        print(f"Required Skills: {title.strip()}")
        print(f"Job Link: {joblink.strip()}")
        print(f"Published Date: {published.strip()}")
        print("") # separator
    
