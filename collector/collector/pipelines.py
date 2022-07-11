# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from collector.settings import MONGODBCONNECTIONSTRING


class CollectorPipeline:

    def open_spider(self, spider):
        self.connect = MongoClient(MONGODBCONNECTIONSTRING, connect=False)

    def process_item(self, item, spider):
        db = self.connect["ytChannel"]
        collection = db["videos"]

        newData = {
            "videoID": item["videoID"],
            "videoTitle": item["videoTitle"],
            "videoLink": item["videoLink"],
            "videoImage": item["videoImage"],
            "videoStatus": item["videoStatus"],
            "videoViews": item["videoViews"],
            "videoChannelName": item["videoChannelName"],
            "videoUploadedTime": item["videoUploadedTime"]
        }
        if collection.find_one({"videoChannelName": item["videoChannelName"]}) == None:
            if collection.find_one({"videoID": item["videoID"]}):
                print("Duplicate video")
                return
            print("Insert NewData")
            collection.insert_one(newData)
        elif collection.find_one({"$and": [{"videoChannelName": item["videoChannelName"]}, {"videoID": {"$ne": item["videoID"]}}]}):
            print("Update Data")
            collection.update_one(
                {"videoChannelName": item["videoChannelName"]}, {"$set": newData})

    def close_spider(self, spider):
        self.connect.close()
