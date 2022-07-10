# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CollectorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    videoID = scrapy.Field()
    videoTitle = scrapy.Field()
    videoLink = scrapy.Field()
    videoImage = scrapy.Field()
    videoStatus = scrapy.Field()
    videoViews = scrapy.Field()
    videoChannelName = scrapy.Field()
    videoUploadedTime = scrapy.Field()
