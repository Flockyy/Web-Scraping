# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import TakeFirst, MapCompose, Join

class ThomannItem(scrapy.Item):
    name = scrapy.Field()
    make = scrapy.Field()
    observer = scrapy.Field()
    sell_rank = scrapy.Field()
    price = scrapy.Field()
    features = scrapy.Field()
    rating = scrapy.Field()
    nb_evaluation = scrapy.Field()
    
