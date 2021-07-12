
### Scrapy Items and Pipelines ###

#section 01
import scrapy
from practical01.items import Practical01Item


#section 02
class MySpider02(scrapy.Spider):
    name = "Books02"
    start_urls = [
        "http://books.toscrape.com/catalogue/tipping-point-for-planet-earth-how-close-are-we-to-the-edge_643/index.html"
    ]

    #section 03
    def parse(self, response):
        item = Practical01Item()
        # code for Scrapy Items and Pipelines => outputBooks02.csv
        #item['title'] = response.xpath('/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1').extract()
        #item['price'] = response.xpath('/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/p[1]').extract()
        # code for Traversing Options => outputBooks02a.csv 
        item['title'] = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        return item

