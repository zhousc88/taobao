#author:zhousc
import json,pymongo
class StoreData(object):
    def __init__(self):
        self.client=pymongo.MongoClient("localhost",27017)
        self.db=self.client.TB
    def store_goods(self,items):
        for item in items:
            self.db.goods.insert(item['goods'])
            self.db.shops.inser(item['shops'])
    def store_category(self,items):
        #类别信息存储
        for item in items:
            self.db.category.insert(item)

    def store_related(self,items):
        # 相似信息存贮
        for item in items:
                self.db.related.insert(item)

    def store_goods(self,items):
        #商品信息存储
       for item in items:
            self.db.goods.insert(item['goods'])
            self.db.shop.insert(item['shops'])

    def store_tags(self,items):
        for item in items:
            self.db.tags.insert(item)

    def store_rate(self,items):
        for item in items:
            self.db.rate.insert(item)