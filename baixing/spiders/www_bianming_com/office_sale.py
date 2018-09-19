# -*- coding: utf-8 -*-
#便民网
#写字楼出售
import re

import scrapy


class BianmingSpider(scrapy.Spider):
    name = 'office_sale'
    allowed_domains = ['sh.bqqm.com']
    start_urls = ['http://sh.bqqm.com/xiezilou/s5218s0s0/']

    def parse(self, response):
        item = {}
        item['city'] = response.xpath("//div[@class='bar_left']/b/text()").extract_first()
        # 房屋列表页信息
        li_list = response.xpath("//div[@id='main']//tr")
        for li in li_list:
            item["type"] = 3
            item["bd_type"] = 4
            item["title"] = li.xpath("./td[2]/a/text()").extract_first()
            item["price"] = li.xpath("./td[3]/b/text()").extract_first()
            item["size"] = li.xpath("./td[4]").extract_first()
            item["contact_url"] = ""
            item["form"] = ""
            item["url"] = li.xpath("./td[2]/a/@href").extract_first()
            if item["url"] is not None:
                item["url"]="http://sh.bqqm.com"+item["url"]
                yield scrapy.Request(
                    item["url"],
                    callback=self.parse_zhufang_list,
                    meta={"item": item}
                )
        # 翻页
        next_url = response.xpath("//div[@class='pager']/a[11]/@href").extract_first()
        if next_url is not None:
            next_url = "http://sh.bqqm.com" + item["url"]
        yield scrapy.Request(
            next_url,
            callback=self.parse,
            meta={"item": item}

        )
    # 房屋详情页信息
    def parse_zhufang_list(self, response):
        item = response.meta["item"]
        item["area"] = ""
        item["street"] = ""
        item["address"] = response.xpath("//div[@id='thress']/ul/li[5]/text()").extract_first()
        item["phone"] = response.xpath("//div[@class='telbox']/span[2]/text()").extract_first()
        item["floor"] = ""
        item["house_allocation"] = ""
        item["description"] = response.xpath("//div[@class='content']/span/text()").extract()
        item["img_url"] = response.xpath("//div[@class='descriptionImg']/img/@src").extract_first()
        item["time"] = response.xpath("//div[@class='top']/span//text()").extract_first().split('：')[-1]
        item["name"] = response.xpath("//div[@id='thress']/ul/li[6]/text()").extract_first()
        item["registered_company"] = response.xpath("//div[@id='thress']/ul/li[2]/text()").extract_first().split('(')[-1].split(')')[0]
        if item["registered_company"] == "可注册公司":
            item["registered_company"] = 1
            print(item["registered_company"])
        item["category"] = response.xpath("//div[@id='thress']/ul/li[2]/text()").extract_first().split('(')[0]