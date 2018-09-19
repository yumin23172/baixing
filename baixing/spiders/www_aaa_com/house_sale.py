# -*- coding: utf-8 -*-

#住宅出售
import re

import scrapy


class NanjingzaixianSpider(scrapy.Spider):
    name = 'house_sale'
    # allowed_domains = ['']
    start_urls = ['']

    # 房屋列表页区域划分
    def parse(self, response):
        item = {}
        li_list = response.xpath("")
        for li in li_list:
            item["area"] = li.xpath(".").extract_first()
            area_url = li.xpath(".").extract_first()
            if area_url:
                a_url = "" + area_url
                yield scrapy.Request(
                    url=a_url,
                    callback=self.parse_list,
                    meta={"item": item}
                )
    # 房屋列表页信息
    def parse_list(self, response):
        item = {}
        li_list = response.xpath("")
        for li in li_list:
            item["title"] = li.xpath(".").extract_first()
            url = li.xpath(".").extract_first()
            if url:
                item["url"] = "" + url
                yield scrapy.Request(
                    item["url"],
                    callback=self.parse_detail,
                    meta={"item": item}
                )
        # 翻页
        # next_url = response.xpath("//div[@class='pager']/a[11]/@href").extract_first()
        # if next_url is not None:
        #     next_url = "http://sh.bqqm.com" + item["url"]
        # yield scrapy.Request(
        #     next_url,
        #     callback=self.parse,
        #     meta={"item": item}
        #
        # )

    # 房屋详情页信息
    def parse_detail(self, response):
        item = response.meta["item"]
        item['city'] = ""
        item["street"] = ""
        item["community"] = ""
        address= response.xpath("").extract_first()
        if address:
            item["address"] = response.xpath("").extract_first()
        else:
            item["address"] =""
        item["type"] = 3
        item["bd_type"] = 1
        price = response.xpath("").extract_first()
        if price:
            p = response.xpath("").extract_first()
            item["price"]=float(p)
        else:
            item["price"] =float(0)
        size=response.xpath("").extract_first()
        if size:
            size = response.xpath("").extract_first()
            item["size"] = float(size)
        y=response.xpath("").extract_first()
        if y:
            if "室" in y:
                shi = response.xpath("").extract_first()
                item["shi"]=int(shi)
            else:
                item["shi"] =0
            if "厅" in y:
                ting = response.xpath("").extract_first()
                item["ting"] = int(ting)
            else:
                item["ting"] =0
            if "卫" in y:
                wei = response.xpath("").extract_first()
                item["wei"] = int(wei)
            else:
                item["wei"] = 0
        item["phone"] = response.xpath("").extract_first()
        item["contact_url"] = ""
        orientation = response.xpath("").extract_first()
        if orientation:
            item["orientation"] = response.xpath("").extract_first()
        else:
            item["orientation"] =""
        subway = response.xpath("").extract_first()
        if subway :
            item["subway"] = response.xpath("").extract_first()
        else:
            item["subway"] =""
        floor = response.xpath("").extract_first()
        if floor:
            item["floor"] = response.xpath("").extract_first()
        else:
            item["floor"] = ""
        decoration = response.xpath("").extract_first()
        if decoration:
            item["decoration"] = response.xpath("").extract_first()
        else:
            item["decoration"] = ""
        house_types = response.xpath("").extract_first()
        if house_types:
            item["house_types"] = response.xpath("").extract_first()
        else:
            item["house_types"] = ""
        description = response.xpath("").extract_first()
        if description:
            item["description"] = response.xpath("").extract_first()
        else:
            item["description"] = "暂无描述"
        img_url = response.xpath("").extract_first()
        if img_url:
            item["img_url"] = response.xpath("").extract_first()
        else:
            item["img_url"] = ""
        item["time"] = response.xpath("").extract_first()

        property_type = response.xpath("").extract_first()
        if property_type:
            item["property_type"] = response.xpath("").extract_first()
        else:
            item["property_type"] = ""
        name = response.xpath("").extract_first()
        if name:
            item["name"] = response.xpath("").extract_first()
        else:
            item["name"] = ""
        item["from"] = response.xpath("").extract_first()
        yield item
