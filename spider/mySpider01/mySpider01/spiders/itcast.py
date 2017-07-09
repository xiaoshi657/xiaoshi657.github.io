# -*- coding: utf-8 -*-
import scrapy,uuid
from mySpider01.items import Myspider01Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['www.cnblogs.com']
    url = 'https://www.cnblogs.com/sitehome/p/'
    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 取出每个页面里帖子链接列表
        links = response.xpath("//*[@id='post_list']/div/div[2]/h3/a/@href").extract()
        # f=open(str(uuid.uuid1())+".html","a+")
        # f.write(response.text.encode("utf-8"))
        # f.close()

        # 迭代发送每个帖子的请求，调用parse_item方法处理
        for link in links:
            print link
            yield scrapy.Request(link, callback = self.parse_item)
        # 设置页码终止条件，并且每次发送新的页面请求调用parse方法处理
        #if self.offset <= 200:
        self.offset += 1
        ye_url=self.url+str( self.offset)+"?uuid="+str(uuid.uuid1())
        #加参数dont_filter = True 关闭去从，否着#传参，默认是一个网址
        yield scrapy.Request(ye_url, callback = self.parse,dont_filter = True)

    # 处理每个帖子里
    def parse_item(self, response):
        item = Myspider01Item()
        item['title'] = response.xpath('//*[@id="cb_post_title_url"]/text()').extract()
        item["content"] = response.xpath('//*[@id="cnblogs_post_body"]').extract()
        item["salary"]=response.xpath('//*[@id="author_profile_detail"]/a[1]/text()').extract()
        yield item