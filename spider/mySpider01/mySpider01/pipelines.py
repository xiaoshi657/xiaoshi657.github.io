# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis,json,uuid,re

class Myspider01Pipeline(object):
    # __init__方法是可选的，做为类的初始化方法
   # def __init__(self):
        # 创建了一个文件
        #self.filename = open("teacher.json", "w")

    # process_item方法是必须写的，用来处理item数据
    def process_item(self, item, spider):
        jsontext = dict(item)["content"]
        # re1=re.compile()
        # m =re1.match(jsontext)

        ret = re.match("jsonp\d+\(\[(.*)\,1\]\)$", jsontext)
        # ret.group()

        r_text= ret.group(1)
        print r_text
        try:
            r = redis.StrictRedis(host='192.168.0.109', port=6379)
        except Exception, e:
            print e.message
        r.set("test2_jsonp_51cto_"+str(uuid.uuid1()),r_text)
        #self.filename.write(jsontext.encode("utf-8"))
        return item

    # close_spider方法是可选的，结束时调用这个方法
   # def close_spider(self, spider):
     #   self.filename.close()





