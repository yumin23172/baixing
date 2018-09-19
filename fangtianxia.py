import json
import re

import requests
import base64

from lxml import etree
from selenium import webdriver
import time


class Fangtianxia:
    def __init__(self):
        self.n = 5

    def denglu(self):
        d = webdriver.Chrome('')
        time.sleep(5)
        d.get('https://passport.fang.com/')
        e = d.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/dt/span[2]')
        if e:
            e.click()
        time.sleep(1)
        d.find_element_by_xpath('//*[@id="username"]').click()
        d.find_element_by_xpath('//*[@id="username"]').send_keys('15629185662')
        d.find_element_by_xpath('//*[@id="password"]').click()
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="password"]').send_keys('yumin135172')
        d.find_element_by_xpath('//*[@id="loginWithPswd"]"]').click()
        time.sleep(5)
        d.get('http://sh.esf.fang.com/usercenter/HousePublish/Ebhousepublish/')
        time.sleep(5)
        d.quit()
    def put(self,item):
        cookie = 'integratecover=1; global_cookie=xduam2d4cb6shf936d1bqrh9o1mjkt4l2fi; Integrateactivity=notincludemc; SoufunSessionID_Rent=3_1535503357_12462; showAdsh=1; searchLabelN=3_1536280768_18962%5B%3A%7C%40%7C%3A%5D991bf5aa36ddfcafe651e199aecceab9; searchConN=3_1536280768_19033%5B%3A%7C%40%7C%3A%5D6bd0ef10f2f678f8326a8cc330f71607; logGuid=ee0a1a3d-f397-4d41-8b26-7d25735ca40c; city=sh; new_loginid=107943560; token=298ef8bd509744afa842d1c34505e2da; sfut=A5975D3BDAEC98AEA86B3B2FF46CB157DF2F73E3F9C60F01B6DA9D11ACF7CAE64A17FD041BA6EFFA24C1D193514685095FF14B9021849950A5B6CD10D4C885C95D6323DD02004F4C18D74120764478FE52F84828BBBB098DBDA00D1DE8E0CA9A; sf_source=; s=; indexAdvLunbo=lb_ad5%2C0; Captcha=725272524F6468566E4535467753474A493152702B6E65756E475463756E62586B6E566933744467797A596657702F487971753278757379356254694E53326269315650517546386448773D; new_loginid=107943560; login_username=yumin6492865873; unique_cookie=U_8sqg6flnehg90ebrn33ptsmrt1ujlr9vym0*88'
        headers = {
            'Host': 'sh.esf.fang.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie
        }
        data = {
            "input_House_ProjName": item["小区名称"],
            "input_House_Dong": item["栋"],
            "input_House_danyuan": item["单元"],
            "input_House_Fang": item["号"],
            "input_House_Room":item["室"],
            "input_House_Hall": item["厅"],
            "input_House_Toilet": item["卫"],
            "input_House_BuildingArea": item["面积"],
            "input_House_Floor": item["楼层"],
            "input_House_TotalFloor":  item["总楼层"],
            "slt_House_Forward_Select": '南北',
            "input_House_Price": item["价格"],
            "input_LinkMan":item["称呼"],
            "linksex": '0',
            'input_MobileCode':'15629185662',
            'slt_House_JinRong':'是'
        }
        url = "http://sh.esf.fang.com/UserCenter/HousePublish/EbHousePublishSave"
        res = requests.post(url, headers=headers, data=data)
        print(res.content)
        # res_1 = re.findall('''info":"(.*?)","status":"(.*?)"''', res)[0]
        # if  res_1[1]=='n':
        #     print(res_1[0])
        # else:
        #     print('发布成功')

item = {}
item["小区名称"] = "万城理想公馆"
item["单元"]='1'
item["号"]='2'
item["栋"]='1'
item["室"]='1'
item["厅"]='1'
item["卫"]='1'
item["面积"]='123'
item["楼层"]='3'
item["总楼层"]='30'
item["价格"]='254'
item["称呼"]='胡女生'
if __name__ == '__main__':
    fangtianxia =Fangtianxia()
    fangtianxia.put(item)