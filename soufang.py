#搜房网出租出售发布
import sys
import base64
import re
import requests
import json
sys.path.append(".")
from util.mysqlutil import CityUrl_ID
from util.httputil import RequestsAgent
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker


class SoufangRelease:
    def __init__(self):
        self.http = RequestsAgent()
        self.ritem = {
            'error': '', # 预发布失败原因
            'release': '', # 预发布成功 1 预发布失败 2
            'url': '' # 预发布成功后 url
        }

    # 获取 城市 区域 id
    def __searchByCity(self, city, area):
        try:
            if city and area:
                city_id = self.session.query(CityUrl_ID).filter(and_(CityUrl_ID.city == city, CityUrl_ID.area == area))[0].city_id_soufang
                area_id = self.session.query(CityUrl_ID).filter(and_(CityUrl_ID.city == city, CityUrl_ID.area == area))[0].area_id_soufang
        except Exception:
            self.session.close()
            self.engine.dispose()
            return 0
        self.session.close()
        self.engine.dispose()
        return city_id,area_id

    def __newSession(self):
        self.engine = create_engine('mysql+pymysql://weiyuan:weiyuan987@120.55.54.158:3306/url_db?charset=utf8')
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    # 上传室内图片
    def img(self):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; agent_sofang_session=e2f4fc14b3a003bb838f82e5b9f957e399bb8dbf; www_sofang_session=eyJpdiI6IndGZlhjOXlwU010eVJ3WXM4dGdZaFE9PSIsInZhbHVlIjoiZ1wvdjZoUExYbk1Dd1h5d1c5Y3BLaVhUemlJODhGVzRVUWR5eFNSM1kydFpLWnNvOW1HYTRuQkxVVGo5UXRrY3F2RFZ1b1JzTFJRZndwemlzN1JsVG93PT0iLCJtYWMiOiJlNWU3ODJiNThkZWQ5OTA4ZDIxNDI1ZjkzMjJlMDUyNzNhZTU4YzM1N2Q1YmViOWUyYTg4NDVlMmM3NzE3M2FmIn0%3D; cityid=eyJpdiI6IlZVaHdEUXFJdlwveWh4enpjVEx1cytnPT0iLCJ2YWx1ZSI6InY2aDZXZ3Z6S2Jxckdmd0pQUCs5dnc9PSIsIm1hYyI6ImU2M2JiNGM3MzBiZjlkMGU0MGE4ZWMzM2UwNGVhYjJmYmEwNzliNmRlNDE4ODA5YWZiMjEwYjBmMjMzMjFjZDgifQ%3D%3D; city=eyJpdiI6Inc2XC9scGxTdkhxMndjZG9JWVJjSDl3PT0iLCJ2YWx1ZSI6IndoK0E2bk9GbVwvNnFmeEExN002a2JzY1c4bWVkUyt2UkpDdSttV29wbUNscDNxdldqbnFrRWdFSUhwNVhLUnArRUZ3NG1EWnNUR0UwUHJjK1dsUWJQQitLY2QyaStnSU4yXC84T1JiNUdwVmVjVHoxcjRpWEswcTIxbGlHd0xYSDEzVFI5XC84YTJaVm1raDd5Vjh2VnBVZ2U1RmtHZzZ1cHVZYkZCbTNOb2xSUDlIMzNTcm9PeStTZE1FMURkS0Y2aDBBSXZHRjNueDRBZ0s3d1J2UVo0b2I5TmNQS01kM29MNVJ3OExWVDBXbDRVRjZsRnNlWlwvZ3ZlUXdNSkQwZVV5S3FGYkFERklTeVpOZVNwYm13bkcxMjFHaEFnb1pFUDFMNk85b0tlWVc0OD0iLCJtYWMiOiJlMGUwN2IyMDAxODBmNTUzZmE2Yjk2NmQ0MDcxNzIzMjkzN2VhNmUwODgwNzdkMWU3MDA0NDBmNWIxMWRhYTFkIn0%3D; citypy=eyJpdiI6InBDNWlKcVAySnlqc1NCdENSXC8xSFBRPT0iLCJ2YWx1ZSI6Imh6cWlvbkQ3TE9vSnJHdjE0ZVJcL1RBPT0iLCJtYWMiOiIxYzVkMzUwNmE5M2VjY2IzMDQ4YTViNjNlNjdjZTUwNmJkNzFjNWE2YTliMDE5YzU4MmIzNjdiZGI0MTQ3NDFlIn0%3D; XSRF-TOKEN=eyJpdiI6ImZxN2R0ckJOVzdWckVaeTlCYzhQR1E9PSIsInZhbHVlIjoiamluWnZnemNxK00wZDBLS09WTkJDVVJHd3d1RVFXa2lkS1N2V0tsYUgxNjN3K3FsQmdTeDVONzZkbmtLZTBkVnBTa1JcL1RFRHdrUU5ndlZvd2xTa1ZRPT0iLCJtYWMiOiIyODRlM2E2NmQ4MDQ5ZTgwM2FlMDlhODNhYzExNjQ4NzRhMTU4ZWQxYWI3MTg0OTU0YzE3MWUzYmI0ODU3ZTk5In0%3D'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldsale/house',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        img_list = []
        files_name = [r'C:\Users\Admin\Pictures\Saved Pictures\text1.jpg',r'C:\Users\Admin\Pictures\Saved Pictures\text.jpg']
        for img in files_name:
            files = {'attachment_file': ('timg.jpg', open(img, 'rb'), 'image/jpeg')}
            self.res = requests.post('http://agent.sofang.com/upload/addphoto?imageType=houseSale',headers=headers_1,files=files).content.decode()
            image = {"img":self.res,"note":"","type":"10"}
            img_list.append(image)
        self.image = str(img_list).replace("'",'"')
        print(self.image)
        return self.res

    # 上传标题图片
    def biaoti_img(self):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; agent_sofang_session=e2f4fc14b3a003bb838f82e5b9f957e399bb8dbf; www_sofang_session=eyJpdiI6IndGZlhjOXlwU010eVJ3WXM4dGdZaFE9PSIsInZhbHVlIjoiZ1wvdjZoUExYbk1Dd1h5d1c5Y3BLaVhUemlJODhGVzRVUWR5eFNSM1kydFpLWnNvOW1HYTRuQkxVVGo5UXRrY3F2RFZ1b1JzTFJRZndwemlzN1JsVG93PT0iLCJtYWMiOiJlNWU3ODJiNThkZWQ5OTA4ZDIxNDI1ZjkzMjJlMDUyNzNhZTU4YzM1N2Q1YmViOWUyYTg4NDVlMmM3NzE3M2FmIn0%3D; cityid=eyJpdiI6IlZVaHdEUXFJdlwveWh4enpjVEx1cytnPT0iLCJ2YWx1ZSI6InY2aDZXZ3Z6S2Jxckdmd0pQUCs5dnc9PSIsIm1hYyI6ImU2M2JiNGM3MzBiZjlkMGU0MGE4ZWMzM2UwNGVhYjJmYmEwNzliNmRlNDE4ODA5YWZiMjEwYjBmMjMzMjFjZDgifQ%3D%3D; city=eyJpdiI6Inc2XC9scGxTdkhxMndjZG9JWVJjSDl3PT0iLCJ2YWx1ZSI6IndoK0E2bk9GbVwvNnFmeEExN002a2JzY1c4bWVkUyt2UkpDdSttV29wbUNscDNxdldqbnFrRWdFSUhwNVhLUnArRUZ3NG1EWnNUR0UwUHJjK1dsUWJQQitLY2QyaStnSU4yXC84T1JiNUdwVmVjVHoxcjRpWEswcTIxbGlHd0xYSDEzVFI5XC84YTJaVm1raDd5Vjh2VnBVZ2U1RmtHZzZ1cHVZYkZCbTNOb2xSUDlIMzNTcm9PeStTZE1FMURkS0Y2aDBBSXZHRjNueDRBZ0s3d1J2UVo0b2I5TmNQS01kM29MNVJ3OExWVDBXbDRVRjZsRnNlWlwvZ3ZlUXdNSkQwZVV5S3FGYkFERklTeVpOZVNwYm13bkcxMjFHaEFnb1pFUDFMNk85b0tlWVc0OD0iLCJtYWMiOiJlMGUwN2IyMDAxODBmNTUzZmE2Yjk2NmQ0MDcxNzIzMjkzN2VhNmUwODgwNzdkMWU3MDA0NDBmNWIxMWRhYTFkIn0%3D; citypy=eyJpdiI6InBDNWlKcVAySnlqc1NCdENSXC8xSFBRPT0iLCJ2YWx1ZSI6Imh6cWlvbkQ3TE9vSnJHdjE0ZVJcL1RBPT0iLCJtYWMiOiIxYzVkMzUwNmE5M2VjY2IzMDQ4YTViNjNlNjdjZTUwNmJkNzFjNWE2YTliMDE5YzU4MmIzNjdiZGI0MTQ3NDFlIn0%3D; XSRF-TOKEN=eyJpdiI6ImZxN2R0ckJOVzdWckVaeTlCYzhQR1E9PSIsInZhbHVlIjoiamluWnZnemNxK00wZDBLS09WTkJDVVJHd3d1RVFXa2lkS1N2V0tsYUgxNjN3K3FsQmdTeDVONzZkbmtLZTBkVnBTa1JcL1RFRHdrUU5ndlZvd2xTa1ZRPT0iLCJtYWMiOiIyODRlM2E2NmQ4MDQ5ZTgwM2FlMDlhODNhYzExNjQ4NzRhMTU4ZWQxYWI3MTg0OTU0YzE3MWUzYmI0ODU3ZTk5In0%3D'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldsale/house',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        data_1 = {
                     'path':self.res
        }

        response = requests.post('http://agent.sofang.com/upload/addphoto?imageType=houseSale&title=1',headers=headers_1,data=data_1).content.decode()
        image = {"img":response,"type":"9","note":"","tag":"2"}
        img_list=[image]
        self.image1 = str(img_list).replace("'",'"')
        print(self.image1)

    def roomStr(self, item):
        self.roomStr = item["shi"] + '_' + item["ting"] + '_' + item["wei"] + '_' + item["chufang"]
        return self.roomStr

    # 出租
    def addCzInfo(self,item):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; cityid=eyJpdiI6InZhZU1acXZaakZGZkJacGpnYWxTWEE9PSIsInZhbHVlIjoiMXdPWkt4Qm80dlZYZWhNRWNlV1BkZz09IiwibWFjIjoiMGVjY2Q5ZWMwMmQ4NGUwZWE2OWY1ZDhiZmI2ZDQ0NzYwNmE2MzA1OWY0MmMzZTdiYzIyY2FkZTM2MmY5Yjc4MSJ9; city=eyJpdiI6IkRGQTl6ODVWbkg5ZmU0elwvcXpTVld3PT0iLCJ2YWx1ZSI6ImZrUXNJamZ6dGkxZzc2aFZiYlJCcXlKXC95bzJyQVwvbXo0b3ZNUDNcL2dpeE9zYVhpdDJ0bnMrN0hnUlFcLzFOM0VMTFpJMVwvcTkyejd6azlJcUY1SHZvc3czUmFsc2J2ZFhhWVBaVXNEMEVzenBsMUdxMDQzaWo2ZVhTTTFEdVBcLytUWmd6Qytha2VzaHNUbXo0TmZzanVzVEx4blVzTG1pWWFqdDF3dXJqS0I2S2Y1ZThLeDVveXFBSDdCS3JRTTFjcVNjNUh0OWp5RlJZYmh2SUlhNEMzdHp2Um93aFwvMFl5QVBwZmtTTkJ6N1wvSDVmc2V2ek1JZE52cEJLZXRscitsNTJsOVFLOFFFQ1NoOHZ1Vk9XWG1SMUdKUG5iUklPYXdxdUh4c041T3p4dGM9IiwibWFjIjoiYzNiNWJlZmNhMzVkMTk5MzM3MWZmMTliY2M2NDliNmI5ZGNkOTQwYzI5NzlhYmNjMDJiYTBhZjAxMGFmMGU3NCJ9; citypy=eyJpdiI6ImFPN3VrQVhZb1BiRzBkVHBBV21OZWc9PSIsInZhbHVlIjoiWk5ubm53N2JaeGVvQ2RMN1E4dUNMZz09IiwibWFjIjoiZGQ2YmMwODUyYzk3ZDU1ZmMwNWI2MWViODExOTA3NTA1NTU1NTM3M2NiYmQwYTJhMGU2ODRhMDNkNWFiMDg0MyJ9; agent_sofang_session=0997ce38e2bf724675a9c34c8750b8138b35948f; XSRF-TOKEN=eyJpdiI6Ijl3ZkUzZGlXdU1xRUxcL3F3ZlZ4Sit3PT0iLCJ2YWx1ZSI6IkpIXC9vb2p4WGdiQ1wvUnBYMnhac2VGUXlENmg1dDVGTmhyUWpoK2JNWTBkQUlwU0ozb01GOUxLM0hhNTZcL2JXdXAwblBubW5HMjB0MTh0emxZMlwveDNlQT09IiwibWFjIjoiMzUxYmM2NTcwMmI2Y2UxYzk0MzNlZDU0NjJmMGE2YjA0NGQ1ZDNhMGYzNzAxZDA4NzgyNjg2Zjg5NGM5Y2QyNyJ9'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldrent/house',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        data = {
            '_token': item["token"],                                #token
            'houseType1': item["houseType1"],                       #房屋类型（houseType1）
            'rentType': item["rentType"],                           #出租类型（rentType）
            'cityId': item["cityId"],                               #市(cityId)
            'cityareaId': item["cityareaId"],                       #区(cityareaId)
            'name': item["name"],                                   #小区(name)
            'communityId': item["communityId"],                     # 小区id（communityId）
            'address': item["address"],                             #地址(address)
            'fitment': item["fitment"],                             #装修状况（fitment）
            'roomStr': self.roomStr ,                               #室厅卫厨(roomStr)
            "price": item["price"],                                 #出租价格 (price)
            'priceUnit': item["priceUnit"],                         #价格单位（priceUnit）
            'paymentType': item["paymentType"],                     #付款类型（paymentType）
            "area": item["area"],                                   #面积(area)
            "currentFloor": item["currentFloor"],                   #楼层(currentFloor)
            "totalFloor": item["totalFloor"],                       #总楼层(totalFloor)
            'houseType2': item["houseType2"],                       #物业类型(houseType2)
            'faceTo': item["faceTo"],                               #房屋朝向（faceTo）
            "title": item["title"],                                 #标题(title)
            'describe': item["describe"],                           #描述(describe)
            'indoor':self.image,                                    #室内图（indoor）
            'titleimg':self.image1,                                 #标题图（titleimg）
            "linkman": item["linkman"],                             #联系人(linkman)
            "linkmobile": item["linkmobile"]                        #电话(linkmobile)
        }
        print(data)
        print("*" * 80)
        url='http://agent.sofang.com/submitrent'
        res = requests.post(url, headers=headers_1, data=data).content.decode()
        print(res)
        self.ritem['url'] = url
        result = re.findall('''"result":(.*?),"message":"(.*?)"''', res)[0]
        if result:
            if 'false' in result:
                self.ritem['error'] = result[1]
                self.ritem['release'] = 2
            else:
                self.ritem['release'] = 1
    #出租正式发布
    def chuzu_fabu(self):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; agent_sofang_session=e2f4fc14b3a003bb838f82e5b9f957e399bb8dbf; cityid=eyJpdiI6IlZVaHdEUXFJdlwveWh4enpjVEx1cytnPT0iLCJ2YWx1ZSI6InY2aDZXZ3Z6S2Jxckdmd0pQUCs5dnc9PSIsIm1hYyI6ImU2M2JiNGM3MzBiZjlkMGU0MGE4ZWMzM2UwNGVhYjJmYmEwNzliNmRlNDE4ODA5YWZiMjEwYjBmMjMzMjFjZDgifQ%3D%3D; city=eyJpdiI6Inc2XC9scGxTdkhxMndjZG9JWVJjSDl3PT0iLCJ2YWx1ZSI6IndoK0E2bk9GbVwvNnFmeEExN002a2JzY1c4bWVkUyt2UkpDdSttV29wbUNscDNxdldqbnFrRWdFSUhwNVhLUnArRUZ3NG1EWnNUR0UwUHJjK1dsUWJQQitLY2QyaStnSU4yXC84T1JiNUdwVmVjVHoxcjRpWEswcTIxbGlHd0xYSDEzVFI5XC84YTJaVm1raDd5Vjh2VnBVZ2U1RmtHZzZ1cHVZYkZCbTNOb2xSUDlIMzNTcm9PeStTZE1FMURkS0Y2aDBBSXZHRjNueDRBZ0s3d1J2UVo0b2I5TmNQS01kM29MNVJ3OExWVDBXbDRVRjZsRnNlWlwvZ3ZlUXdNSkQwZVV5S3FGYkFERklTeVpOZVNwYm13bkcxMjFHaEFnb1pFUDFMNk85b0tlWVc0OD0iLCJtYWMiOiJlMGUwN2IyMDAxODBmNTUzZmE2Yjk2NmQ0MDcxNzIzMjkzN2VhNmUwODgwNzdkMWU3MDA0NDBmNWIxMWRhYTFkIn0%3D; citypy=eyJpdiI6InBDNWlKcVAySnlqc1NCdENSXC8xSFBRPT0iLCJ2YWx1ZSI6Imh6cWlvbkQ3TE9vSnJHdjE0ZVJcL1RBPT0iLCJtYWMiOiIxYzVkMzUwNmE5M2VjY2IzMDQ4YTViNjNlNjdjZTUwNmJkNzFjNWE2YTliMDE5YzU4MmIzNjdiZGI0MTQ3NDFlIn0%3D; XSRF-TOKEN=eyJpdiI6IlB3M3JqcGxudGFta3lYb21IMnEyZnc9PSIsInZhbHVlIjoiVVhudU1mbGdlK2txbkRRN2N3aHRURjZQeVdCWVpZZXluZHpZRUF3VUdsTDBxeDVhcVNUQ1VjRWQ2VWlNcmVpOTQ3UWh3RVkraFFNbTBzUHhrY2NyXC9nPT0iLCJtYWMiOiIxZTU1NjIxZTFkMzc1N2MxNzIxN2I0Yzc1OWMyZTZhOWZkNWU0ZWQxODhhNWRkYWM3YTEzMmI2YWYzMmViNDI5In0%3D'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldrentmanage/shops/releaseed',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        data_1 = {
            'id': self.id
        }
        url = 'http://agent.sofang.com/statusrent/release?id={}'.format(self.id)
        response = requests.get(url, headers=headers_1, data=data_1).content.decode()
        print(response)
        if response == "1":
            print("正式发布成功")
        elif response == "5":
            print("您当天免费发布套数已用完！")
        else:
            print("正式发布失败")
    # 出售
    def addCsInfo(self,item):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; cityid=eyJpdiI6InZhZU1acXZaakZGZkJacGpnYWxTWEE9PSIsInZhbHVlIjoiMXdPWkt4Qm80dlZYZWhNRWNlV1BkZz09IiwibWFjIjoiMGVjY2Q5ZWMwMmQ4NGUwZWE2OWY1ZDhiZmI2ZDQ0NzYwNmE2MzA1OWY0MmMzZTdiYzIyY2FkZTM2MmY5Yjc4MSJ9; city=eyJpdiI6IkRGQTl6ODVWbkg5ZmU0elwvcXpTVld3PT0iLCJ2YWx1ZSI6ImZrUXNJamZ6dGkxZzc2aFZiYlJCcXlKXC95bzJyQVwvbXo0b3ZNUDNcL2dpeE9zYVhpdDJ0bnMrN0hnUlFcLzFOM0VMTFpJMVwvcTkyejd6azlJcUY1SHZvc3czUmFsc2J2ZFhhWVBaVXNEMEVzenBsMUdxMDQzaWo2ZVhTTTFEdVBcLytUWmd6Qytha2VzaHNUbXo0TmZzanVzVEx4blVzTG1pWWFqdDF3dXJqS0I2S2Y1ZThLeDVveXFBSDdCS3JRTTFjcVNjNUh0OWp5RlJZYmh2SUlhNEMzdHp2Um93aFwvMFl5QVBwZmtTTkJ6N1wvSDVmc2V2ek1JZE52cEJLZXRscitsNTJsOVFLOFFFQ1NoOHZ1Vk9XWG1SMUdKUG5iUklPYXdxdUh4c041T3p4dGM9IiwibWFjIjoiYzNiNWJlZmNhMzVkMTk5MzM3MWZmMTliY2M2NDliNmI5ZGNkOTQwYzI5NzlhYmNjMDJiYTBhZjAxMGFmMGU3NCJ9; citypy=eyJpdiI6ImFPN3VrQVhZb1BiRzBkVHBBV21OZWc9PSIsInZhbHVlIjoiWk5ubm53N2JaeGVvQ2RMN1E4dUNMZz09IiwibWFjIjoiZGQ2YmMwODUyYzk3ZDU1ZmMwNWI2MWViODExOTA3NTA1NTU1NTM3M2NiYmQwYTJhMGU2ODRhMDNkNWFiMDg0MyJ9; agent_sofang_session=0997ce38e2bf724675a9c34c8750b8138b35948f; XSRF-TOKEN=eyJpdiI6Ijl3ZkUzZGlXdU1xRUxcL3F3ZlZ4Sit3PT0iLCJ2YWx1ZSI6IkpIXC9vb2p4WGdiQ1wvUnBYMnhac2VGUXlENmg1dDVGTmhyUWpoK2JNWTBkQUlwU0ozb01GOUxLM0hhNTZcL2JXdXAwblBubW5HMjB0MTh0emxZMlwveDNlQT09IiwibWFjIjoiMzUxYmM2NTcwMmI2Y2UxYzk0MzNlZDU0NjJmMGE2YjA0NGQ1ZDNhMGYzNzAxZDA4NzgyNjg2Zjg5NGM5Y2QyNyJ9'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldrent/house',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        data = {
            '_token': item["token"],                                #token
            'houseType1': item["houseType1"],                       #房屋类型（houseType1）
            'cityId': item["cityId"],                               #市(cityId)
            'cityareaId': item["cityareaId"],                       #区(cityareaId)
            'name': item["name"],                                   #小区(name)
            'address': item["address"],                             #地址(address)
            'communityId': item["communityId"],                     #小区id（communityId）
            "area": item["area"],                                   #面积(area)
            "price2": item["price2"],                               #出售价格 (price2)
            'priceUnit': item["priceUnit"],                         #价格单位（priceUnit）
            'fitment': item["fitment"],                             #装修状况（fitment）
            'roomStr': self.roomStr ,                               #室厅卫厨(roomStr)
            "currentFloor": item["currentFloor"],                   #楼层(currentFloor)
            "totalFloor": item["totalFloor"],                       #总楼层(totalFloor)
            'faceTo': item["faceTo"],                               #房屋朝向（faceTo）
            "title": item["title"],                                 #标题(title)
            'describe': item["describe"],                           #描述(describe)
            'indoor':self.image,                                    #室内图（indoor）
            'titleimg':self.image1,                                 #标题图（indoor）
            "linkman": item["linkman"],                             #联系人(linkman)
            "linkmobile": item["linkmobile"]                        #电话(linkmobile)
        }
        print(data)
        print("*" * 80)
        url='http://agent.sofang.com/submitsale'
        res = requests.post(url, headers=headers_1, data=data).content.decode()
        print(res)
        self.ritem['url'] = url
        result = re.findall('''"result":(.*?),"message":"(.*?)"''', res)[0]
        if result:
            if 'false' in result:
                self.ritem['error'] = result[1]
                self.ritem['release'] = 2
            else:
                self.ritem['release'] = 1
                self.id = re.findall('"message":"rent-(.*?)"', res)[0]
                print(self.id)
    #出售正式发布
    def chushou_fabu(self):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; agent_sofang_session=e2f4fc14b3a003bb838f82e5b9f957e399bb8dbf; cityid=eyJpdiI6IlZVaHdEUXFJdlwveWh4enpjVEx1cytnPT0iLCJ2YWx1ZSI6InY2aDZXZ3Z6S2Jxckdmd0pQUCs5dnc9PSIsIm1hYyI6ImU2M2JiNGM3MzBiZjlkMGU0MGE4ZWMzM2UwNGVhYjJmYmEwNzliNmRlNDE4ODA5YWZiMjEwYjBmMjMzMjFjZDgifQ%3D%3D; city=eyJpdiI6Inc2XC9scGxTdkhxMndjZG9JWVJjSDl3PT0iLCJ2YWx1ZSI6IndoK0E2bk9GbVwvNnFmeEExN002a2JzY1c4bWVkUyt2UkpDdSttV29wbUNscDNxdldqbnFrRWdFSUhwNVhLUnArRUZ3NG1EWnNUR0UwUHJjK1dsUWJQQitLY2QyaStnSU4yXC84T1JiNUdwVmVjVHoxcjRpWEswcTIxbGlHd0xYSDEzVFI5XC84YTJaVm1raDd5Vjh2VnBVZ2U1RmtHZzZ1cHVZYkZCbTNOb2xSUDlIMzNTcm9PeStTZE1FMURkS0Y2aDBBSXZHRjNueDRBZ0s3d1J2UVo0b2I5TmNQS01kM29MNVJ3OExWVDBXbDRVRjZsRnNlWlwvZ3ZlUXdNSkQwZVV5S3FGYkFERklTeVpOZVNwYm13bkcxMjFHaEFnb1pFUDFMNk85b0tlWVc0OD0iLCJtYWMiOiJlMGUwN2IyMDAxODBmNTUzZmE2Yjk2NmQ0MDcxNzIzMjkzN2VhNmUwODgwNzdkMWU3MDA0NDBmNWIxMWRhYTFkIn0%3D; citypy=eyJpdiI6InBDNWlKcVAySnlqc1NCdENSXC8xSFBRPT0iLCJ2YWx1ZSI6Imh6cWlvbkQ3TE9vSnJHdjE0ZVJcL1RBPT0iLCJtYWMiOiIxYzVkMzUwNmE5M2VjY2IzMDQ4YTViNjNlNjdjZTUwNmJkNzFjNWE2YTliMDE5YzU4MmIzNjdiZGI0MTQ3NDFlIn0%3D; XSRF-TOKEN=eyJpdiI6ImdUOVc5alBuSGtuUW1Dc2hHVFJNZkE9PSIsInZhbHVlIjoiNkxRR01oZXoyQ3VoQmVIYTc5a1o5VXdiTHBJQmpycEVqU0hXQjBVa1pTUFN0QVRjcm5CVkt3VFFZdE9SZG9iR2VBUkR5V2F6V1wvTnh1VnFTXC9HeUZrdz09IiwibWFjIjoiMDA1OWViZjBlYjMyOTc2YzNkYTE4MGVmMGZiMGI1YjIzN2QwZDUzMGMwNmZhMDE2ZWI5MTg1ZDMyMmE0MDM4YSJ9'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldrentmanage/shops/releaseed',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        data_1 = {
            'id': self.id
        }
        url = 'http://agent.sofang.com/statussale/release?id={}'.format(self.id)
        response = requests.get(url, headers=headers_1, data=data_1).content.decode()
        if response=="1":
            print("正式发布成功")
        elif response=="5":
            print("您当天免费发布套数已用完！")
        else:
            print("正式发布失败")

    def run(self,item):
        self.__newSession()
        city_area_id = self.__searchByCity(item['localArea'], item['localDiduan'])
        if not city_area_id:
            return 0
        self.city_id = city_area_id[0]
        self.area_id = city_area_id[1]
        if item['rentType'] == '1':
            self.addCzInfo(item)
            self.chuzu_fabu()
            return self.ritem
        else:
            self.addCsInfo(item)
            print(self.ritem)
            self.chushou_fabu()
            return self.ritem

if __name__ == '__main__':
    item = {
    'token': 'EA5qr8p2jP4jTWXoNpH44lLb6shQqN7Wld6NKdNZ',                         # 在house?rentType=1里面
    "rentType": "1",                                                             #（1整租2合租。这里把1写死，合租暂时不涉及）
    'houseType1': '3',                                                           #(3住宅2写字楼1商铺)
    "cityId":"332","cityareaId":"2985",
    "price": '3456',                                                             #出租用price出售用price1或者price2
    "price2":'154',"area":'456', 'priceUnit':'2',                                #2,price2住宅1,price1写字楼商铺
    "name":'月亮湾浦发广场',"address":'普陀中山北路1655弄10支弄','communityId': '306030',
    "fitment":'3',                                                                #（1毛坯2简装3中装修4精装修5豪华装修）
    "shi": "3",
    "ting": "2",
    "wei": "1",
    "chufang": "1",
    "faceTo":"1",                                                                 #（1东2南3西4北5南北6东南7西南8东北9西北10东西）
    "currentFloor":"4","totalFloor":"25",
    # "houseType2":"301",                                                           #(302经济适用房303商住楼304别墅305豪宅306平房307四合院)（3住宅2写字楼1商铺）
    "title":"信你据斤斤计上风格化斤erty计较但广发VC方法给-寒计较斤斤计较斤斤计较斤斤计较",
    "describe":"水水水水水水d水时间还哈工水ghplm水水法的实施",
    "linkman":"张鱼","linkmobile":"15629185662",

    }

    SoufangRelease().run(item)

# 1 发布数量没有限制，但是title相同的不能重复发，
# 2 信息有预发布和已发布两个步骤
# 3 不同账号改token和cookie值
# 4 住宅商铺写字楼只用换2个字段（houseType1，priceUnit）
# 5 除了市（cityId）区（cityareaId）其他字段可随便填