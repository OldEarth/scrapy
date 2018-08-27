from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
import logging

from ..items import DoubanSpiderTop250Item

logging.basicConfig(level=logging.DEBUG)

class DoubanSpider(CrawlSpider):
    name = 'douban_many_movie_spider'

    download_delay = 1

    allowed_domains = ['movie.douban.com']

    start_urls = ['http://movie.douban.com/top250?start=0&filter=&type=']

    rules = [Rule(LinkExtractor(allow=(
        '(https://movie)\.(douban)\.(com)(/top250\?start=)\d+')),
        callback='parse_item', follow=True)]

    def parse_item(self, response):

        print('+' * 50)
        print response

        sel = Selector(response)
        item = DoubanSpiderTop250Item()

        movie_name = sel.xpath('//span[@class="title"][1]/text()').extract()
        star = sel.xpath('//span[@class="rating_num"]/text()').extract()
        quote = sel.xpath('//p[@class="quote"]/span[@class="inq"]/text('
                          ')').extract()

        item['movie_name'] = [n.encode('utf-8') for n in movie_name]
        item['star'] = [n.encode('utf-8') for n in star]
        item['quote'] = [n.encode('utf-8') for n in quote]

        yield item
