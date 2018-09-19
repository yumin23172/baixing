# -*- coding: utf-8 -*-
#百姓网
import scrapy


class BaixingfSpider(scrapy.Spider):
    name = 'house_rental'
    allowed_domains = ['shanghai.baixing.com']
    start_urls = ['http://shanghai.baixing.com/xinfangchushou/?afo=Jlc']

    def parse(self, response):
        item = {}
        item['city'] = response.xpath("//div[@class='toolbar-link']/a[1]/text()").extract_first()
        # 房屋列表页信息
        li_list = response.xpath("//div[@class='main']//li")
        for li in li_list:
            item["area"] = li.xpath(".//div/div[3]").extract_first().split('[')[-1].split(']')[0].split('-')[0]
            item["street"] = li.xpath(".//div/div[3]").extract_first().split('[')[-1].split(']')[0].split('-')[1]
            item["community"] = li.xpath(".//div/div[3]").extract_first().split('[')[-1].split(']')[0].split('-')[2]
            item["address"] = li.xpath(".//div/div[3]").extract_first().split('[')[0]
            item["type"] = 3
            item["bd_type"] = 4
            item["rent_type"] = li.xpath(".//div/div[3]").extract_first()
            item["title"] = li.xpath("./div/div[1]/a[1]/text()").extract_first()
            item["pay_method"] = li.xpath("./div/div[1]/a/text()").extract_first()
            item["price"] = li.xpath("./div/div[1]/span/text()").extract_first()
            item["size"] = li.xpath("./div/div[2]").extract_first().split("/")[1]
            item["contact_url"] = li.xpath("./").extract_first()
            item["shi"] = li.xpath("./div/div[2]").extract_first().split("/")[0][0]
            item["ting"] = li.xpath("./div/div[2]").extract_first().split("/")[0][2]
            item["wei"] = li.xpath("./div/div[2]").extract_first().split("/")[0][4]
            item["orientation"] = li.xpath("./div/div[2]").extract_first().split("/")[2]
            item["floor"] = li.xpath("./div/div[2]").extract_first().split("/")[4]
            item["subway"] = li.xpath("./div/div[2]").extract_first().split("/")[4]
            item["house_allocation"] = li.xpath("./div/div[2]").extract_first().split("/")[4]
            item["name"] = ""
            item["form"] = response.xpath("./").extract_first()
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

        # 房屋详情页信息

    def parse_zhufang_list(self, response):
        item = response.meta["item"]
        item["phone"] = response.xpath("//li[@class='contact-btn-box']//strong").extract_first()
        item["decoration"] = response.xpath("//div[@class='viewad-meta2']/div[1]/label[2]/@title").extract_first()
        item["house_types"] = response.xpath("//div[@class='viewad-meta2']/div[4]/label[2]/@title").extract_first()
        item["description"] = response.xpath("//section[@class='viewad-description']/div[2]").extract()
        item["img_url"] = response.xpath("//div[@class='featured-height']/div/a/@style").extract_first().split('(')[-1].split(')')[0]
        item["time"] = response.xpath("//div[@class='viewad-actions']/span[2]").extract_first()
