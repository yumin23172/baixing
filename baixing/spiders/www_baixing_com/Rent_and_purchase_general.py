# -*- coding: utf-8 -*-
import scrapy


class BaixingfSpider(scrapy.Spider):
    name = 'Rent_and_purchase_general'
    allowed_domains = ['shanghai.baixing.com']
    start_urls = ['http://shanghai.baixing.com/qiufang/?afo=YuC']

    def parse(self, response):
        # 城市
        item = {}
        item['city'] = response.xpath("//div[@class='toolbar-link']/a[1]/text()").extract_first()
        # 写字楼列表页信息
        li_list = response.xpath("//div[@class='main']//li")
        for li in li_list:
            item["area"] = li.xpath(".//div/div[3]").extract_first().split('[')[-1].split(']')[0].split('-')[0]
            item["type"] = 3
            item["bd_type"] = 4
            item["title"] = li.xpath("./div/div[1]/a[1]/text()").extract_first()
            item["price"] = 0
            item["size"] = 0
            item["contact_url"] = ""
            item["name"] = ""
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

        # 写字楼详情页信息

    def parse_zhufang_list(self, response):
        item = response.meta["item"]
        item["phone"] = response.xpath("//li[@class='contact-btn-box']//strong").extract_first()
        item["description"] = response.xpath("//div[@class='viewad-text']").extract()
        item["time"] = response.xpath("//div[@class='viewad-actions']/span[1]").extract_first()

