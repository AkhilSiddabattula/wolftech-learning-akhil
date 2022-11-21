# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComprassaltaItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    entityIdAtSource = scrapy.Field()
    shortDescription = scrapy.Field()
    supplierName = scrapy.Field()
    openDate = scrapy.Field()
    originalUrl = scrapy.Field()
    documentLinks = scrapy.Field()
    detail = scrapy.Field()
    lotTitle = scrapy.Field()
    documentLinks = scrapy.Field()

