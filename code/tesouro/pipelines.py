# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests, json, logging

class TesouroPipeline(object):


	def open_spider(self, spider):
		self.lines = []
		logging.log(logging.WARNING, "OPEN SET")

	def close_spider(self, spider):
		logging.log(logging.WARNING, "CLOSE SET {}".format(len(self.lines)))

	def process_item(self, item, spider):
		self.lines.append(item)
		return item