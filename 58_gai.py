import requests
import base64
from selenium import webdriver
import json
import re
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, and_
from mysql_connect import CityUrl_ID


class Wuba_fabu(object):

    def newSession(self):
        self.engine = create_engine('mysql+pymysql://weiyuan:weiyuan987@120.55.54.158:3306/url_db?charset=utf8')
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def searchByCity(self, item):
        try:
            if item['area']:
                self.city_id = self.session.query(CityUrl_ID).filter(and_(CityUrl_ID.city == item['localArea'], CityUrl_ID.area == item['localDiduan']))[0].city_id_58
                self.area_id = self.session.query(CityUrl_ID).filter(and_(CityUrl_ID.city == item['localArea'], CityUrl_ID.area == item['localDiduan']))[0].area_id_58
        except Exception:
            self.session.close()
            self.engine.dispose()
            return 0
        self.session.close()
        self.engine.dispose()

    def img_post(self, file_name):
        with open(file_name, 'rb') as f:
            ls = base64.b64encode(f.read()).decode()
        s = json.dumps({"Pic-Size": "0*0", "Pic-Encoding": "base64", "Pic-Path": "/dwater/fang/big/", "Pic-Data": ls})
        self.img_url = "/dwater/fang/big/" + requests.post('http://upload.58cdn.com.cn/json', data=s).content.decode()
        if self.img_url:
            print(self.img_url)
            print('图片上传成功')
        else:
            print("不稳定，转用自动化测试工具上传")
            self.selenium_img(file_name)

    def selenium_img(self, file_name):
        d = webdriver.Chrome()
        d.get('https://passport.58.com/login?path=https%3A%2F%2Fmy.58.com%2Fpro%2Finfoall%2F')
        e = d.find_element_by_xpath('//*[@id="pwdLogin"]/i')
        if e:
            e.click()
        d.find_element_by_xpath('//*[@id="usernameUser"]').send_keys('15839900552')
        d.find_element_by_xpath('//*[@id="passwordUserText"]').click()
        d.find_element_by_xpath('//*[@id="passwordUser"]').send_keys('cheng123')
        d.find_element_by_xpath('//*[@id="btnSubmitUser"]').click()
        d.get('http://post.58.com/fang/2/8/s5?PGTID=0d000000-0000-0964-4e55-da6e0f8d6801&ClickID=1')
        d.find_element_by_xpath('//*[@id="imgUpload"]/div/input').send_keys(file_name)
        t = d.find_element_by_xpath('//*[@id="flashflashContent"]/ul/li[2]/img').get_attribute('src')
        d.quit()
        return t

    def put(self, item):
        headers = {
            'Cookie': item['cookie']
        }
        data = {
            "HireType": item['HireType'],
            "Title": item['Title'],
            "Content": item['Content'],
            "xiaoquname": item['xiaoquname'],
            "localArea": self.city_id,
            "localDiduan": self.area_id,
            "dizhi": item['dizhi'],
            "area": item['area'],
            "huxingshi": item['huxingshi'],
            "huxingting": item['huxingting'],
            "huxingwei": item['huxingting'],
            "MinPrice": item['MinPrice'],
            "Floor": item['Floor'],
            "zonglouceng": item['zonglouceng'],
            "fittype": item['fittype'],
            "Toward": item['Toward'],
            "chewei": item['chewei'],
            "dianti": item['dianti'],
            "louhao": item['louhao'],
            'danyuanhao': item['danyuanhao'],
            'menpaihao': item['menpaihao'],
            "HouseAllocation": item['HouseAllocation'],
            "Pic": self.img_url,
            "HouseUserType": "683039", #经纪人
            "Phone": item['Phone'],
            "goblianxiren": item['goblianxiren'],
        }
        print(data)
        url = 'http://post.58.com/fang/{}/8/s5/submit'.format(self.city_id)
        res = requests.post(url, headers=headers, data=data).content.decode()
        print(res)
        msg_list = re.findall('''"msg":"(.*?)","rs":"(.*?)"''', res)[0]
        if msg_list[1] == 'failed':
            print(msg_list[0])
        else:
            print('发布成功')



    def run(self, item):
        self.newSession()
        self.img_post(item['Pic'])
        self.searchByCity(item)
        self.put(item)


if __name__ == '__main__':

    item = {
        "HireType": 2,
        "Title": '机不可失，失不再来！！！！',
        "Content": '近九号地铁，交通便利，附近有大超市，购物方便！',
        "xiaoquname": '公捷苑',
        "localArea": '上海',
        "localDiduan": '松江',
        "dizhi": '松江新城',
        "area": 100,
        "huxingshi": 1,
        "huxingting": 1,
        "huxingwei": 1,
        "MinPrice": 5000,
        "Floor": 5,
        "zonglouceng": 6,
        "fittype": 2,
        "Toward": 2,
        "chewei": 1,
        "dianti": 1,
        "louhao": 2,
        'danyuanhao': 31,
        'menpaihao': 502,
        "HouseAllocation": '6|15',
        "Pic": r'C:\Users\程文杰\Desktop\timg.jpg',
        "HouseUserType": "683039",
        "Phone": '15839900552',
        "goblianxiren": '隔壁老王',
        'cookie': '''id58=c5/njVt/qyFev1xoG/rVAg==; 58tj_uuid=569c6d0e-4b39-4903-add1-2a43e72d7557; als=0; xxzl_deviceid=xZ9mPseAI7Mn8ZosNsl4kA6A%2Fi7x3CVyHlj4%2F07p8bjqxLmR1mXHuRm2IzOIS269; wmda_uuid=38ffe19a4e4fb32241f50a962d22e62a; wmda_new_uuid=1; xxzl_smartid=8a7ad5e477366a1ae6435d8c0643059b; __utma=253535702.788575898.1535348043.1535348043.1535348043.1; __utmc=253535702; __utmz=253535702.1535348043.1.1.utmcsr=vip.58.com|utmccn=(referral)|utmcmd=referral|utmcct=/vcenter/qiyeziliao/; defraudName=defraud; duibiId=; wmda_visited_projects=%3B1732038237441%3B3381039819650%3B2286118353409%3B2385390625025%3B4200524323842; vip=v%3D1%26vipuserpline%3D0%26masteruserid%3D46952359857687%26vipkey%3D8ef46d62c0aa3b2b8217c38540600dca%26vipusertype%3D11; ppStore_fingerprint=F763D7BB7A0A4A2E8781DEC907BA809B56139B05CC891245%EF%BC%BF1535531906070; PPU="UID=46952359857687&UN=wuba3q1970&TT=a650f9d0ef411664d059e8ad1689ec4a&PBODY=IvVRbqsVdXMLypyIMGF_m_-fZuhlWcPVKPy_n0iV2d6e1k4xqGxR_N0bDLQLOVQL3YcPc2BMfz4MezpyPCa4VIVLACnnXQB4oRtLFnN-ye9Nuikfy-kPKwyZ4HovEMbLeXiZotCDdWcRc9MUrLG7jhU7jseVQocdvtTb4mQ_888&VER=1"; 58cooper="userid=46952359857687&username=wuba3q1970&cooperkey=7321fbc8b8e90ce028e15eda670f09b5"; city=sh; 58home=sh; new_uv=17; utm_source=; spm=; init_refer=http%253A%252F%252Fsh.58.com%252F%253FPGTID%253D0d000000-0000-04e1-54b1-926fbcdff20a%2526ClickID%253D1; www58com="AutoLogin=false&UserID=46952359857687&UserName=wuba3q1970&CityID=0&Email=&AllMsgTotal=1&CommentReadTotal=0&CommentUnReadTotal=0&MsgReadTotal=0&MsgUnReadTotal=0&RequireFriendReadTotal=0&RequireFriendUnReadTotal=0&SystemReadTotal=0&SystemUnReadTotal=1&UserCredit=0&UserScore=0&PurviewID=&IsAgency=false&Agencys=null&SiteKey=1FC200CCC2CA2C7E970B994D29FFDDF5F736534DFE645C14D&Phone=&WltUrl=&UserLoginVer=2A31A22D97063405900A4D565FBD40D76&LT=1535535262019"; new_session=0'''

    }
    wuba = Wuba_fabu()
    wuba.run(item)
