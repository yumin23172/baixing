# -*- coding: utf-8 -*-
import re
#二手房出售
import scrapy


class LiebiaoSpider(scrapy.Spider):
    name = 'house_sale'
    allowed_domains = ['beijing.liebiao.com']
    start_urls = ['http://beijing.liebiao.com/ershoufang/']

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
            item["size"] = li.xpath(".//div[@class='params']/span[2]/text()").extract_first()
            item["decoration"] = li.xpath("//div[@class='params']/span[1]/text()").extract_first()
            item["contact_url"] = ""
            item["shi"] = li.xpath(".//div[@class='params']/span[3]/text()").extract_first().split("/")[0][0]
            item["ting"] = li.xpath(".//div[@class='params']/span[3]/text()").extract_first().split("/")[0][2]
            item["wei"] = li.xpath(".//div[@class='params']/span[3]/text()").extract_first().split("/")[0][4]
            item["subway"] = ""
            item["name"] = li.xpath(".//div[@class='detail']/div[2]/div[3]/span/text()").extract_first().split('：')[-1]
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
        item["area"] = response.xpath("//div[@class='field-wrap']/div/dl[2]//dd/a[@class='region'][1]/text()").extract_first()
        if item["area"] is None:
            item["area"] = response.xpath("//div[@class='field-wrap']/div/dl[3]//dd/a[@class='region'][1]/text()").extract_first()
        item["street"] = response.xpath("//div[@class='field-wrap']/div/dl[2]//dd/a[@class='region'][2]/text()").extract_first()
        if item["street"] is None:
            item["street"] = response.xpath("//div[@class='field-wrap']/div/dl[3]//dd/a[@class='region'][2]/text()").extract_first()
        item["community"] = response.xpath("//div[@class='main-field-wrap clf']/dl[2]/dd//text()").extract_first()
        item["address"] = response.xpath("//div[@class='field-wrap']/div/dl[2]//dd//span/text()").extract_first()
        if item["address"] is None:
            item["address"] = response.xpath("//div[@class='field-wrap']/div/dl[3]//dd//span/text()").extract_first()
        item["phone"] = response.xpath("//div[@class='phone-way']//span/text()").extract_first()
        item["floor"] = response.xpath("//div[@class='dec-params clf']/dl[4]/dd/text()").extract_first()
        item["house_types"] = response.xpath("//div[@class='main-field-wrap clf']/dl[3]//dd/text()").extract_first().split('  ')[1]
        item["description"] = response.xpath("//div[@class='content-wrap']//span").extract()
        item["img_url"] = response.xpath("//div[@class='small-pic-wrap']/ul/li/@style").extract_first().split('(')[-1].split(')')[0]
        item["time"] = response.xpath("//div[@class='statistic']/span/text()").extract_first()
        item["property_type"] = response.xpath("//div[@class='dec-params clf']/dl[5]/dd/text()").extract_first()
        item["orientation"] = response.xpath("//div[@class='main-field-wrap clf']/dl[3]//dd/text()").extract_first().split('  ')[-1]