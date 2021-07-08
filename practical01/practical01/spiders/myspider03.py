
### Scrapy Items and Pipelines ###

#section 01
import scrapy
from practical01.items import Practical01Item


#section 02
class MySpider02(scrapy.Spider):
    name = "Books03"
    start_urls = [
        "http://books.toscrape.com/catalogue/tipping-point-for-planet-earth-how-close-are-we-to-the-edge_643/index.html",
        "http://books.toscrape.com/catalogue/the-most-perfect-thing-inside-and-outside-a-birds-egg_938/index.html",
        "http://books.toscrape.com/catalogue/immunity-how-elie-metchnikoff-changed-the-course-of-modern-medicine_900/index.html",
        "http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html"
    ]

    #section 03
    def parse(self, response):
        item = Practical01Item()
        # code for Scrapy Challenge => outputBooks03.csv
        # My first attempt
        #item['title'] = response.xpath('/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1/text()').extract()
        #item['price'] = response.xpath('/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/p[1]/text()').extract()
        #item['category'] = response.xpath('/html/body/div/div/ul/li[3]/a/text()').extract()
        #item['availability'] = response.xpath('/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/p[2]/text()').extract()
        # solution...
        item['title'] = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        item['category'] = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()
        item['availability'] = response.xpath("normalize-space(//p[@class='instock availability']/i/following::node()[1])").get()

        return item

