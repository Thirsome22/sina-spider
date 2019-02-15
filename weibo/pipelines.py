# -*- coding: utf-8 -*-
import pymongo
from scrapy.exceptions import DropItem
from openpyxl import Workbook

from weibo.items import *

class WeiboPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost',27017)
        print('连接成功')
        db = client['weibo']
        self.Information = db["Information"]
        self.Tweets = db["Tweets"]
        self.Follows = db["Follows"]
        self.Fans = db["Fans"]
        self.KeyTweets = db["KeyTweets"]
    def process_item(self, item, spider):
        if isinstance(item,InformationItem):
            for data in item:
                if not data:
                    raise DropItem("Missing data!")
                self.Information.update({'_id':item['_id']},dict(item),upsert=True)
        elif isinstance(item,TweetsItem):
            for data in item:
                if not data:
                    raise DropItem("Missing data!")
                self.Tweets.update({'_id':item['_id']},dict(item),upsert=True)
        elif isinstance(item,FansItem):
            for data in item:
                if not data:
                    raise DropItem("Missing data!")
                self.Fans.update({'_id':item['_id']},dict(item),upsert=True)
        elif isinstance(item,FollowsItem):
            for data in item:
                if not data:
                    raise DropItem("Missing data!")
                self.Follows.update({'_id':item['_id']},dict(item),upsert=True)
        elif isinstance(item,KeyTweetsItem):
            for data in item:
                if not data:
                    raise DropItem("Missing data!")
                self.KeyTweets.update({'_id':item['_id']},dict(item),upsert=True)
        return item


# 存储在表格中    设置工序一
class WeiboBiaogePipeline(object):
    def __init__(self):
        self.wb = Workbook() # class实例化
        self.ws = self.wb.active # 激活工作表
        self.ws.append(['唯一标识符', 'ID号', '关键词', '微博内容', '发布时间', '爬取时间'])

    def process_item(self, item, spider): # 工序具体内容
        line = [item['_id'], item['ID'], item['keyword'], item['text'], item['PubTime'], item['createtime']]
        self.ws.append(line) # 将数据以行的形式添加到xlsx中
        self.wb.save('G:\data.xlsx') # 保存xlsx文件
        return item
