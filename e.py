import requests
import base64
from selenium import webdriver
import time
import re
from lxml import etree
import json


class P58_Cs:
    def __init__(self):
        self.n = 5

    def city_id(self):
        response = requests.get(
            "http://www.58.com/changecity.html").content.decode()
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

    def img_post(self, name='8f1fda1af6f24b0821bc867aaf2cad9c.jpg'):
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
        d.find_element_by_xpath('//*[@id="usernameUser"]').click()
        d.find_element_by_xpath('//*[@id="usernameUser"]').send_keys('13260662303')
        d.find_element_by_xpath('//*[@id="passwordUserText"]').click()
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="passwordUserText"]').send_keys('yumin135172')
        d.find_element_by_xpath('//*[@id="btnSubmitUser"]').click()
        time.sleep(5)
        d.get('http://post.58.com/fang/2/12/s5')
        time.sleep(5)
        d.find_element_by_xpath('//*[@id="imgUpload"]/div/input').send_keys('C:\\Users\Admin\Pictures\Saved Pictures\\8f1fda1af6f24b0821bc867aaf2cad9c.jpg')
        time.sleep(2)
        t = d.find_element_by_xpath('//*[@id="flashflashContent"]/ul/li[2]/img').get_attribute('src')
        # 上传图片的@src
        time.sleep(5)
        d.quit()
        return t

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

    def put(self, item):
        cookie = 'commontopbar_new_city_info=2%7C%E4%B8%8A%E6%B5%B7%7Csh; commontopbar_ipcity=sh%7C%E4%B8%8A%E6%B5%B7%7C0; id58=QkGAmVtyJ2knaL9XFx/KeQ==; 58tj_uuid=274076e8-2c01-406b-9c9f-774538f53b12; wmda_uuid=73dee54c8766ee2f16a35d9fb701daf3; wmda_new_uuid=1; als=0; 58home=sh; city=sh; xxzl_deviceid=DIbI0nGzeAx0Zrl6N6cRoyfOJJ83uPOFCnULmiR0uO6yWsOvseTeQ%2BsrwiDdjgED; post_uuid=f26d3010-927a-4bd5-8995-56123511f42b; xxzl_smartid=7a5ea67ca39f1ef8d873d2414d2ebdbf; gr_user_id=d2c3ef44-f6fa-4bea-9119-e67ce7a68196; wmda_visited_projects=%3B2385390625025%3B1732038237441%3B3381039819650%3B2286118353409; bangtoptipclose=1; new_uv=21; utm_source=; spm=; init_refer=; new_session=0; popup_logintab_new=1; popup_loginstab_second=0; ppStore_fingerprint=61C8D91031269BEA8EF713DB4E6DC0508AFAC05ED2D93160%EF%BC%BF1535590746381; PPU="UID=51885951006991&UN=yukang_2303&TT=44b03ff0d418ed6723371c7cb00293b0&PBODY=An5Qr-_3NOoAQxPb-CRyWrv7fFGk0oaMWbLos5uAYWyFod_nXTN5-lKdLhDQjwC7C4L5lo4haoMjI7VsdkPsvFEnjRwZOLaTUKYXyZycguLNlWS8ddetXens3NJbtgKN2NTs2AxST-1IJ8PhAh_0J1MgFnGRYCbO1Qd3LlTfW6s&VER=1"; 58cooper="userid=51885951006991&username=yukang_2303&cooperkey=bb07d75632c9018c4065319972f47307"; www58com="AutoLogin=false&UserID=51885951006991&UserName=yukang_2303&CityID=0&Email=&AllMsgTotal=0&CommentReadTotal=0&CommentUnReadTotal=0&MsgReadTotal=0&MsgUnReadTotal=0&RequireFriendReadTotal=0&RequireFriendUnReadTotal=0&SystemReadTotal=0&SystemUnReadTotal=0&UserCredit=0&UserScore=0&PurviewID=&IsAgency=false&Agencys=null&SiteKey=4E2D7FDC8FC5457587EBA52689C6162FFEF9FB500777E41EA&Phone=&WltUrl=&UserLoginVer=3FFB2E44A074375AA1DE42EAF697DB64C&LT=1535590742796"; wmda_session_id_2385390625025=1535590803159-6a45d6d6-b58b-46bf; __utma=253535702.2095062439.1535093443.1535520700.1535590806.5; __utmc=253535702; __utmz=253535702.1535590806.5.5.utmcsr=sh.58.com|utmccn=(referral)|utmcmd=referral|utmcct=/house.shtml; __utmb=253535702.1.10.1535590806'
        headers = {
            'Host': 'post.58.com',
            'Origin': 'http://post.58.com',
            'Referer': 'http://post.58.com/fang/2/12/s5?PGTID=0d30000c-0000-2de2-e7c0-a5f3a1397748&ClickID=1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie
        }
        city_id = self.search(item["城市"])
        ardi = self.ld(city_id, item["区域"], item["地段"])
        print(ardi)
        data = {
            "type": "0",
            "isBiz": "1",
            # "xiaoqu": "330561",
            "xiaoquname": item["位置"]["xiaoquname"],
            "localArea": ardi[0],
            "localDiduan": ardi[1],
            "dizhi": item["位置"]["dizhi"],
            "huxingshi": item["房屋户型"]["室"],
            "huxingting": item["房屋户型"]["厅"],
            "huxingwei": item["房屋户型"]["卫"],
            "area": item["房屋户型"]["面积"],
            "MinPrice": item["总价"],
            "Title": item["标题"],
            "ObjectType": "3",
            "fittype": "2",

            "Toward": "",
            "chanquannianxian": "70",
            "chanquan": "2",
            "jianzhuniandai": "1989",
            "Floor": "19",
            "zonglouceng": "26",
            "Content": item["详细介绍"],
            # "Pic": "/p1/big/n_v2b247c050522247f4a8ba059d00805734.jpg",
            # 上传图片的@src
            "Phone": item["联系电话"],
            "yzm": "",
            "goblianxiren": item["联系人"],
            # "name": item["联系人"],
            "globalQQOpenId": "",
            "postparam_openidtype": " ",
            'cube_post_jsonkey': '{"jzJson":null,"znJson":null,"zdJson":{"infotop_time_price_string":"12,43.04;24,50.64;72,148.88,151.92;168,336.76,354.48;360,698.83,759.60;720,1367.28,1519.20","infotop_hourconsume":"2.11","infotop_cateId":"12","infotop_localId":"6184","infotop_categoryId":"0","infotop_cityId":"2","infotop_userId":"30825196901895","infotop_source":"1501","infotop_hotCoafficient":"1.5","selectTime":"","allConsume":"0.00","couponPassword":"","couponAmount":"0.00","selectEventId":"","topType":"0","selectAutoTopVal":"1","canMakeInfoTop":"false"},"jzFee":"0","znFee":"0","zdFee":"0.00","jzCop":"0","znCop":"0","zdCop":"0.00","sourceId":"1501","productId":"100006","secondCateId":"12","dispSecondCateId":"12","cityId":"2","dispCityId":"2"}',
            'jz_refresh_post_key': '0',
            'userid': '51885951006991',
            'postparam_userid': '51885951006991',
            'hidPostParam': '0',
            'captcha_type': '',
            'captcha_input': '',
            'selectBiz': '0',
            'GTID': '0d50000c-0000-2edf-b891-ecbe43353209',
            'commercial': '{"cateid":"12","common":{"commonType":"10","pagetype":"1","platform":"-1","source":"101010110"},"local":"2","selected":false}'
        }
        url = 'http://post.58.com/fang/{}/12/s5/submit'.format(
            city_id)
        res = requests.post(url, headers=headers, data=data)

        print(res.content.decode())


# *位置：迎江 请选择地段 具体地址
# *房屋户型：1室2厅3卫共4㎡
# *总价：5万
# *标题：迎江小区 1室2厅3卫 4平米
# *详细介绍：详细介绍详细介绍详细介绍详细介绍详细介绍详细介绍详细介绍详细介绍详细介绍详细介绍​
# *联系电话：18356632280
# *联系人：联系人

# //script[@type="text/javascript"]

item = {}
item["城市"] = "安庆"
item["区域"] = "大观区"
item["地段"] = ""
item["位置"] = {
    "xiaoqu": "330561",
    "xiaoquname": "蛤仙道观",
    "localArea": "1399",
    "localDiduan": "6184",
    "dizhi": "苟利国家生死以路", }
item["房屋户型"] = {"室": 1, "厅": 2, "卫": 3, "面积": 4}
item["总价"] = 5
item["标题"] = "蛤仙道观长寿观史养生房"
item["详细介绍"] = "苟利国家生死以，岂因祸福避趋之"
item["联系电话"] = "13260662303"
item["联系人"] = "鱼显示"

P58_Cs().city_id()
s = P58_Cs().put(item)
print(s)
