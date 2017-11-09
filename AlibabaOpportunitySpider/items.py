# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime


class AlibabaItem(scrapy.Item):
    applyed = scrapy.Field()
    code = scrapy.Field()
    degree = scrapy.Field()
    departmentId = scrapy.Field()
    departmentName = scrapy.Field()
    description = scrapy.Field()
    effectiveDate = scrapy.Field()
    expired = scrapy.Field()
    favorited = scrapy.Field()
    firstCategory = scrapy.Field()
    gmtCreate = scrapy.Field()
    gmtModified = scrapy.Field()
    id = scrapy.Field()
    isNew = scrapy.Field()
    isOpen = scrapy.Field()
    isUrgent = scrapy.Field()
    name = scrapy.Field()
    recruitNumber = scrapy.Field()
    requirement = scrapy.Field()
    secondCategory = scrapy.Field()
    status = scrapy.Field()
    uneffectualDate = scrapy.Field()
    workExperience = scrapy.Field()
    workLocation = scrapy.Field()
    href = scrapy.Field()
    other = scrapy.Field()

    def __setitem__(self, key, value):
        if key in self.fields:
            if key in ("uneffectualDate", "gmtModified", "gmtCreate", "effectiveDate"):
                self._values[key] = datetime.datetime.fromtimestamp(float(value) / 1000)
            else:
                if key in ("description", "requirement"):
                    value = value.replace("<br/>", "\n")
                self._values[key] = value
                if key == "id":
                    self._values["href"] = "https://job.alibaba.com/zhaopin/position_detail.htm?positionId=" + str(value)
        else:
            if "other" not in self._values:
                self._values["other"] = dict()
            self._values["other"].update({key: value})

            # raise KeyError("%s does not support field: %s" %
            #     (self.__class__.__name__, key))
