# -*- coding: utf-8 -*-
import scrapy,uuid
from mySpider01.items import Myspider01Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    #allowed_domains = ['other.51cto.com']
    url = 'http://other.51cto.com/php/get_channel_recommend_art_list.php?callback=jsonp%s&page=%s&type_id=519&type=recommend&page_size=19'
    json_tag = 1499596309887
    offset = 2
    start_urls = [url%(str(json_tag),str(offset))]


    def parse(self, response):
        item = Myspider01Item()
        item["content"]=response.text
        print  response.text
        yield item

        self.offset += 1
        self.json_tag+=1
        ye_url= self.url % (str(self.json_tag),str(self.offset))
        yield scrapy.Request(ye_url, callback = self.parse)

