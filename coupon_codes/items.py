# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CouponCodesItem(scrapy.Item):
    # define the fields for your item here like:
    course_name = scrapy.Field()
    course_publisher = scrapy.Field()
    course_price = scrapy.Field()
    course_language = scrapy.Field()
    course_description = scrapy.Field()
    course_coupon_code = scrapy.Field()
    pass
