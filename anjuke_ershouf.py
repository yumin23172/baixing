import json
import re

import requests
import base64

from lxml import etree
from selenium import webdriver
import time
#安居客二手房

class Anjuke_Cs:
    def __init__(self):
        self.n = 5

    def img(self, name):
        d = webdriver.Chrome('')
        time.sleep(5)
        d.get('https://vip.anjuke.com/house/publish/ershou/')
        e = d.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/span[2]')
        if e:
            e.click()
        time.sleep(1)
        d.find_element_by_xpath('//*[@id="loginName"]').click()
        d.find_element_by_xpath('//*[@id="loginName"]').send_keys('15629185662')
        d.find_element_by_xpath('//*[@id="loginPwd"]').click()
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="loginPwd"]').send_keys('yumin135172')
        d.find_element_by_xpath('//*[@id="loginSubmit"]').click()
        time.sleep(5)
        d.get('https://vip.anjuke.com/house/publish/ershou/')
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="room_fileupload"]').send_keys(''
            'C:\\Users\Admin\Pictures\Saved Pictures\\3b87e950352ac65ca217f7fbf1f2b21193138a2c.jpg')
        time.sleep(2)
        d.find_element_by_xpath('//*[@id="room_fileupload"]').send_keys(
            'C:\\Users\Admin\Pictures\Saved Pictures\\8b13632762d0f703ea7608fb02fa513d2797c5d5.jpg')
        time.sleep(2)
        d.find_element_by_xpath('//*[@id="room_fileupload"]').send_keys(
            'C:\\Users\Admin\Pictures\Saved Pictures\\1462888527153aa.jpg')
        time.sleep(2)
        d.find_element_by_xpath('//*[@id="model-fileupload"]').send_keys(
            'C:\\Users\Admin\Pictures\Saved Pictures\\b3119313b07eca80b2628a139b2397dda04483db.jpg')
        time.sleep(2)
        d.find_element_by_xpath('//*[@id="room-upload-display"]/div[1]/div/i[1]').click()
        time.sleep(1)
        t1 = d.find_element_by_xpath('//*[@id="room-upload-display"]/div[1]/img').get_attribute('src')
        t2 = d.find_element_by_xpath('//*[@id="room-upload-display"]/div[2]/img').get_attribute('src')
        t3 = d.find_element_by_xpath('//*[@id="room-upload-display"]/div[3]/img').get_attribute('src')
        t4 = d.find_element_by_xpath('//*[@id="model-upload-display"]/div[1]/img').get_attribute('src')
        # 上传图片的@src
        time.sleep(5)
        d.quit()
        return t1,t2,t3,t4
    def put(self):
        cookie = '_ga=GA1.2.1457586794.1534207850; 58tj_uuid=57438cea-0748-4609-b1ae-f7f5c4f5a234; als=0; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1534466717,1535505603; ctid=11; aQQ_brokerguid=37224B3E-0AD2-E82C-F672-1B25EBFA866A; _gid=GA1.2.933466498.1536032059; __xsptplus8=8.10.1536033245.1536033245.1%232%7Cwww.baidu.com%7C%7C%7Cvip.anjuke%7C%23%23aXjaTtedJB0tHLXw5qHOdJ0N7nTpjqRx%23; lui=74969145%3A2; sessid=24F302A8-D277-2F2C-E3B3-CD41D47C0754; lps=http%3A%2F%2Flogin.anjuke.com%2Flogin%2Fverify%3Ftoken%3D3022e333ccfe3ea116c4ff14558efc14%26source%3D1%7Chttps%3A%2F%2Fvip.anjuke.com%2Flogin; twe=2; init_refer=https%253A%252F%252Fvip.anjuke.com%252Flogin%253Fhistory%253DaHR0cDovL3ZpcC5hbmp1a2UuY29tL2hvdXNlL3B1Ymxpc2gvZXJzaG91Lw%253D%253D; new_uv=7; anjukereg=6kXZHhTKf4HTNVSn; aQQ_ajkguid=5B1877E1-A01D-08E8-6B54-BD510EAB519F; ajk_member_id=74969145; ajk_member_name=U15360539999387; ajk_member_key=017e942b14dd9e63c0c54dfa1fb700e0; ajk_member_time=1567646520; aQQ_ajkauthinfos=7R7bEUaZItPWNV%2BpcSBRv%2FtsQ1SGR1siOJoRSW3YCDdy4XLyK09C9cdKYDcEzGgM%2FBQTgSoiXZrnyCZCRwyvjd1o7w; new_session=0; ajk_broker_id=6544973; ajk_broker_ctid=11; ajk_broker_uid=43831982; aQQ_brokerauthinfos=OoTZfSZlbdSA%2BzAx8i4D8DN1bsDp43%2F3234VIoK9Ll3wy9ixW7JDIV1xRRq3hGoElHnvF0UJ64qWnAeU4aHOordLfJBqA8FN1dWcRXsI44yB%2BdzhKSDulrA1ROozZZfXZNGKrbzrfAmXgMVTg%2F4KWWQI299xEhAC6jgzSrgbJhczGKrFY6qSw8w9Q890Gmaz6rUCfdqOqAYCrQ6ZPUZPzF7MNA'
        headers = {

            'Referer': 'https://vip.anjuke.com/house/publish/ershou/?from=manage',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie
        }
        data = {
            "community_unite": item["小区名称"],
            "xiaoquId":'100526713',
            "shi": item["室"],
            "ting": item["厅"],
            "wei": item["卫"],
            "params_16":'1',
            "zhuangXiuQingKuang": '4',
            "chaoXiang": '2',
            "params_17": '1',
            "suoZaiLouCeng": item["楼层"],
            "zongLouCeng": item["总楼层"],
            "params_19": item["户"],
            "params_82": '2',
            "params_20": item["室"],
            "params_83": '2',
            "params_21": item["号"],
            "mianJi": item["建筑面积"],
            "params_12": item["套内面积"],
            "params_24":'1',
            "params_81": '2',
            "params_14": item["建造年代"],
            "params_22": '1',
            "params_26": '2',
            "params_25": '1',
            "params_18": '1',
            "params_29": '0.5',
            "jiaGe": item["售价"],
            "title": item["标题"],
            "content_fangyuanxiangqing": item["房源详情"],
            "content_yezhuxintai": item["业主心态"],
            "content_xiaoqupeitao": item["小区配套"],
            "content_fuwujieshao": item["服务介绍"],
        }
        url = "https://vip.anjuke.com/ajax/community/check_price"
        res = requests.post(url, headers=headers, data=data).content.decode()
        print(res)
        msg_list = re.findall('status":"(.*?)","msg":"(.*?)"', res)
        print(msg_list)
        # if 'error' in msg_list[0]:
        #     print(msg_list[1])
        # else:
        #     print('发布成功')
item = {}
item["小区名称"] = "S半岛清水湾花园"
item["室"] = "1"
item["厅"] = "1"
item["卫"] = "1"
item["楼层"] = "2"
item["总楼层"] = "23"
item["户"] = "2"
item["室"] = "3"
item["号"] = "1"
item["建筑面积"] = "136"
item["套内面积"] = "100"
item["建造年代"] = "2011"
item["售价"] = "258"
item["标题"] = "坡度是阿萨德；法国全的方好法境但是风格和他人 "
item["房源详情"] = "阿德在法国和然他很温万元一堂下次课的兔可独雨客恶意团结统一基督徒当然建议对人体环境"
item["业主心态"] = "阿道夫干堂课的兔可独客恶意团次结统一基督当然建议点燃火炬天阿德在法国和然他很温万元一堂课的兔可独雨客恶意团结统一基督徒当然建议对人体环境"
item["小区配套"] = "图哈特特万元一堂课的兔可独听想雨客恶意团统一基督徒当然建身份认同感和阿德在法国和然他很温万元一堂课的兔可独雨客恶意团结统一基督徒当然建议对人体环境"
item["服务介绍"] = "人生已经饿一天温柔元一堂课的需兔可独听雨客恶意团结统一基督徒当然同时让她还有"
if __name__ == '__main__':
    anjuke = Anjuke_Cs()
    anjuke.put()