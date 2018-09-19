
import json
import re

import requests
import base64

from lxml import etree
from selenium import webdriver
import time
#搜房房屋出租

class Soufang_Cs():
    def __init__(self):
        self.n = 5
    def put(self):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; www_sofang_session=eyJpdiI6InpzUDJxNU5xaEhLTDNCcSt2SkNZY1E9PSIsInZhbHVlIjoiWjJvVVg3cGIzRzhcL2JRZks1MVhTTVpvRlU3Vnp5aHRiSXBFeWNxQ21sXC9vM2xVNjdxU2dHamNJeU9iXC9hb1RDR2xJN1lldGV1MmlSdzI4cmxiVzNkcXc9PSIsIm1hYyI6ImQ4YTdmYzhjYTRjNjkyOTkwZjEwODU2OTI5MWFiNTk4NDEyYjFlMGZjNmRmZDU5ODU1NTM2Njk1NTY0N2RkZTYifQ%3D%3D; cityid=eyJpdiI6InF1UlNHMWU2T2k4M2JaYmRqbDU0UlE9PSIsInZhbHVlIjoiNThUWHhYaEVUdmNFXC9JaEtpNVd2WHc9PSIsIm1hYyI6IjQ1YjE4ZWNjMGFmMGFhMDM3M2Q4OWRkYWNlZGQ1MTczYTUxMzEwYTQ0MDZiM2JmZWM4ZWYyOThlNGZhYzAzMTQifQ%3D%3D; city=eyJpdiI6IldjdHpINzNBUVJLNFBDbmVvaURyZWc9PSIsInZhbHVlIjoiaVk3Sms1V3RzVU5XdVpTbnFpRVpsUEVsY1RTMXU2dTNlMGI2Tnk2cmt3RUhTUjBiVG9HWjNVVE1rd1ZxY3o4XC9rUDRzclVod1ZGbWQ0a1ZFUERpVTc4NUhUR2JrRWFSTGtXVHlyXC9sMDVENzhjaEs2R1dSdHVNNkN3NXUrOTBmc25ZMzVIOUx1QWpRRnRYSjExWW1lbklIdVBDZ2ZXbG9YWEQ3UktcL0hcL1pralYwMWo5cCtxekY1RmV1STVvR1wvRWJlVkoyU1pna2gzTGJjTndoZ2p0dVwvazV0dU9USlFjUUhSZVlMTm0zQ1VKRndGSUEyRDFDMDZBd042NzhIVzRaS2FTRVBWZk1QekJ1RDFxbGY1bUdxdGlETnR0NzJMUVZhOW5yMTFZWEw1RDg9IiwibWFjIjoiYTdjYmNiYmNkMzhlMDU2ZmEzZDljMDg4MzQyODc2NThlN2U3NzMxNDQ2MDRlMGM4Mjc5Mzc1NzFhOTM5ZGYzZCJ9; citypy=eyJpdiI6Im83NzN3dDUwZGJwWXdMalN4NTZ4dEE9PSIsInZhbHVlIjoiTWQzUW5MN1BCSUxHUExwVytrNk9CQT09IiwibWFjIjoiYTRhZWEzMTIxZDFjYWEwZjc4ODBlMGFhNDkxNTdmYmM5ZGEyZTE4MjQxYjI1MDQ0YjNkMmM5ZmZiNTJkOTllOSJ9; agent_sofang_session=e7755e867ad6c303d29a01b453980c8cfa44d594; XSRF-TOKEN=eyJpdiI6IlB0V1BSc1laeW1wNXV4TVpuNk1ZZHc9PSIsInZhbHVlIjoiMVpOdUZUZWdjWk9GRDY4RmZpa21TVUVTdkE5b2oyYis0OG1PSzFGSFVwRWU5elBLVDk4a2EzM1wvaFwvYm1lYmQ0QnM0VjljTWJkTGZpSkh3ekNmTEkrZz09IiwibWFjIjoiYzI0M2ZmNWVkNjQ5N2FmNzdkNDBkMGZlNWM2YmFkMDJiOWM1Zjk0YTI1ZjJkODg1MmM5YzI5NDI3NjJlMGY2MCJ9'
        headers = {
            'host': 'www.sofang.com',
            'Referer': 'http://agent.sofang.com/oldrent/house?rentType=1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,
        }
        data = {
            '_token': 'rUgUrHUP7xEdsxNo6ZMRuVYmbovCchCAIJ89iLLp',
            'communityId': '132256',
            'houseType1': '3',
            'longitude': '121.443566',
            'latitude': '31.268065',
            'rentType': '1',
            'provinceId': '3',
            'cityId': '332',
            'cityareaId': '2985',
            'businessAreaId': '4704',
            'name': '展宏大厦',
            'address': '普陀区延长西路318弄之2 - 9号',
            'roomStr': '1_1_1_1',
            'houseRoom': '1',
            'currentFloor': '5',
            'totalFloor': '50',
            'houseType2': '303',
            'fitment': '3',
            'faceTo': '1',
            'area': '158',
            'price': '5000',
            'priceUnit': '1',
            'paymentType': '1',
            'equipment[]': '9',
            'title': '上的风格不VS东方宾馆的发行收入已经',
            'indoor': '[{"img": "/house/rent/2018_09/11/143240_1536647560_FBCS.jpg", "note": "", "type": "10"}]',
            'titleimg': '[{"img": "/house/rent/2018_09/11/143242_1536647562_5313.jpg", "type": "9", "note": "", "tag": "2"}]',
            'linkman':'鱼',
            'linkmobile':'15629185662'

        }

        url = 'http://agent.sofang.com/submitrent'
        res = requests.post(url, headers=headers, data=data).content.decode()
        print(res)

if __name__ == '__main__':
    soufang =Soufang_Cs()
    soufang.put()

