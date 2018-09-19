# -*- coding: utf-8 -*-
#便民网
#住宅出租
import re

import scrapy


class BianmingSpider(scrapy.Spider):
    name = 'house_rental'
    allowed_domains = ['sh.bqqm.com']
    start_urls = ['http://sh.bqqm.com/zufang/']

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
            item["size"] = li.xpath("./td[2]/span[2]").extract_first()
            item["contact_url"] = ""
            item["shi"] = li.xpath("./td[4]/text()").extract_first()[0]
            item["ting"] = li.xpath("./td[4]/text()").extract_first()[2]
            item["wei"] = li.xpath("./td[4]/text()").extract_first()[4]
            item["orientation"] = ""
            item["subway"] = ""
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
        item["community"] = ""
        item["address"] = response.xpath("//div[@id='thress']/ul/li[9]/text()").extract_first()
        item["rent_type"] = response.xpath("//div[@id='thress']/ul/li[3]/text()").extract_first()
        item["pay_method"] = response.xpath("//div[@id='thress']/ul/li[5]/text()").extract_first().split('(')[-1].split(')')[0].split(',')[0]
        item["phone"] = response.xpath("//div[@class='telbox']/span[2]/text()").extract_first()
        item["floor"] = response.xpath("//div[@id='thress']/ul/li[6]/text()").extract_first()
        item["floor"]=re.findall(r"第(.*?)层",item["floor"])
        item["house_allocation"] = response.xpath("//div[@id='thress']/ul/li[8]/text()").extract_first()
        item["house_types"] = ""
        item["description"] = response.xpath("//div[@class='content']/span/text()").extract()
        item["img_url"] = response.xpath("//div[@class='descriptionImg']/img/@src").extract_first()
        item["time"] = response.xpath("//div[@class='top']/span//text()").extract_first().split('：')[-1]
        item["decoration"] = response.xpath("//div[@id='thress']/ul/li[7]/text()").extract_first().split('(')[-1].split(')')[0].split(",")[1]
        item["name"] = response.xpath("//div[@id='thress']/ul/li[10]/text()").extract_first().split('：')[-1]