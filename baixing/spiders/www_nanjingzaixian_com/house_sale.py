# -*- coding: utf-8 -*-

#住宅出售
import re

import scrapy


class NanjingzaixianSpider(scrapy.Spider):
    name = 'house_sale_nanjing'
    allowed_domains = ['www.025002.com']
    start_urls = ['http://www.025002.com/post/fangwu/chushou/gr/list-0-0-0-0-0-2-1-0-0-0-0-0.html']

    # 房屋列表页区域划分
    def parse(self, response):
        item = {}
        li_list = response.xpath("//div[@class='men-ys']/ul/li[1]/span[position()>2]")
        for li in li_list:
            item["area"] = li.xpath("./a/text()").extract_first()
            area_url = li.xpath("./a/@href").extract_first()
            if area_url:
                a_url = "http://www.025002.com" + area_url
                yield scrapy.Request(
                    url=a_url,
                    callback=self.parse_list,
                    meta={"item": item}
                )
    # 房屋列表页信息
    def parse_list(self, response):
        item = {}
        li_list = response.xpath("//div[@id='newscontent']//ul/li")
        for li in li_list:
            item["title"] = li.xpath("./div[2]//a/text()").extract_first()
            url = li.xpath("./div[2]//a/@href").extract_first()
            if url:
                item["url"] = "http://www.025002.com" + url
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
        item['city'] = "南京"
        item["street"] = ""
        community = response.xpath("//div[@class='neirong']/dl[1]/dd[7]/text()").extract_first()
        if community:
            item["community"] = response.xpath("//div[@class='neirong']/dl[1]/dd[7]/text()").extract_first()
        else:
            item["community"] = ""
        address= response.xpath("//div[@class='neirong']/dl[1]/dd[8]/text()").extract_first()
        if address:
            item["address"] = response.xpath("//div[@class='neirong']/dl[1]/dd[8]/text()").extract_first()
        else:
            item["address"] =""
        item["type"] = 3
        item["bd_type"] = 1
        price = response.xpath("//div[@class='neirong']/dl[1]//b/text()").extract_first()
        if price:
            if "面议" in price:
                item["price"] = float(0)
            else:
                p = response.xpath("//div[@class='neirong']/dl[1]//b/text()").extract_first()
                item["price"]=float(p)
        else:
            item["price"] =float(0)
        size=response.xpath("//div[@class='neirong']/dl[1]//dd[3]/text()").extract_first()
        if size:
            if "室" in size:
                shi=response.xpath("//div[@class='neirong']/dl[1]//dd[3]/text()").extract_first().strip("\r\n ").replace(" ","").split("-")[0][0]
                if "二" in shi:
                    s="2"
                    item["shi"] = int(s)
                else:
                    item["shi"]=int(shi)
            if "厅" in size:
                ting = response.xpath("//div[@class='neirong']/dl[1]//dd[3]/text()").extract_first().strip("\r\n ").replace(" ","").split("-")[0][2]
                if "两" in ting:
                    s="2"
                    item["shi"] = int(s)
                else:
                    item["ting"] = int(ting)
            if "卫" in size:
                wei = response.xpath("//div[@class='neirong']/dl[1]//dd[3]/text()").extract_first().strip("\r\n ").replace(" ","").split("-")[0][4]
                item["wei"] = int(wei)
            else:
                item["wei"] =0
            if "㎡" in size:
                size = response.xpath("//div[@class='neirong']/dl[1]//dd[3]/text()").extract_first().strip("\r\n ").replace(" ","").split("-")[-1].replace("㎡","")
                item["size"] = float(size)
        item["phone"] = response.xpath("//div[@class='neirong']/dl[1]/dd[11]/i/text()").extract_first()
        item["contact_url"] = ""
        orientation = response.xpath("//div[@class='neirong']/dl[1]/dd[6]/text()").extract_first()
        if orientation:
            item["orientation"] = response.xpath("//div[@class='neirong']/dl[1]/dd[6]/text()").extract_first().split("-")[-1]
        else:
            item["orientation"] =""
        item["subway"] =""
        floor = response.xpath("//div[@class='neirong']/dl[1]/dd[4]/text()").extract_first()
        if floor:
            item["floor"] = response.xpath("//div[@class='neirong']/dl[1]/dd[4]/text()").extract_first().replace("\r\n ","").strip(" ").replace(" ","")
        else:
            item["floor"] = ""
        decoration = response.xpath("//div[@class='neirong']/dl[1]/dd[6]/text()").extract_first()
        if decoration:
            item["decoration"] = response.xpath("//div[@class='neirong']/dl[1]/dd[6]/text()").extract_first().split("-")[0]
        else:
            item["decoration"] = ""
        item["house_types"] = ""
        description = response.xpath("//div[@class='show-con twocon']/div/p/text()").extract_first()
        if description:
            item["description"] = response.xpath("//div[@class='show-con twocon']/div/p/text()").extract_first().replace("\xa0","").replace("\u3000","")
        else:
            item["description"] = "暂无描述"
        img_url = response.xpath("//div[@class='show-con twocon']/div/div/img/@src").extract_first()
        if img_url:
            item["img_url"] = response.xpath("//div[@class='show-con twocon']/div/div/img/@src").extract_first()
        else:
            item["img_url"] = ""
        item["time"] = response.xpath("//div[@class='balefthead']/span[1]/text()").extract_first().split(" ")[0].split("：")[-1]
        item["property_type"] = ""
        name = response.xpath("//div[@class='neirong']/dl[1]/dd[9]/text()").extract_first()
        if name:
            item["name"] = response.xpath("//div[@class='neirong']/dl[1]/dd[9]/text()").extract_first()
        else:
            item["name"] = ""
        item["from"] = ""
        yield item
