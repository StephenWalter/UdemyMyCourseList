import requests
from bs4 import BeautifulSoup

# r = requests.get('https://google.com')

# soup = BeautifulSoup(r.content, 'lxml')
# test bs is working
# print(soup.title)
# print(soup.find_all('a'))

# return webpage content nicely structured
# print(soup.prettify())

# using the http://quotes.toscrape.com/ website
r = requests.get('http://quotes.toscrape.com/')

soup = BeautifulSoup(r.content, 'lxml')
# select an element
print(soup.title.text)
# return quotes on page - this will return all structure (divs)
quotes = soup.find_all("div", class_="quote")
print(quotes)
# to get just the quotes
for e in quotes:
    print(e.find("span").text)

# return tags on page - this will return all structure (divs)
tags = soup.find_all("div", class_="tags")
print(tags)
# to get just the tags
for e in tags:
    print(e.text)


