
import json
import re

import requests
import base64

from lxml import etree
from selenium import webdriver
import time
#百姓商铺出租

class Baixing_Cs():
    def __init__(self):
        self.n = 5
    def img_post(self, file_name):
        with open(file_name, 'rb') as f:
            ls = base64.b64encode(f.read()).decode()
        s = json.dumps({"Pic-Size": "0*0", "Pic-Encoding": "base64", "Pic-Path": "/dwater/fang/big/", "Pic-Data": ls})
        self.img_url = requests.post('http://www.baixing.com/c/klog/web_image_upload_pv', data=s).content.decode()
        if self.img_url:
            print(self.img_url)
            print('图片上传成功')
        else:
            print("不稳定，转用自动化测试工具上传")
            self.img(file_name)
    def img(self,file_name):
        d = webdriver.Chrome('')
        time.sleep(5)
        d.get('http://www.baixing.com/oz/login')
        e = d.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/a')
        if e:
            e.click()
            time.sleep(2)
        d.find_element_by_xpath('//*[@id="id_identity"]/div/input').click()
        time.sleep(1)
        d.find_element_by_xpath('//*[@id="id_identity"]/div/input"]').send_keys('15629185662')
        d.find_element_by_xpath('//*[@id="id_password"]/div/input').click()
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="id_password"]/div/input').send_keys('yumin135172')
        d.find_element_by_xpath('//*[@id="id_submit"]').click()
        time.sleep(5)
        d.get('http://www.baixing.com/fabu/jingyingzhuanrang/')
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="rt_rt_1cmpipimd1g9r1pai1ib81f417un1"]/label').send_keys(file_name)
        time.sleep(2)
        t = d.find_element_by_xpath('//*[@id="id_images"]/div/div/ul/li/img').get_attribute('src')
        # 上传图片的@src
        time.sleep(5)
        d.quit()
        return t

    def put(self, item):
        cookie = '__trackId=153369057824615; _ga=GA1.2.1699710414.1533690580; __admx_track_id=4q-qUgSNd-6Gz3tEy4s91w; __admx_track_id.sig=ak4oXIw_cFpqjffy6CgMLKCjOu0; __uuid=115355059957995.5702a; appId=8brlm7ufr6863; rongSDK=websocket; au392680674_67c826f13ebfau392680674_67c826f13ebf=1535644800000; __city=wuhan; login_on_tab=0; wo_weixin_close_count=2; _gid=GA1.2.1712243544.1535954468; __t=ut5b878d3b54e0e6.67195065; __u=229702992; __c=facbddf642d4075d9fe4a62792f6c731ff6581ff; __n=%E5%B0%8F%E7%99%BE%E5%A7%9308301807317; __m=15629185662; Hm_lvt_5a727f1b4acc5725516637e03b07d3d2=1536197297,1536219395,1536222103,1536306144; trafficPopupishow=1; _auth_redirect=http%3A%2F%2Fwuhan.baixing.com%2Ffabu%2Fqiufang%2F%3F; __chat_udid=6e2f27e6-1e8e-4b39-b78b-eef4ae991f11; u229702992=1; u229702992_3229b495c1bda=1536308266491; mc=8%2C0%2C0; u229702992_3229b495c1bdau229702992_3229b495c1bda=1536308266491; navi16a90db2=120.92.13.29:80,u229702992_3229b495c1bda; bind_hint=20180907; __sense_session_pv=37; Hm_lpvt_5a727f1b4acc5725516637e03b07d3d2=1536309873; _gat=1'
        headers = {
            'host': 'www.baixing.com',
            'Referer': 'http://www.baixing.com/fabu/jingyingzhuanrang/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie
        }
        data = {
               # "posterType": "1",
               # "小区名": item["小区名"],
               "地区": "m7156",
               # "具体地点": item["具体地点"],
               # "室": item["室"],
               # "厅": item["厅"],
               # "卫": item["卫"],
               "面积": item["面积"],
               'content:':item["描述"],
               # "楼层": item["楼层"],
               # "总楼层": item["总楼层"],
               # "房间朝向": "东",
               # "装修情况": "毛坯房",
               # "房屋类型": "公寓",
               # "建筑年代": item["建筑年代"],
               # "是否满二": "1",
               # "唯一住房": "1,",
               "价格": item["价格"],
               "title": item["标题"],
               "contact": item["电话"],
               'allowChatOnly': '0',
               'token': 'a41c93fdd58564cd58ffdb594ff6d390',
               '8cb44b44cba8fde': '25d2d34a491536544184',
               'spread_type': '5',
               'agreement':'on'
        }

        url = 'http://www.baixing.com/fabu/jingyingzhuanrang/'
        res = requests.post(url, headers=headers, data=data)
        print(res.content.decode())

item = {}
# item["城市"] = "武汉"
# item["小区名"] = "菱湖上品(江汉-唐家墩)"
# item["具体地点"]="唐家墩路21附"

# item["地段"] = "丁字桥路60号小区"
# #
# item["所在区域"] = {
#               "localArea": "1399",
#               "localDiduan": "6184",
#               "dizhi": "丁字桥路60号小区", }
# item["室"]="2",
# item["厅"]="2",
# item["卫"]="3",
# item["楼层"] = "3"
# item["总楼层"] = "23"
item["面积"]="120"
# item["建筑年代"] = "2006"
item["价格"] = "4000"
item["标题"] = "阿三的风格"
item["描述"] = "配套齐全汇佳大厦200平方写字楼低价出售阿史夫人的酸涩的风格"
item["电话"] = "15629185662"

if __name__ == '__main__':
    baixing = Baixing_Cs()
    baixing.put(item)

