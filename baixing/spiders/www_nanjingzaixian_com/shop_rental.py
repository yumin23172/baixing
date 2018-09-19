# -*- coding: utf-8 -*-
import re

import scrapy


class NanjingzaixianSpider(scrapy.Spider):
    name = 'shops_rental'
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
                item["url"] = "" + item["url"]
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
        item["address"] = response.xpath("").extract_first()
        item["type"] = 4
        item["bd_type"] = 4
        item["width"] = float(0)
        item["length"] = float(0)
        item["high"] = float(0)
        item["manage_status"] = ""
        price = response.xpath("").extract_first()
        if price:
            p = response.xpath("//div[@class='neirong']/dl[1]//b/text()").extract_first()
            item["price"] = float(p)
        else:
            item["price"] = float(0)
        size = response.xpath("").extract_first()
        if size:
            s = response.xpath("").extract_first()
            item["size"] = float(s)
        pay_method = response.xpath("").extract_first()
        if pay_method:
            item["pay_method"] = response.xpath("").extract_first()
        else:
            item["pay_method"] = ""
        item["phone"] = response.xpath("").extract_first()
        item["contact_url"] = ""
        item["manage_industry"] = ""
        floor = response.xpath("").extract_first()
        if floor:
            item["floor"] = response.xpath("").extract_first()
        else:
            item["floor"] = ""
        category= response.xpath("").extract_first()
        if category:
            item["category"] = response.xpath("").extract_first()
        else:
            item["category"] = ""
        description = response.xpath("").extract_first()
        if description:
            item["description"] = response.xpath("").extract_first()
        else:
            item["description"] = ""
        img_ur = response.xpath("").extract_first()
        if img_ur:
            item["img_ur"] = response.xpath("").extract_first()
        else:
            item["img_ur"] = ""
        item["time"] = response.xpath("").extract_first()
        item["house_allocation"] = response.xpath("").extract_first()
        name = response.xpath("").extract_first()
        if name:
            item["name"] = response.xpath("").extract_first()
        else:
            item["name"] = ""
        item["from"] = response.xpath("").extract_first()
