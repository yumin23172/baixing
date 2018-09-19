# -*- coding: utf-8 -*-
#望京网
#住宅出售
import re

import scrapy


class BianmingSpider(scrapy.Spider):
    name = 'house_sale'
    allowed_domains = ['esf.wangjing.cn']
    start_urls = ['http://esf.wangjing.cn/index.php?type=sale&realtype=1&page={}'.format(n for n in range(1,159))]

    def parse(self, response):
        item = {}
        item['city'] = "北京"
        # 房屋列表页信息
        li_list = response.xpath("//div[@class='listing']/div")
        for li in li_list:
            item["type"] = 3
            item["bd_type"] = 4
            item["title"] = li.xpath(".//div[@class='title']//text()").extract_first()
            item["size"] = li.xpath(".//div[@class='area']").extract_first()
            item["floor"] = li.xpath(".//div[@class='info']/text()").extract_first().split('：')[-1].split('/')[0]
            item["contact_url"] = ""

            item["orientation"] = ""
            item["subway"] = ""
            item["time"] = li.xpath("//div[@class='broker']").extract_first().split('： ')[-1]

            item["price"] = li.xpath("//div[@class='price']//text()").extract_first()
            item["url"] = li.xpath(".//div[@class='photo']/a/@href").extract_first()
            if item["url"] is not None:
                item["url"]="http://esf.wangjing.cn"+item["url"]
                yield scrapy.Request(
                    item["url"],
                    callback=self.parse_zhufang_list,
                    meta={"item": item}
                )

    # 房屋详情页信息
    def parse_zhufang_list(self, response):
        item = response.meta["item"]
        item["area"] = ""
        item["street"] = ""
        item["community"] = ""
        item["address"] = response.xpath("//div[@class='propInfoBox']/ul/li[6]/span/text()").extract_first()
        item["property_type"] = ""
        item["phone"] = response.xpath("//div[@class='telenumb']/text()").extract_first()
        item["house_types"] = response.xpath("//div[@class='propInfoBox']/ul/li[3]/span/a/text()").extract_first()
        item["description"] = response.xpath("//div[@class='propDescValue']/div[2]/p/text()").extract()
        item["img_url"] = response.xpath("//div[@style='text-align: center']//tr[2]/td/a/img/@src").extract_first()
        if item["img_url"] is not None:
            item["img_url"]="http://esf.wangjing.cn"+item["img_url"]
        item["form"] = ""
        item["decoration"] = response.xpath("//div[@id='propNav']/text()").extract_first().split('>  ')[-1].split(' ')[4]
        item["shi"] = response.xpath("//div[@id='propNav']/text()").extract_first().split('>  ')[-1].split(' ')[0][0]
        item["ting"] = response.xpath("//div[@id='propNav']/text()").extract_first().split('>  ')[-1].split(' ')[1][0]
        item["wei"] = response.xpath("//div[@id='propNav']/text()").extract_first().split('>  ')[-1].split(' ')[2][0]
        item["name"] = response.xpath("//div[@class='propInfoBox']//ul[2]/li[1]/span[2]/text()").extract_first().split('  ')[0]