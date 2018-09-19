# -*- coding: utf-8 -*-

#求租求售


import scrapy


class NanjingzaixianSpider(scrapy.Spider):
    name = 'Rent_and_purchase_general'
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
        item["type"] = 3
        item["bd_type"] = 4
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
        item["phone"] = response.xpath("").extract_first()
        item["contact_url"] = ""
        description = response.xpath("").extract_first()
        if description:
            item["description"] = response.xpath("").extract_first()
        else:
            item["description"] = ""
        item["time"] = response.xpath("").extract_first()
        name = response.xpath("").extract_first()
        if name:
            item["name"] = response.xpath("").extract_first()
        else:
            item["name"] = ""
        item["from"] = response.xpath("").extract_first()

