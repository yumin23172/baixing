import json
import re

import requests
import base64

from lxml import etree
from selenium import webdriver
import time
#赶集商铺出售

class Ganji_Cs:
    def __init__(self):
        self.n = 5
    def city(self):
        response = requests.get('http://www.ganji.com/index.htm').content.decode()
        res = etree.HTML(response)
        city_id_dict = {}
        a_list = res.xpath('//h2[text()="按照拼音首字母选择"]/../dl/dd/a')
        for a in a_list:
            id_first = a.xpath("./@href")
            if id_first:
                id_second = id_first[0]
                id_third = re.findall(r'http://(.*).ganji.com/', id_second)
                if id_third:
                    id_forth = id_third[0]
                    city = a.xpath("./text()")[0]
                    city_id_dict[city] = id_forth
        city_id_dict = json.dumps(city_id_dict)
        return city_id_dict
    def area_to_street(self, district_id):
        data = {
            'district_id': district_id,
            'with_all_option': 1,
            '__hash__': 'JPv7/73SVIZDYWom8alWZxPytWrUPulqDlcEyc6BtHblRBu+hCLHQfY+3l7Ek3S4'
        }

        response = requests.post("http://www.ganji.com/ajax.php?_pdt=fang&module=streetOptions",
                                 data=data).content.decode()
        return response

    def unicode(self, street):
        ust = street.encode('unicode_escape').decode()
        return ust
    def img(self):
        img_list = [[], []]
        files_name = [r'C:\Users\Admin\Pictures\Saved Pictures\text.jpg', r'C:\Users\Admin\Pictures\Saved Pictures\text2.jpg']
        for img in files_name:
            files = {'attachment_file': ('timg.jpg', open(img, 'rb'), 'image/jpeg')}
            res = requests.post('http://image.ganji.com/upload.php', files=files)
            res = res.content.decode()
            print(res)
            r_d = json.loads(res)
            print(r_d)
            image = {"image": r_d["info"][0]["url"], "thumb_image": r_d["info"][0]["thumbUrl"],
                     "width": r_d["info"][0]["image_info"][0], "height": r_d["info"][0]["image_info"][1], "is_new": 'true'}
            img_list[0].append(image)
        self.image = str(img_list).replace("'true'", 'true').replace(" ", '').replace("'", '"')
        print(self.image)
    def put(self):
        cookie = 'statistics_clientid=me; ganji_uuid=7073847906243396007082; ganji_xuuid=d9713ce9-2419-4573-8ba5-829fac55f083.1535503838562; xxzl_deviceid=qdVlLyty3ZwZJyYs%2F86tIiCgPYNU0%2Fl64rv%2FiE9tnup5QCz3fxXq2WDv0JJDoLbd; lg=1; __utmganji_v20110909=0xfcf83bd0acc317b69b0e45f624682b1; 58tj_uuid=7311e31f-cdeb-4053-af30-4bdb29f54d45; wmda_uuid=9c712060aa465ef321535bc6c8580458; wmda_new_uuid=1; als=0; wmda_visited_projects=%3B3603688536834%3B3381039819650; xxzl_smartid=883341e74e0937b3afe63690a649b64b; NTKF_T2D_CLIENTID=guest463E7671-D2E6-EF71-A21D-8332579554DE; __utmc=32156897; username_login_n=15629185662; GanjiLoginType=0; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A31189300093%7D; nTalk_CACHE_DATA={uid:kf_10111_ISME9754_793207811}; _wap__utmganji_wap_caInfo_V2=%7B%22ca_name%22%3A%22mobile_fang5_fabu_youce%22%2C%22ca_source%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%7D; _wap__utmganji_wap_newCaInfo_V2=%7B%22ca_n%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_i%22%3A%22-%22%7D; STA_DS=0; use_https=1; ershoufangABTest=A; ganji_fang_fzp_pc=1; Hm_lvt_8dba7bd668299d5dabbd8190f14e4d34=1535964968; Hm_lpvt_8dba7bd668299d5dabbd8190f14e4d34=1535964968; vehicle_list_view_type=1; citydomain=sh; webimFangTips=793207811; gj_footprint=%5B%5B%22%5Cu5199%5Cu5b57%5Cu697c%5Cu51fa%5Cu79df%22%2C%22http%3A%5C%2F%5C%2Fsh.ganji.com%5C%2Ffang8%5C%2F%22%5D%2C%5B%22%5Cu79df%5Cu623f%22%2C%22http%3A%5C%2F%5C%2Fsh.ganji.com%5C%2Ffang1%5C%2F%22%5D%2C%5B%22%5Cu4e8c%5Cu624b%5Cu623f%5Cu51fa%5Cu552e%22%2C%22http%3A%5C%2F%5C%2Fsh.ganji.com%5C%2Ffang5%5C%2F%22%5D%5D; __utma=32156897.831268047.1535503842.1536020745.1536039398.15; __utmz=32156897.1536039398.15.11.utmcsr=ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/user/logout.php; GANJISESSID=0epm0sosbedphrk53unafcjmah; sscode=XdQ%2FVfnqfOnCepj7XdG29mdJ; GanjiUserName=yumin1351724; GanjiUserInfo=%7B%22user_id%22%3A793207811%2C%22email%22%3A%22%22%2C%22username%22%3A%22yumin1351724%22%2C%22user_name%22%3A%22yumin1351724%22%2C%22nickname%22%3A%22%22%7D; bizs=%5B%5D; supercookie=AmxmZwN3BQRkWTH2AzEwZGqvMzWzLwD5LwZ3MGHmLzVjZwN3AJAvZzLmMJL0AQWvMQt%3D; __pva__=%5B%5B%221536039928%22%2C%22100_7_5_27860171%22%5D%5D; last_name=yumin1351724; new_uv=4; utm_source=; spm=; new_session=0; init_refer=http%253A%252F%252Fwww.ganji.com%252Fpub%252Fpub.php%253Fact%253Dpub%2526method%253Dload%2526cid%253D7%2526mcid%253D21%2526domain%253Dsh%2526domain%253Dsh; __utmt=1; ganji_login_act=1536040013166; __utmb=32156897.19.10.1536039398; xzfzqtoken=lxirp1GFx8m5Bs%2BVT%2BHMnisVM%2FxK7q7bbNESTrgvMlJlQ6KHvUQvKq5MvWARiga4in35brBb%2F%2FeSODvMgkQULA%3D%3D'

        headers = {
            'Cookie':cookie
        }
        url = "http://www.ganji.com/pub/pub.php?cid=7&mcid=26&act=pub&method=submit"

        data = {
            "deal_type":'1',
            "house_type":'4',
            "store_stat":'3',
            "width":'45',
            "height": '67',
            "depth": '45',
            "frontage":'1',
            "rent_start_period":'12',
            "rent_free_period":'12',
            "pay_fu":'3',
            "pay_ya": '1',
            "xiaoqu": '公捷苑',
            "xiaoqu_pinyin": "",
            "district_id": "205",
            "street_id": "-1",
            "xiaoqu_address": "谷阳北路",
            # "latlng": "b121.239127,31.032847",
            "rent_mode": '1',
            "huxing_shi": "1",
            "huxing_ting": "2",
            "huxing_wei": "3",
            "area": "100",
            "ceng": "5",
            "ceng_total": "6",
            "elevator": "1",
            "chaoxiang": "1",
            "zhuangxiu": "5",
            "bid_structure": "11",
            "fang_xing": "1",
            "peizhi[]": ['dianshiji', 'bingxiang'],
            "price": "3000",
            "pay_type_int": '1',
            "title": "租房上赶集网",
            "description": "交通便利，近地铁，上班的不二选择！！！",
            "person": "高霸霸",
            "phone": "15629185662",
            "agent": "1",
            "images": self.image,
        }
        res = requests.post(url, headers=headers, data=data).content.decode()
        print(res)
        res_1 = re.findall('''displayError\("(.*?)"\)''', res, re.S)
        if not res_1:
            res_2 = re.findall('''(恭喜您，发布成功啦！)''', res, re.S)
            print(res_2[0])
            return res_2[0]

        else:
            print(res_1)
            return res_1[0]



if __name__ == '__main__':
    ganji = Ganji_Cs()
    ganji.img()
    ganji.put()