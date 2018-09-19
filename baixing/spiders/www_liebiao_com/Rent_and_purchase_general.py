# -*- coding: utf-8 -*-
#求租
import scrapy


class LiebiaoSpider(scrapy.Spider):
    name = 'Rent_and_purchase_general'
    allowed_domains = ['beijing.liebiao.com']
    start_urls = ['http://beijing.liebiao.com/qiuzufang/']

    def parse(self, response):
        item = {}
        item['city'] = response.xpath("//div[@class='bar-left left-topbar']/a[1]").extract_first()
        # 房屋列表页信息
        li_list = response.xpath("//div[@class='post-list']/ul/li")
        for li in li_list:
            item["type"] = 3
            item["bd_type"] = 4
            item["title"] = li.xpath(".//h2/a/text()").extract_first()
            item["price"] = li.xpath(".//div[@class='post-other']/p[1]/text()").extract_first()
            item["size"] = ""
            item["contact_url"] = ""
            item["form"] = ""
            item["url"] = li.xpath(".//h2/a/@href").extract_first()
            if item["url"] is not None:
                yield scrapy.Request(
                    item["url"],
                    callback=self.parse_zhufang_list,
                    meta={"item": item}
                )
        # 翻页
        next_url = response.xpath("//div[@class='pager']/ul/li[12]/a/@href").extract_first()
        yield scrapy.Request(
            next_url,
            callback=self.parse,
            meta={"item": item}

        )

        # 房屋详情页信息

    def parse_zhufang_list(self, response):
        item = response.meta["item"]
        item["area"] = response.xpath("//div[@class='field-wrap']/div/dl[3]//dd/a[@class='region'][1]/text()").extract_first()
        item["phone"] = response.xpath("//div[@class='phone-way']//span/text()").extract_first()
        item["description"] = response.xpath("//div[@class='content-wrap']/p/text()").extract()
        item["time"] = response.xpath("//div[@class='statistic']/span/text()").extract_first()
        item["name"] = response.xpath("//div[@class='field-wrap']//dl[2]/dd/span/text()").extract_first()
