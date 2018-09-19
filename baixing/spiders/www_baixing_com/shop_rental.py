# -*- coding: utf-8 -*-
import re

import scrapy


class BaixingfSpider(scrapy.Spider):
    name = 'shops_rental'
    allowed_domains = ['shanghai.baixing.com']
    start_urls = ['http://shanghai.baixing.com/jingyingzhuanrang/?afo=kTE']

    def parse(self, response):
        #城市
        item={}
        item['city']=response.xpath("//div[@class='toolbar-link']/a[1]/text()").extract_first()
        #商铺列表页信息
        li_list = response.xpath("//div[@class='main']//li")
        for li in li_list:
            item["area"] = li.xpath(".//div/div[3]").extract_first().split('[')[-1].split(']')[0].split('-')[0]
            item["street"] = li.xpath(".//div/div[3]").extract_first().split('[')[-1].split(']')[0].split('-')[1]
            item["address"] = li.xpath(".//div/div[3]").extract_first().split('[')[-1].split(']')[0].split('-')[2]
            if item["address"] is not None:
                item["address"] = li.xpath(".//div/div[3]").extract_first().split('[')[-1].split(']')[0].split('-')[2]
            item["type"] = 3
            item["bd_type"] = 4
            item["width"] = ""
            item["length"] = ""
            item["high"] = ""
            item["manage_status"] = ""
            item["title"] = li.xpath("./div/div[1]/a[1]/text()").extract_first()
            item["price"] = li.xpath("./div/div[1]/span/text()").extract_first()

            item["size"] = li.xpath("./div/div[2]").extract_first()
            item["contact_url"] = ""
            item["manage_industry"] =""
            item["house_allocation"] =""
            item["floor"] =""
            item["name"] = ""
            item["category"] =""
            item["form"] = ""
            item["url"] = li.xpath("./div/div[1]/a[1]/@href").extract_first()
            if item["url"] is not None:
                yield scrapy.Request(
                    item["url"],
                    callback=self.parse_zhufang_list,
                    meta={"item": item}
                )
        # 翻页
        next_url = response.xpath("//div[@class='main']//section[2]/ul//li[13]/a/@href").extract_first()
        if next_url is not None:
            next_url = "http://shanghai.baixing.com" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                meta={"item": item}

            )

    # 商铺详情页信息
    def parse_zhufang_list(self, response):
        item = response.meta["item"]
        item["phone"] = response.xpath("//li[@class='contact-btn-box']//strong").extract_first()
        item["description"] = response.xpath("//div[@class='viewad-text']").extract()
        item["img_url"] = response.xpath("//div[@class='featured-height']/div/a/@style").extract_first().split('(')[-1].split(')')[0]
        item["time"] = response.xpath("//div[@class='viewad-actions']/span[2]").extract_first()
        item["pay_method"] = ""