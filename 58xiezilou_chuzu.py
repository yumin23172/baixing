import json
import re

import requests
import base64

from lxml import etree
from selenium import webdriver
import time
#58写字楼出租

class P58_Cs:
    def __init__(self):
        self.n = 5
    def city_id(self):
        response = requests.get(
            "http://www.58.com/changecity.html?catepath=post5&fullpath=1,11,&PGTID=0d50000b-0000-233f-e12b-7751f8355beb&ClickID=3").content.decode()
        res = etree.HTML(response)
        if response:
            json_first = res.xpath('//script[contains(text(),"provinceList")]/text()')
            if json_first:
                json_second = json_first[0]
                json_third_first = re.findall(r'var independentCityList = (\{[\s\S]*\})\n.*var cityList', json_second)[
                    0]
                json_third_second = re.findall(r'var cityList = (\{[\s\S]*\})', json_second)[0]
                json_fourth = {}
                json_fourth.update(json.loads(json_third_first))
                json_third_second_first = json.loads(json_third_second)
                for value in json_third_second_first.values():
                    json_fourth.update(value)
                json_fifth = json.dumps(json_fourth)
                with open("city_abbreviate_id.json", "w") as f:
                    f.write(json_fifth)
            else:
                print('页面逻辑可能已被修改')
        else:
            print("可能已经遭到反爬")

    def search(self, city):
        with open("city_abbreviate_id.json", "r")as f:
            json_str = f.read()
        dict_dict = json.loads(json_str)
        try:
            cit_id = dict_dict[city]
            id_c = re.findall(r"\|(\d*)", cit_id)[0]
            return id_c
        except:
            return "只支持查询市一级行政单位，不支持查询区县一级行政单位"

    def ld(self, city_id, area, diduan=""):
        response = requests.get(
            'http://post.58.com/fang/{}/11/s5'.format(city_id)).content.decode()
        #                              城市
        res = etree.HTML(response)
        datasrc_once = res.xpath('//*[@type="text/javascript"][1]/text()[1]')[0]
        datasrc_second = re.findall(r'var datasrc=(\{.*\})', datasrc_once)[0]
        datasrc_third = json.loads(datasrc_second)
        for s in datasrc_third["localArea"]["values"]:
            if re.findall(area, s['text']) or re.findall(s['text'], area):
                localArea = s['val']
                print(localArea)
                if diduan:
                    if 'children' in s.keys():
                        if s['children'][0]['values']:
                            for v in s['children'][0]['values']:
                                if re.findall(diduan, v['text']) or re.findall(v['text'], diduan):
                                    localDiduan = v['val']
                                    return localArea, localDiduan
                        else:
                            return localArea, ""
                    else:
                        return localArea, ""
                else:
                    return localArea, ""
    def img_post(self, name='257ac895d143ad4b997cee408e025aafa50f06ad.jpg'):
        # 使用post接口上传图片，不稳定
        import base64
        import requests
        import json

        with open(name, 'rb') as f:
            ls = base64.b64encode(f.read()).decode()

        s = json.dumps({"Pic-Size": "0*0", "Pic-Encoding": "base64", "Pic-Path": "/p1/big/", "Pic-Data": ls})
        response = requests.post('http://upload.58cdn.com.cn/json', data=s).content.decode()
        if response:
            return response
        else:
            print("不稳定，转用自动化测试工具上传")
            self.img(name)

    def img(self, name):
        d = webdriver.Chrome('')
        time.sleep(5)
        d.get('https://passport.58.com/login')
        e = d.find_element_by_xpath('//*[@id="pwdLogin"]/i')
        if e:
            e.click()
        d.find_element_by_xpath('//*[@id="usernameUser"]').send_keys('15629185662')
        d.find_element_by_xpath('//*[@id="passwordUserText"]').click()
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="passwordUser"]').send_keys('yumin135172')
        d.find_element_by_xpath('//*[@id="btnSubmitUser"]').click()
        time.sleep(5)
        d.get('http://post.58.com/fang/2/12/s5')
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="imgUpload"]/div/input').send_keys(name)
        time.sleep(2)
        t = d.find_element_by_xpath('//*[@id="flashflashContent"]/ul/li[2]/img').get_attribute('src')
        # 上传图片的@src
        time.sleep(5)
        d.quit()
        return t

    def put(self, item):
        cookie = 'commontopbar_new_city_info=2%7C%E4%B8%8A%E6%B5%B7%7Csh; commontopbar_ipcity=sh%7C%E4%B8%8A%E6%B5%B7%7C0; id58=QkGAmVtyJ2knaL9XFx/KeQ==; 58tj_uuid=274076e8-2c01-406b-9c9f-774538f53b12; wmda_uuid=73dee54c8766ee2f16a35d9fb701daf3; wmda_new_uuid=1; als=0; 58home=sh; city=sh; xxzl_deviceid=DIbI0nGzeAx0Zrl6N6cRoyfOJJ83uPOFCnULmiR0uO6yWsOvseTeQ%2BsrwiDdjgED; post_uuid=f26d3010-927a-4bd5-8995-56123511f42b; xxzl_smartid=7a5ea67ca39f1ef8d873d2414d2ebdbf; gr_user_id=d2c3ef44-f6fa-4bea-9119-e67ce7a68196; wmda_visited_projects=%3B2385390625025%3B1732038237441%3B3381039819650%3B2286118353409; bangtoptipclose=1; __utmc=253535702; 58cooper="userid=57764918451986&username=etre3i8u8&cooperkey=61bc13694cd6215823f47b3ad7bd90a9"; __utma=253535702.2095062439.1535093443.1535590806.1535708322.6; __utmz=253535702.1535708322.6.6.utmcsr=sh.58.com|utmccn=(referral)|utmcmd=referral|utmcct=/house.shtml; new_uv=30; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253DlLjlmkAcCUOU418uM479fMSK6N-H8gk8VxVXRpFrcDy%2526wd%253D%2526eqid%253Daec664e200009374000000045b8c9f41; new_session=0; popup_logintab_new=1; ppStore_fingerprint=61C8D91031269BEA8EF713DB4E6DC0508AFAC05ED2D93160%EF%BC%BF1535942491978; PPU="UID=57764918451986&UN=etre3i8u8&TT=5d477878d1aec90680df86d010e9cea4&PBODY=TFS4VBdWqiUs38vKfGikzXbXIiJ3Qh1WVbQhGkZzsCFmTxrfvG-jSpkGShKQovEHil6jckx0USVYwuEWxiBIPoIpE8Sht5B6puwF3n71Lk06QIg5XJ9CNOwczbHrI4cfL6F0482S8NgdrxoZ7rn1P5UtGAmEIqSTDH7Tmn_ZKKk&VER=1"; www58com="AutoLogin=false&UserID=57764918451986&UserName=etre3i8u8&CityID=0&Email=&AllMsgTotal=0&CommentReadTotal=0&CommentUnReadTotal=0&MsgReadTotal=0&MsgUnReadTotal=0&RequireFriendReadTotal=0&RequireFriendUnReadTotal=0&SystemReadTotal=0&SystemUnReadTotal=0&UserCredit=0&UserScore=0&PurviewID=&IsAgency=false&Agencys=null&SiteKey=08CDD29DF3C9758879A92E8BEAD81E8F9A5AB570C3BD3E7FC&Phone=&WltUrl=&UserLoginVer=4E2D7FDC8FC545758C7C7406FE81BAB9F&LT=1535942489863"'
        headers = {
            'Host': 'post.58.com',
            'Origin': 'http://post.58.com',
            'Referer': 'http://post.58.com/fang/2/12/s5?PGTID=0d000000-0000-042d-5c1c-1490e6193074&ClickID=1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie
        }
        city_id = self.search(item["城市"])
        ardi = self.ld(city_id, item["区域"], item["地段"])
        print(ardi)
        data = {
            "type": "0",
            "isBiz": "1",
            "ObjectType":"1",
            "zhuce":"1",
            "OfficesLevel":"1",
            "loupan": item["楼盘名称"],
            "localArea": ardi[0],
            "localshangquan": ardi[1],
            "dizhi": item["所在区域"]["dizhi"],
            "FitType":"3",
            "partition":"1",
            "loucengfenqu":"1",
            "Floor":  item["楼层"]["Floor"],
            "zonglouceng":  item["楼层"]["zonglouceng"],
            "jianzumianji": item["建筑面积"],
            "shiyonglv": item["建筑面积"],
            "area": item["面积"],
            "MinPrice": item["价格"],
            "fukuanyue": item["付款日期"],
            "peitao":"1",
            "zujin": item["租金"]["zujin"],
            "danwei":"3",
            "includePropertyFee":"1",
            "qizuqi":item["起租期"],
            "mianzuqi": item["免租期"],
            "yajinyue": item["押金日期"],
            "Title": item["标题"],
            "Content": item["补充描述"],
            # "Pic": "/p1/big/n_v2b247c050522247f4a8ba059d00805734.jpg",
            # 上传图片的@src
            "goblianxiren": item["联系人"],
            "Phone": item["联系电话"],
            "globalQQOpenId": "",
            'userid': '57764918451986',
            'postparam_userid': '57764918451986',
        }
        url = 'http://post.58.com/fang/{}/13/s5/submit'.format(city_id)
        res = requests.post(url, headers=headers, data=data)

        print(res.content.decode())




item = {}
item["城市"] = "武汉"
item["区域"] = ""
item["地段"] = ""
item["楼盘名称"]="汇佳大厦"
item["所在区域"] = {
              "localArea": "1399",
              "localDiduan": "6184",
              "dizhi": "嵩山路", }
item["楼层"] = {"loucengfenqu": 1, "Floor": 5, "zonglouceng": 13,}
item["建筑面积"] = {"jianzumianji": 120, "shiyonglv": 50,}
item["面积"]="120"
item["租金"] = {"zujin": 11200, "danwei": 5, "includePropertyFee": 13,}
item["起租期"] = "1"
item["免租期"] = "9"
item["标题"] = "汇佳大厦200平方写字楼低价出售"
item["补充描述"] = "配套齐全汇佳大厦200平方写字楼低价出售"
item["联系人"] = "张先生"
item["联系电话"] = "15629185662"
item["价格"]="1200"
item["押金日期"]="1"
item["付款日期"]="3"


P58_Cs().put(item)
