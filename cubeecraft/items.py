# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CubeecraftItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field()