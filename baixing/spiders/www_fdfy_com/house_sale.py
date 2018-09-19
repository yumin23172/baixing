# -*- coding: utf-8 -*-    #需要验证码
#房东房源网
#住宅出售


import scrapy


class BianmingSpider(scrapy.Spider):
    name = 'house_sale'
    allowed_domains = ['hz.fdfy.cn']
    start_urls = ['http://hz.fdfy.cn/rent/']

    def parse(self, response):
        item = {}
        item['city'] = response.xpath("//div[@id='current-city']/text()")
        # 房屋列表页信息
        li_list = response.xpath("//div[@id='list']/ul/li")
        for li in li_list:
            item["type"] = 3
            item["bd_type"] = 4
            item["title"] = li.xpath(".//a/text()").extract_first()
            item["price"] = li.xpath("//div[@class='list03']/strong/text()").extract_first()
            item["url"] = li.xpath(".//a/@href").extract_first()
            if item["url"] is not None:
                item["url"]="http://hz.fdfy.cn/rent"+item["url"]
                yield scrapy.Request(
                    item["url"],
                    callback=self.parse_zhufang_list,
                    meta={"item": item}
                )
        # 翻页
        next_url = response.xpath("//div[@class='pager']/ul/li[11]/a/@href").extract_first()
        if next_url is not None:
            next_url = "http://hz.fdfy.cn/rent" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                meta={"item": item}

            )
    # 房屋详情页信息
    def parse_zhufang_list(self, response):
        item = response.meta["item"]
        item["area"] = response.xpath("//div[@class='cr_left']/dl[4]/dd/text()").extract_first().split(' - ')[1]
        item["street"] = response.xpath("//div[@class='cr_left']/dl[4]/dd/text()").extract_first().split(' - ')[2]
        item["community"] = response.xpath("//div[@class='cr_left']/dl[3]/dd/text()").extract_first()
        item["address"] = response.xpath("//div[@class='cr_left']/dl[4]/dd/text()").extract_first().split(' - ')[3]
        item["property_type"] = ""
        item["house_types"] = response.xpath("//div[@class='cr_left']/dl[5]/dd/text()").extract_first().split(' - ')[-1]
        item["decoration"] = response.xpath("//div[@class='cr_left']/dl[5]/dd/text()").extract_first().split(' - ')[0]
        item["phone"] = response.xpath("//div[@class='telephone']/span/text()").extract_first()
        item["description"] = response.xpath("//div[@class='infoitem']/div//text()").extract()

        item["img_url"] = response.xpath("//div[@class='desc-image even']/img/@src").extract_first()
        item["form"] = ""
        item["name"] = response.xpath("//div[@class='propInfoBox']//ul[2]/li[1]/span[2]/text()").extract_first().split('  ')[0]
        item["shi"] = response.xpath("//div[@id='propNav']/text()").extract_first().split('>  ')[-1].split(' ')[0][0]
        item["ting"] = response.xpath("//div[@id='propNav']/text()").extract_first().split('>  ')[-1].split(' ')[1][0]
        item["wei"] = response.xpath("//div[@id='propNav']/text()").extract_first().split('>  ')[-1].split(' ')[2][0]
        item["size"] = response.xpath(".//div[@class='area']").extract_first()
        item["floor"] = response.xpath(".//div[@class='info']/text()").extract_first().split('：')[-1].split('/')[0]
        item["contact_url"] = ""
        item["orientation"] = ""
        item["subway"] = ""
        item["time"] = response.xpath("//div[@class='broker']").extract_first().split('： ')[-1]