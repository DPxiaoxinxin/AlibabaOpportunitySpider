# -*- coding: utf-8 -*-
import json
import urllib

import scrapy
from scrapy.spiders import CrawlSpider, Rule

from AlibabaOpportunitySpider.items import AlibabaItem


class AlibabaSpider(CrawlSpider):
    name = 'alibaba'
    allowed_domains = ['job.alibaba.com']
    start_urls = ['https://job.alibaba.com/zhaopin/socialPositionList/doList.json?pageSize=1000&t=0.7105616242301789&pageIndex=0']
    pages = 0


    def parse(self, response):
        data = json.loads(response.text)
        if data["isSuccess"]:
            self.pages = int(data["returnValue"]["totalPage"])
            for page in range(self.pages):
            # for page in range(2):
                yield scrapy.Request(self.start_urls[0].replace("pageIndex=0", "pageIndex={page}".format(page=page)), callback=self.parse_item)

    def parse_item(self, response):
        datas = json.loads(response.text)["returnValue"]["datas"]
        for data in datas:
            item = AlibabaItem()
            for key, value in data.items():
                item[key] = value
            yield item


