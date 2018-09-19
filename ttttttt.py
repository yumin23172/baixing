import requests

class Soufang_Cs:
    def __init__(self):
        self.n = 5
    def fabu(self):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; agent_sofang_session=e2f4fc14b3a003bb838f82e5b9f957e399bb8dbf; cityid=eyJpdiI6IlZVaHdEUXFJdlwveWh4enpjVEx1cytnPT0iLCJ2YWx1ZSI6InY2aDZXZ3Z6S2Jxckdmd0pQUCs5dnc9PSIsIm1hYyI6ImU2M2JiNGM3MzBiZjlkMGU0MGE4ZWMzM2UwNGVhYjJmYmEwNzliNmRlNDE4ODA5YWZiMjEwYjBmMjMzMjFjZDgifQ%3D%3D; city=eyJpdiI6Inc2XC9scGxTdkhxMndjZG9JWVJjSDl3PT0iLCJ2YWx1ZSI6IndoK0E2bk9GbVwvNnFmeEExN002a2JzY1c4bWVkUyt2UkpDdSttV29wbUNscDNxdldqbnFrRWdFSUhwNVhLUnArRUZ3NG1EWnNUR0UwUHJjK1dsUWJQQitLY2QyaStnSU4yXC84T1JiNUdwVmVjVHoxcjRpWEswcTIxbGlHd0xYSDEzVFI5XC84YTJaVm1raDd5Vjh2VnBVZ2U1RmtHZzZ1cHVZYkZCbTNOb2xSUDlIMzNTcm9PeStTZE1FMURkS0Y2aDBBSXZHRjNueDRBZ0s3d1J2UVo0b2I5TmNQS01kM29MNVJ3OExWVDBXbDRVRjZsRnNlWlwvZ3ZlUXdNSkQwZVV5S3FGYkFERklTeVpOZVNwYm13bkcxMjFHaEFnb1pFUDFMNk85b0tlWVc0OD0iLCJtYWMiOiJlMGUwN2IyMDAxODBmNTUzZmE2Yjk2NmQ0MDcxNzIzMjkzN2VhNmUwODgwNzdkMWU3MDA0NDBmNWIxMWRhYTFkIn0%3D; citypy=eyJpdiI6InBDNWlKcVAySnlqc1NCdENSXC8xSFBRPT0iLCJ2YWx1ZSI6Imh6cWlvbkQ3TE9vSnJHdjE0ZVJcL1RBPT0iLCJtYWMiOiIxYzVkMzUwNmE5M2VjY2IzMDQ4YTViNjNlNjdjZTUwNmJkNzFjNWE2YTliMDE5YzU4MmIzNjdiZGI0MTQ3NDFlIn0%3D; XSRF-TOKEN=eyJpdiI6IlB3M3JqcGxudGFta3lYb21IMnEyZnc9PSIsInZhbHVlIjoiVVhudU1mbGdlK2txbkRRN2N3aHRURjZQeVdCWVpZZXluZHpZRUF3VUdsTDBxeDVhcVNUQ1VjRWQ2VWlNcmVpOTQ3UWh3RVkraFFNbTBzUHhrY2NyXC9nPT0iLCJtYWMiOiIxZTU1NjIxZTFkMzc1N2MxNzIxN2I0Yzc1OWMyZTZhOWZkNWU0ZWQxODhhNWRkYWM3YTEzMmI2YWYzMmViNDI5In0%3D'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldrentmanage/shops/releaseed',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        data_1 = {
            'id': '2018090000100413'
        }
        print(data_1)
        url = 'http://agent.sofang.com/statusrent/release?id={}'.format('2018090000100413')
        response = requests.get(url, headers=headers_1, data=data_1).content.decode()
        print(response)
        if response=="1":
            print("正式发布成功")
        elif response=="5":
            print("您当天免费发布套数已用完！")
        else:
            print("正式发布失败")
if __name__ == '__main__':
    soufang = Soufang_Cs()
    soufang.fabu()
