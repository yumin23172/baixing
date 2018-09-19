import json
import re

import requests
import base64

from lxml import etree
from selenium import webdriver
import time


class First_Time:
    def __init__(self):
        self.n = 5

    def img(self, name):
        d = webdriver.Chrome('')
        time.sleep(5)
        d.get('http://sz.01fy.cn/member/houseSale.php')
        e = d.find_element_by_xpath('//*[@id="normal-login"]')
        if e:
            e.click()
        time.sleep(1)
        d.find_element_by_xpath('//*[@id="username"]').click()
        d.find_element_by_xpath('//*[@id="username"]').send_keys('15629185662')
        d.find_element_by_xpath('//*[@id="passwd"]').click()
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="passwd"]').send_keys('yumin135172')
        d.find_element_by_xpath('//*[@id="loginform"]/div[5]/input').click()
        time.sleep(5)
        d.get('http://sz.01fy.cn/member/houseSale.php')
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="rt_rt_1cmorm4masut65n1s9v1oe91eme1"]/label').send_keys(name)
        time.sleep(2)
        t = d.find_element_by_xpath('//*[@id="container_picture_WU_FILE_0"]/a/img').get_attribute('src')
        # 上传图片的@src
        time.sleep(5)
        d.quit()
        return t
    def put(self):
        cookie = 'access_uid=66002083; renthouse_rent=x%DAu%8F%DD%0E%820%0C%85%DFe%D7%5C%0CJ%3B%CA%AB%88%21%B0%9FH%22B%94%5D%18%E3%BB%DB%99%90+%91%9B%93%D3%B3v%FDzz%A9%C1%A9ZA%C9%BA%A0%8AT%A6%C6o%A0%C5-%C3r%F5%E2%9BH%D6%99%26%B2%B7%BE%89%95%F3%01%F3%26%22%04%93%B4%94%CC%90%EB%E5%85m%21%0A%18%24a%27J%05%88r%60%5E%3B%09%7B%9D%3Ct%A2%5C%C8%0F%E4%A8%DB%F6%CB%E2%CB%14%1F%BE%BDO%D3%A8jX%CB%F9%3EX%A1%01%D0%3AS%F16%2C%ED%F2%9C%13%5E%AE%DE%D9%F6%0C%A3%F3%833L%AF%05%13-%CBZ%83%90%40%82%85%15%04%A1%A3_p%130%01z%A4%DD%EC%11l%BE%87%AD%FE%C0%9E%3F%B9%21qb; salehouse_sale=x%DA%5D%8E%C9%0A%C30%10C%FFe%CE9xO%26%BFR%97%90%C5%A6%06g%21%F1%1CJ%E9%BFwR%C8%A1%BD%08%E9%81%84n%2FH%13%B4%D0%18tZ+T0%7F%B3%60WR%C9%81%BD%27%8B%AA%F6%E4%26%D7%7Bjt%10%ACFNL%2C%8E%A7%0EL%5Cm%A5%27%13%9A%93%283%9C%AA%23we%E4%96%B5%2Ax%C2%88%C8%5E%9Bp%B5%AC%D6%FD%EF%FE%FF%02%1Fy%ACt%84n_%D7%19Zu%C5mO%23%BF%93JT%40K%2A%5Dyn%9C%17%CA%F9%7D%FF%00%7F%60B%00; Hm_lvt_dab72e550be0fa0f04610109fd49072a=1536198621,1536198682,1536221462,1536281945; PHPSESSID=qh088legj6ivpi8h4ns5bct9n1; FY_AUTH_MEMBER_STRING=QlFUQFZeVlkLEUBXa1BaXAMWVlkXVFlmDVlGFgRmVlldUBFdAktUYQ; FY_AUTH_MEMBER_NAME=15629185662; FY_hide_member_ad=1; FY_cityid=4; Hm_lpvt_dab72e550be0fa0f04610109fd49072a=1536283092'
        headers = {
            'Host': 'sz.01fy.cn',
            'Referer': 'http://sz.01fy.cn/sale/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie
        }
        url = "http://sz.01fy.cn/ajax/index.php?action=is_house_exist"

        data = {
            "house_type":'1',
            "borough_name": item["小区名称"],
            "cityarea_name": item["区域"],
            "cityarea2_name": item["片区"],
            "house_address": item["详细地址"],
            "house_age":item["建筑年代"],
            "house_floor": item["楼层"],
            "house_topfloor": item["总楼层"],
            "elevator_caption": '1',
            "parking_lot_caption": '1',
            "house_room": '1',
            "house_hall": '1',
            "house_toilet": '1',
            "house_veranda": '2',
            "house_totalarea":item["面积"],
            "house_price": item["价格"],
            "house_fitment": '3',
            "house_toward": '3',
            "house_title": item["标题"],
            "house_desc": item["房源描述"],
            "owner_name": '鱼鱼',

        }
        res = requests.post(url, headers=headers, data=data).content.decode()
        print(res)
        res_1 = re.findall('''info":"(.*?)","status":"(.*?)"''', res)[0]
        if  res_1[1]=='n':
            print(res_1[0])
        else:
            print('发布成功')

item = {}
item["小区名称"] = "岁的法国"
item["区域"]='罗湖'
item["片区"]='东门'
item["详细地址"]='岁的法国'
item["建筑年代"]='2008'
item["楼层"]='1'
item["总楼层"]='20'
item["面积"]='123'
item["价格"]='256'
item["标题"]='罗湖东门岁的法国1室1厅1卫'
item["房源描述"]='哦思考的骗局奥术飞弹哦是频繁地根据'
if __name__ == '__main__':
    firsttime =First_Time()
    # firsttime.img()
    firsttime.put()