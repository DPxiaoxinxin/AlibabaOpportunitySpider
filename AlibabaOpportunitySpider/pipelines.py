# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
from datetime import date


class AlibabaopportunityspiderPipeline(object):
    def __init__(self):
        self.file_obj = open("alibaba-{date}.csv".format(date=date.today()), "w", encoding='utf_8_sig', newline="")
        self._fields = ["id", "name", "firstCategory", "secondCategory", "workLocation", "degree", "workExperience",
                        "departmentId", "departmentName", "gmtCreate", "gmtModified", "effectiveDate", "expired",
                        "isNew",
                        "isUrgent", "description", "requirement", "status", "href", "applyed", "code", "favorited",
                        "isOpen",
                        "recruitNumber", "uneffectualDate", "other"]
        self._dictwriter = csv.DictWriter(self.file_obj, fieldnames=self._fields)
        self._dictwriter.writerow({
            "id": "id",
            "name": "职位名称",
            "firstCategory": "第一职位类别",
            "secondCategory": "第二职位类别",
            "workLocation": "工作地点",
            "degree": "学历",
            "workExperience": "工作年限",
            "departmentId": "部门ID",
            "departmentName": "部门名",
            "gmtCreate": "发布时间",
            "gmtModified": "修改时间",
            "effectiveDate": "有效时间",
            "expired": "是否过期",
            "isNew": "是否最新",
            "isUrgent": "是否紧急",
            "description": "工作职责",
            "requirement": "工作要求",
            "status": "状态",
            "href": "详细链接",
            "other": "其它信息",
            "applyed": "applyed",
            "code": "code",
            "favorited": "是否收藏",
            "isOpen": "isOpen",
            "recruitNumber": "recruitNumber",
            "uneffectualDate": "uneffectualDate"
        })

    def process_item(self, item, spider):
        self._dictwriter.writerow(item._values)
        return item

    def close_spider(self, spider):
        self.file_obj.close()
