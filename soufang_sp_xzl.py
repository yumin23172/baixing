import base64

import requests
# from util.time_13bit import time_13bit
import json
import os
import time
import re
from lxml import etree
import execjs
from selenium import webdriver
import time

class Soufang_Cs:
    def __init__(self):
        self.n = 5
        self.ritem = {
            'error': '',  # 失败原因
            'release': '',  # 成功 1 失败 2
            'url': ''  # 成功后 url
        }
    def img(self):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; cityid=eyJpdiI6InZhZU1acXZaakZGZkJacGpnYWxTWEE9PSIsInZhbHVlIjoiMXdPWkt4Qm80dlZYZWhNRWNlV1BkZz09IiwibWFjIjoiMGVjY2Q5ZWMwMmQ4NGUwZWE2OWY1ZDhiZmI2ZDQ0NzYwNmE2MzA1OWY0MmMzZTdiYzIyY2FkZTM2MmY5Yjc4MSJ9; city=eyJpdiI6IkRGQTl6ODVWbkg5ZmU0elwvcXpTVld3PT0iLCJ2YWx1ZSI6ImZrUXNJamZ6dGkxZzc2aFZiYlJCcXlKXC95bzJyQVwvbXo0b3ZNUDNcL2dpeE9zYVhpdDJ0bnMrN0hnUlFcLzFOM0VMTFpJMVwvcTkyejd6azlJcUY1SHZvc3czUmFsc2J2ZFhhWVBaVXNEMEVzenBsMUdxMDQzaWo2ZVhTTTFEdVBcLytUWmd6Qytha2VzaHNUbXo0TmZzanVzVEx4blVzTG1pWWFqdDF3dXJqS0I2S2Y1ZThLeDVveXFBSDdCS3JRTTFjcVNjNUh0OWp5RlJZYmh2SUlhNEMzdHp2Um93aFwvMFl5QVBwZmtTTkJ6N1wvSDVmc2V2ek1JZE52cEJLZXRscitsNTJsOVFLOFFFQ1NoOHZ1Vk9XWG1SMUdKUG5iUklPYXdxdUh4c041T3p4dGM9IiwibWFjIjoiYzNiNWJlZmNhMzVkMTk5MzM3MWZmMTliY2M2NDliNmI5ZGNkOTQwYzI5NzlhYmNjMDJiYTBhZjAxMGFmMGU3NCJ9; citypy=eyJpdiI6ImFPN3VrQVhZb1BiRzBkVHBBV21OZWc9PSIsInZhbHVlIjoiWk5ubm53N2JaeGVvQ2RMN1E4dUNMZz09IiwibWFjIjoiZGQ2YmMwODUyYzk3ZDU1ZmMwNWI2MWViODExOTA3NTA1NTU1NTM3M2NiYmQwYTJhMGU2ODRhMDNkNWFiMDg0MyJ9; agent_sofang_session=0997ce38e2bf724675a9c34c8750b8138b35948f; XSRF-TOKEN=eyJpdiI6Ik5mRksrME1NYjhlRGRaVERQY0ZcL2FBPT0iLCJ2YWx1ZSI6Inc1TlhUdHI3ZEdmc3ZkNWFTQ3lQYzk5bVZYOW9uRG1Td1FXbytQd0RidGpWdXVIcjJmZHl2NGl2cXZxZnF6dmR1T3NjNmJRQnBmV2FqbFU3enNPTHhnPT0iLCJtYWMiOiI4ZGI3MjI3YzMyMjhkOGE4MzlkOGU5MTNkYTgwNTExMjkyZmIyZDE2MDg5NTY1ZjhmMTI5ZGYxMTJlYjU4NzY3In0%3D'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldsale/house',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        img_list = []
        files_name = [r'C:\Users\Admin\Pictures\Saved Pictures\text.jpg',r'C:\Users\Admin\Pictures\Saved Pictures\text1.jpg']
        for img in files_name:
            files = {'attachment_file': ('timg.jpg', open(img, 'rb'), 'image/jpeg')}
            res = requests.post('http://agent.sofang.com/upload/addphoto?imageType=houseSale',headers=headers_1,files=files).content.decode()
            image = {"img":res,"note":"","type":"10"}
            img_list.append(image)
        self.image = str(img_list).replace("'",'"')
        print(self.image)

    def roomStr(self, item):
        self.roomStr = item["shi"] + '_' + item["ting"] + '_' + item["wei"] + '_' + item["chufang"]
        return self.roomStr
    def put(self, ):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; cityid=eyJpdiI6InZhZU1acXZaakZGZkJacGpnYWxTWEE9PSIsInZhbHVlIjoiMXdPWkt4Qm80dlZYZWhNRWNlV1BkZz09IiwibWFjIjoiMGVjY2Q5ZWMwMmQ4NGUwZWE2OWY1ZDhiZmI2ZDQ0NzYwNmE2MzA1OWY0MmMzZTdiYzIyY2FkZTM2MmY5Yjc4MSJ9; city=eyJpdiI6IkRGQTl6ODVWbkg5ZmU0elwvcXpTVld3PT0iLCJ2YWx1ZSI6ImZrUXNJamZ6dGkxZzc2aFZiYlJCcXlKXC95bzJyQVwvbXo0b3ZNUDNcL2dpeE9zYVhpdDJ0bnMrN0hnUlFcLzFOM0VMTFpJMVwvcTkyejd6azlJcUY1SHZvc3czUmFsc2J2ZFhhWVBaVXNEMEVzenBsMUdxMDQzaWo2ZVhTTTFEdVBcLytUWmd6Qytha2VzaHNUbXo0TmZzanVzVEx4blVzTG1pWWFqdDF3dXJqS0I2S2Y1ZThLeDVveXFBSDdCS3JRTTFjcVNjNUh0OWp5RlJZYmh2SUlhNEMzdHp2Um93aFwvMFl5QVBwZmtTTkJ6N1wvSDVmc2V2ek1JZE52cEJLZXRscitsNTJsOVFLOFFFQ1NoOHZ1Vk9XWG1SMUdKUG5iUklPYXdxdUh4c041T3p4dGM9IiwibWFjIjoiYzNiNWJlZmNhMzVkMTk5MzM3MWZmMTliY2M2NDliNmI5ZGNkOTQwYzI5NzlhYmNjMDJiYTBhZjAxMGFmMGU3NCJ9; citypy=eyJpdiI6ImFPN3VrQVhZb1BiRzBkVHBBV21OZWc9PSIsInZhbHVlIjoiWk5ubm53N2JaeGVvQ2RMN1E4dUNMZz09IiwibWFjIjoiZGQ2YmMwODUyYzk3ZDU1ZmMwNWI2MWViODExOTA3NTA1NTU1NTM3M2NiYmQwYTJhMGU2ODRhMDNkNWFiMDg0MyJ9; agent_sofang_session=0997ce38e2bf724675a9c34c8750b8138b35948f; XSRF-TOKEN=eyJpdiI6Ijl3ZkUzZGlXdU1xRUxcL3F3ZlZ4Sit3PT0iLCJ2YWx1ZSI6IkpIXC9vb2p4WGdiQ1wvUnBYMnhac2VGUXlENmg1dDVGTmhyUWpoK2JNWTBkQUlwU0ozb01GOUxLM0hhNTZcL2JXdXAwblBubW5HMjB0MTh0emxZMlwveDNlQT09IiwibWFjIjoiMzUxYmM2NTcwMmI2Y2UxYzk0MzNlZDU0NjJmMGE2YjA0NGQ1ZDNhMGYzNzAxZDA4NzgyNjg2Zjg5NGM5Y2QyNyJ9'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldrent/house',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        data = {
            '_token': item["token"],                                #token
            'houseType1': '1',                                      #房屋类型（houseType1）
            # 'provinceId': item["provinceId"],                       #省(provinceId)
            'cityId': item["cityId"],                               #市(cityId)
            'cityareaId': item["cityareaId"],                       #区(cityareaId)
            'name': item["name"],                                   #小区(name)
            'address': item["address"],                             #地址(address)
            'communityId': item["communityId"],                     #小区id（communityId）
            "area": item["area"],                                   #面积(area)
            "price1": item["price1"],                               #出售价格 (price2)
            'priceUnit': item["priceUnit"],                         #价格单位（priceUnit）
            'fitment': item["fitment"],                             #装修状况（fitment）



            'roomStr': self.roomStr ,                            #室厅卫厨(roomStr)
            'houseType2': item["houseType2"],                       #物业类型(houseType2)
            "currentFloor": item["currentFloor"],                   #楼层(currentFloor)
            "totalFloor": item["totalFloor"],                       #总楼层(totalFloor)
            'faceTo': item["faceTo"],                               #房屋朝向（faceTo）
            "title": item["title"],                                 #标题(title)
            'describe': item["describe"],                           #描述(describe)
            'indoor':self.image,                                    #图片（indoor）
            # 'indoor': '[{"img":"/house/sale/2018_09/14/145828_1536908308_BWKT.jpg","note":"","type":"10"}]',
            # 'titleimg': '[{"img":"/house/sale/2018_09/14/145830_1536908310_DJ5K.jpg","type":"9","note":"","tag":"2"}]',
            "linkman": item["linkman"],                             #联系人(linkman)
            "linkmobile": item["linkmobile"]                        #电话(linkmobile)
        }
        print(data)
        print("*" * 80)
        url='http://agent.sofang.com/submitsale'
        res = requests.post('http://agent.sofang.com/submitsale',headers=headers_1, data=data).content.decode()
        print(res)
        self.ritem['url'] = url
        result = re.findall('''"result":(.*?),"message":"(.*?)"''', res)[0]
        if result:
            if 'false' in result:
                self.ritem['error'] = result[1]
                self.ritem['release'] = 2
                print(self.ritem['error'])
            else:
                self.ritem['release'] = 1
                print("成功")
        # print(res)
        # msg_list = re.findall('''"result":(.*?),"message":"(.*?)"''', res)[0]
        # if 'false' in msg_list:
        #     print(msg_list[1])
        # else:
        #     print('发布成功')

    def fabu(self):
        d = webdriver.Chrome('')
        time.sleep(5)
        d.get('http://agent.sofang.com/oldrentmanage/house/releaseed')
        e = d.find_element_by_xpath('/html/body/div[1]/div/dl[2]/dd[1]/a')
        if e:
            e.click()
        time.sleep(1)
        d.find_element_by_xpath('//*[@id="lproname"]').click()
        d.find_element_by_xpath('//*[@id="lproname"]').send_keys('15629185662')
        d.find_element_by_xpath('//*[@id="lpropwd"]').click()
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="lpropwd"]').send_keys('yumin135172')
        d.find_element_by_xpath('//*[@id="login"]').click()
        time.sleep(5)
        d.get('http://agent.sofang.com/oldrentmanage/house/releaseed')
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="main_r"]/div[3]/ul/li[2]/div[2]/a[2]').click()
item={
'token': 'EA5qr8p2jP4jTWXoNpH44lLb6shQqN7Wld6NKdNZ',       # 在house?rentType=1里面
"cityId":"332","cityareaId":"2985",
"price1":'124',"area":'156','priceUnit':'1',
"name":'上海月星环球商业中心',"address":'普陀中山北路3300号','communityId': '142202',
"fitment":'3',                                            #（1毛坯2简装3中装修4精装修5豪华装修）
# "roomStr":"2_2_1_1",
"shi":"2",
"ting":"2",
"wei":"1",
"chufang":"1",
"faceTo":"1",                                              #（1东2南3西4北5南北6东南7西南8东北9西北10东西）
"currentFloor":"4","totalFloor":"25",
"houseType2":"101",                                        #(302经济适用房303商住楼304别墅305豪宅306平房307四合院)
"title":"出售计上风化斤er广VC给-计较斤较斤斤计较斤斤计较",
"describe":"水水水水水水d水时间还哈工水ghplm水水法的实施",
"linkman":"张鱼","linkmobile":"15629185662",
}
if __name__ == '__main__':
    soufang = Soufang_Cs()
    soufang.img()
    soufang.roomStr(item)
    soufang.put()



# 字段：
#token
#房屋类型（houseType1）
#出租类型（rentType）[整租，合租]
#省(provinceId)
#市(cityId)
#区(cityareaId)
#小区(name)
#地址(address)
#小区id（communityId）
#面积(area)
#出售价格 (price1)
#出售价格 (price2)
#出租价格 (price)
#价格单位（priceUnit）
#装修状况（fitment）
#室厅卫厨(roomStr)
#物业类型(houseType2)
#楼层(currentFloor)
#总楼层(totalFloor)
#房屋朝向（faceTo）
#标题(title)
#描述(describe)
#图片（indoor）
#联系人(linkman)
#电话(linkmobile)
