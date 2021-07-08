
### This didn't work as you have to initialise scrapy project e.g. "scrapy startproject scrapy02"


#section 01
import scrapy


#section 02
class FirstSpider(scrapy.Spider):
    name = "Books"
    start_urls = [
        "http://books.toscrape.com/",
        "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
    ]

    #section 03
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'books-%s.html' % page
        with open(filename, "wb") as f:
            f.write(response.body)




