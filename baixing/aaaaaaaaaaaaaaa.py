import requests
import re
import json

"""
{
name：小区门
city:城市
area：区域
street：街道
adress：地址
price:均价
url:详情页连接
}

"""


class Ganji_Cs:
    def __init__(self):
        self.cookie = '''ganji_xuuid=e8045685-367b-436b-d2f5-3b952f460966.1535098201433; ganji_uuid=9794110922303180317680; xxzl_deviceid=AA9M9XkJTr4CbY7nbaT3gZAlEMVAw92TGqg2Rq3bq6yIpm%2BIdM00sLw%2FFC%2FQNB6A; __utmganji_v20110909=0x1e6b4ea4d53f03d7d5b19de94627879; lg=1; 58tj_uuid=30cba9b8-f5b7-4cfb-a31c-62c041503b65; wmda_uuid=9c77a55511c6e2ff861e1c051a660daf; wmda_new_uuid=1; als=0; wmda_visited_projects=%3B3603688536834%3B3381039819650; citydomain=sh; bdshare_firstime=1535944823007; NTKF_T2D_CLIENTID=guest60BAD191-21A3-835D-67E7-9D7212122DF3; __utmc=32156897; use_https=1; ganji_fang_fzp_pc=1; ershoufangABTest=B; gj_footprint=%5B%5B%22%5Cu4e8c%5Cu624b%5Cu623f%5Cu51fa%5Cu552e%22%2C%22http%3A%5C%2F%5C%2Fsh.ganji.com%5C%2Ffang5%5C%2F%22%5D%2C%5B%22%5Cu79df%5Cu623f%22%2C%22http%3A%5C%2F%5C%2Fbj.ganji.com%5C%2Ffang1%5C%2F%22%5D%5D; webimFangTips=793925505; _wap__utmganji_wap_caInfo_V2=%7B%22ca_name%22%3A%22mobile_fang5_fabu_youce%22%2C%22ca_source%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%7D; _wap__utmganji_wap_newCaInfo_V2=%7B%22ca_n%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_i%22%3A%22-%22%7D; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22mobile_fang5_fabu_youce%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A52640273650%7D; GANJISESSID=9sv2o7sl7r2e3s65pim4l6vms7; sscode=skQyScoW8enxRD8UskGoPyjy; GanjiUserName=%E6%88%90c%E5%A4%A7w%E5%99%A8j; GanjiUserInfo=%7B%22user_id%22%3A793925505%2C%22email%22%3A%22%22%2C%22username%22%3A%22%5Cu6210c%5Cu5927w%5Cu5668j%22%2C%22user_name%22%3A%22%5Cu6210c%5Cu5927w%5Cu5668j%22%2C%22nickname%22%3A%22%22%7D; bizs=%5B%5D; supercookie=AmxmBGV1AGN1WQuuMwNlLJH0BJL4LGVmMQp0AGL2ZQp4BQN4MJV1BJHkZwplBGEwZwL%3D; username_login_n=%E6%88%90c%E5%A4%A7w%E5%99%A8j; GanjiLoginType=0; last_name=%E6%88%90c%E5%A4%A7w%E5%99%A8j; nTalk_CACHE_DATA={uid:kf_10111_ISME9754_793925505,opd:1}; new_uv=7; utm_source=; spm=; __utma=32156897.100183559.1535098210.1536033387.1536036452.10; __utmz=32156897.1536036452.10.10.utmcsr=sh.ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; new_session=0; init_refer=http%253A%252F%252Fwww.ganji.com%252Fvip%252Fmy_post_list.php%253F_rid%253D0.27302813643034707; xxzl_smartid=6ccb2ad0d564653498f19e6e6a4879ab; ganji_login_act=1536036573950; __utmb=32156897.7.10.1536036452; nTalk_PAGE_MANAGE={|m|:[{|61707|:|367524|}],|t|:|12:52:32|}'''

    def img(self):
        img_list = [[], []]
        files_name = [r'C:\Users\Admin\Pictures\Saved Pictures\3b87e950352ac65ca217f7fbf1f2b21193138a2c.jpg', r'C:\Users\Admin\Pictures\Saved Pictures\8b13632762d0f703ea7608fb02fa513d2797c5d5.jpg']
        for img in files_name:
            files = {'attachment_file': ('timg.jpg', open(img, 'rb'), 'image/jpeg')}
            res = requests.post('http://image.ganji.com/upload.php', files=files)
            res = res.content.decode()
            r_d = json.loads(res)
            image = {"image": r_d["info"][0]["url"], "thumb_image": r_d["info"][0]["thumbUrl"],
                     "width": r_d["info"][0]["image_info"][0], "height": r_d["info"][0]["image_info"][1], "is_new": 'true'}
            img_list[0].append(image)
        self.image = str(img_list).replace("'true'", 'true').replace(" ", '').replace("'", '"')
        print(self.image)
    def put(self):
        headers = {
            'Cookie': self.cookie,
        }
        url = "http://www.ganji.com/pub/pub.php?cid=7&mcid=20&act=pub&method=submit"
        response = requests.session()
        data = {
            "xiaoqu": '公捷苑',
            "xiaoqu_pinyin": "",
            "district_id": "205",
            "street_id": "-1",
            "xiaoqu_address": "谷阳北路",
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
            "phone": "15839900552",
            "agent": "1",
            "images": self.image,
        }
        print(data)
        res = response.post(url, headers=headers, data=data).content.decode()
        res_1 = re.findall('''displayError\("(.*?)"\)''', res, re.S)
        if not res_1:
            res_2 = re.findall('''(恭喜您，发布成功啦！)''', res, re.S)
            print(res_2[0])
            return res_2[0]

        else:
            print(res_1)
            return str(res_1)
if __name__ == '__main__':
    ganji = Ganji_Cs()
    ganji.img()
    ganji.put()
