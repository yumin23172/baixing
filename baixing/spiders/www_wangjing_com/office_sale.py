# -*- coding: utf-8 -*-
#望京网
#写字楼出售无信息
import re

import scrapy


class BianmingSpider(scrapy.Spider):
    name = 'office_sale'
    allowed_domains = ['esf.wangjing.cn']
    start_urls = ['http://esf.wangjing.cn/index.php?type=sale&realtype={}'.format(n for n in range(1,7))]

    def parse(self, response):
        pass