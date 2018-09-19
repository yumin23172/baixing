# -*- coding: utf-8 -*-
#南京在线网
#住宅出租
import re

import scrapy


class NanjingzaixianSpider(scrapy.Spider):
    name = 'house_rental'
    # allowed_domains = ['']
    start_urls = ['']

    # 房屋列表页信息
    def parse(self, response):
        item = {}
        li_list = response.xpath("")
        for li in li_list:
            item["title"] = li.xpath(".").extract_first()
            url = li.xpath(".").extract_first()
            if url:
                item["url"]=""+item["url"]
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
        item['city'] = response.xpath("").extract_first()
        item["area"] = response.xpath("").extract_first()
        item["street"] = response.xpath("").extract_first()
        item["community"] = response.xpath("").extract_first()
        address = response.xpath("").extract_first()
        if address:
            item["address"] = response.xpath("").extract_first()
        else:
            item["address"] = ""
        item["type"] = 4
        item["bd_type"] = 1
        price = response.xpath("").extract_first()
        if price:
            p = response.xpath("//div[@class='neirong']/dl[1]//b/text()").extract_first()
            item["price"]=float(p)
        else:
            item["price"] =float(0)
        size = response.xpath("").extract_first()
        if size:
            s =response.xpath("").extract_first()
            item["size"] = float(s)
        item["phone"] = response.xpath("").extract_first()
        item["contact_url"] = ""
        y = response.xpath("").extract_first()
        if y:
            if "室" in y:
                shi = response.xpath("").extract_first()
                item["shi"] = int(shi)
            else:
                item["shi"] = 0
            if "厅" in y:
                ting = response.xpath("").extract_first()
                item["ting"] = int(ting)
            else:
                item["ting"] = 0
            if "卫" in y:
                wei = response.xpath("").extract_first()
                item["wei"] = int(wei)
            else:
                item["wei"] = 0
        orientation = response.xpath("").extract_first()
        if orientation:
            item["orientation"] = response.xpath("").extract_first()
        else:
            item["orientation"] = ""
        item["subway"] = response.xpath("").extract_first()
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
            item["description"] = ""
        img_url = response.xpath("").extract_first()
        if img_url:
            item["img_url"] = response.xpath("").extract_first()
        else:
            item["img_url"] = ""
        item["time"] = response.xpath("").extract_first()
        name = response.xpath("").extract_first()
        if name:
            item["name"] = response.xpath("").extract_first()
        else:
            item["name"] = ""
        item["from"] = response.xpath("").extract_first()

        rent_type = response.xpath("").extract_first()
        if rent_type:
            item["rent_type"] = response.xpath("").extract_first()
        else:
            item["rent_type"] = ""
        pay_method = response.xpath("").extract_first()
        if pay_method:
            item["pay_method"] = response.xpath("").extract_first()
        else:
            item["pay_method"] = ""
        house_allocation = response.xpath("").extract_first()
        if house_allocation:
            item["house_allocation"] = response.xpath("").extract_first()
        else:
            item["house_allocation"] = ""
