# -*- coding: utf-8 -*-
#望京网
#求租求售


import scrapy


class BianmingSpider(scrapy.Spider):
    name = 'Rent_and_purchase_general'
    allowed_domains = ['esf.wangjing.cn']
    start_urls = ['http://esf.wangjing.cn/index.php?type=hire']

    def parse(self, response):
        item = {}
        item['city'] = "北京"
        # 房屋列表页信息
        li_list = response.xpath("//div[@class='listing']/div")
        for li in li_list:
            item["type"] = 3
            item["bd_type"] = 4
            item["title"] = li.xpath(".//div[@class='title']//text()").extract_first()
            item["size"] = 0
            item["contact_url"] = ""
            item["time"] = li.xpath("//div[@class='broker']").extract_first().split('： ')[-1]
            item["price"] = li.xpath("//div[@class='price']//text()").extract_first()
            item["url"] = li.xpath(".//div[@class='photo']/a/@href").extract_first()
            if item["url"] is not None:
                item["url"] = "http://esf.wangjing.cn" + item["url"]
                yield scrapy.Request(
                    item["url"],
                    callback=self.parse_zhufang_list,
                    meta={"item": item}
                )

        # 房屋详情页信息

    def parse_zhufang_list(self, response):
        item = response.meta["item"]
        item["area"] = ""
        item["phone"] = response.xpath("//div[@class='telenumb']/text()").extract_first()
        item["description"] = response.xpath("//div[@class='propDescValue']/div[2]/p/text()").extract()
        item["form"] = ""
        item["name"] = response.xpath("//div[@class='propInfoBox']//ul[2]/li[1]/span[2]/text()").extract_first().split('  ')[0]