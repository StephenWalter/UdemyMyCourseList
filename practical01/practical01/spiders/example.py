
# Spider generated from the loocation /home/stephen/Dev/_Repos_/GitHub/UdemyMyCourseList/practical01 using the 
# scrapy genspider example example.com command and then  executed using scrapy crawl example
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
