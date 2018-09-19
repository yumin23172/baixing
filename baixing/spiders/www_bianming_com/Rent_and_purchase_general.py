# -*- coding: utf-8 -*-
#便民网
#求租求售


import scrapy


class BianmingSpider(scrapy.Spider):
    name = 'Rent_and_purchase_general'
    allowed_domains = ['sh.bqqm.com']
    start_urls = ['http://sh.bqqm.com/qiuzu/']

    def parse(self, response):
        item = {}
        item['city'] = response.xpath("//div[@class='bar_left']/b/text()").extract_first()
        # 房屋列表页信息
        li_list = response.xpath("//div[@id='main']//tr")
        for li in li_list:
            item["type"] = 3
            item["bd_type"] = 4
            item["title"] = li.xpath("./td[1]/a/text()").extract_first()
            item["price"] = li.xpath("./td[2]").extract_first()
            item["size"] = ""
            item["contact_url"] = ""
            item["form"] = ""
            item["url"] = li.xpath("./td[1]/a/@href").extract_first()
            if item["url"] is not None:
                item["url"]="http://sh.bqqm.com"+item["url"]
                yield scrapy.Request(
                    item["url"],
                    callback=self.parse_zhufang_list,
                    meta={"item": item}
                )
        # 不翻页，只有一页

    # 房屋详情页信息
    def parse_zhufang_list(self, response):
        item = response.meta["item"]
        item["area"] =response.xpath("//div[@id='thress']/ul/li[1]/text()").extract_first()
        item["phone"] = response.xpath("//div[@class='telbox']/span[2]/text()").extract_first()
        item["description"] = response.xpath("//div[@class='content']/span/text()").extract()
        item["time"] = response.xpath("//div[@class='top']/span//text()").extract_first().split('：')[-1]
        item["name"] = response.xpath("//div[@id='thress']/ul/li[8]/text()").extract_first()
