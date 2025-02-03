import requests
from bs4 import BeautifulSoup
#URL of a news website (Example:BBC News)
url = "https://www.bbc.com/news"
#Send GET request to the URL
response = requests.get(url)
#Print (response.text)
#Check if the request was successful
if response.status_code == 200:
    print("Page fetched successfully!\n")
    #parse the HTML content of the page using beautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    #Find headlines (example: Find all <h3> tags with class 'gs-c-promo-heading_tittle')
    headlines = soup.find_all ('h2', class_='sc-8ea7699c-3')
    #print(headlines)
    #Display the first 5 headlines
    print("Top 5 Headlines:")
    for i, headline in enumerate(headlines[:5]):
        print(f"{i+1}. {headline.get_text()}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

#https://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
#URL of a news website 
url = "https://quotes.toscrape.com/"
#Send GET request to the URL
response = requests.get(url)
#print (type(response.content))
soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup)
    #Extract quotes, authors, and tags
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_ = 'author')
tags = soup.find_all('div', class_='tags')
#print the extracted information
for quote, author, tag in zip(quotes, authors, tags):
    print(f'Quote: {quote.text}')
    print(f'Author: {author.text}')
    print('tags:')
    for t in tag.find_all('a',class_='tag'):
          print(f'-{t.text}')
          print()
#Task 1
import requests
from bs4 import BeautifulSoup
url = "https://www.w3schools.com/python/"
response  = requests.get(url)
if response.status_code == 200:
    print("Page fetched successfully!\n")
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    print("Extracted Links:")
    for link in links:
        print(link)
else:
    print(f"Failed to fetch page, status code: {response.status_code}")

#Scrape Article Titles from a News Website
import requests
from bs4 import BeautifulSoup
# URL of the news website (Example: BBC)
url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("h3") 
for idx, title in enumerate(titles, 1):
    print(f"{idx}. {title.get_text(strip=True)}")
