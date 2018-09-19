# -*- coding: utf-8 -*-
#商铺租售
import scrapy


class LiebiaoSpider(scrapy.Spider):
    name = 'shop_rental_sale'
    allowed_domains = ['shanghai.baixing.com']
    start_urls = ['http://shanghai.baixing.com/qiufang/?afo=YuC']

    def parse(self, response):
        item = {}
        item['city'] = response.xpath("//div[@class='bar-left left-topbar']/a[1]").extract_first()
        # 房屋列表页信息
        li_list = response.xpath("//div[@class='post-list']/ul/li")
        for li in li_list:
            item["type"] = 3
            item["bd_type"] = 4
            item["width"] = ""
            item["length"] = ""
            item["high"] = ""
            item["manage_status"] = ""
            item["title"] = li.xpath(".//h2/a/text()").extract_first()
            item["price"] = li.xpath(".//div[@class='post-other']/p[1]/text()").extract_first()
            item["pay_method"] =""
            item["size"] = li.xpath(".//div[@class='spec-params']/span[2]/text()").extract_first()
            item["contact_url"] = ""
            item["manage_industry"] = ""
            item["house_allocation"] = ""
            item["name"] = li.xpath(".//div[@class='detail']/div[3]/span/text()").extract_first().split('：')[-1]
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
        item["address"] = response.xpath("//div[@class='field-wrap']/div/dl[2]//dd//span/text()").extract_first()
        if item["address"] is None:
            item["address"] = response.xpath("//div[@class='field-wrap']/div/dl[3]//dd//span/text()").extract_first()
        item["phone"] = response.xpath("//div[@class='phone-way']//span/text()").extract_first()
        item["floor"] =""
        item["description"] = response.xpath("//div[@class='content-wrap']//span").extract()
        item["img_url"] = response.xpath("//div[@class='small-pic-wrap']/ul/li/@style").extract_first().split('(')[-1].split(')')[0]
        item["time"] = response.xpath("//div[@class='statistic']/span/text()").extract_first()
        item["category"] = response.xpath("//div[@class='main-field-wrap clf']/dl[2]/dd/text()").extract_first()