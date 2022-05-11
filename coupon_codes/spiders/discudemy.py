from coupon_codes.items import CouponCodesItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DiscudemySpider(CrawlSpider):
    name = 'discudemy'
    allowed_domains = ['www.discudemy.com']
    start_urls = ['https://www.discudemy.com/all']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='card-header']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//ul[contains(@class, 'pagination3')]/li[last()]/a"), follow=True),

    )

    def parse_item(self, response):
        item = CouponCodesItem()
        item['course_name'] = response.xpath("//h1[contains(@class, 'header')]/text()").get()
        item['course_publisher'] = response.xpath("//span[@class='publisher']/text()").get()
        item['course_price'] = response.xpath("//span[@class='price']/text()").get()
        item['course_language'] = response.xpath("//span[@class='languages']/text()").get()
        url = response.xpath("//a[contains(@class, 'ui big inverted green button discBtn')]/@href").get()
        return response.follow(url, self.parse_code, cb_kwargs=dict(item=item))
        

    def parse_code(self, response, item):
        item['course_coupon_code'] = response.xpath("//a[@id='couponLink']/text()").get()

        return item
        

