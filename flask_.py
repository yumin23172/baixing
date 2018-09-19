
from flask_ import Flask
from flask_ import request
import sys
import socket
import json
socket.setdefaulttimeout(8)  #设置 握手 链接超时时间
sys.setrecursionlimit(1000000) # 设置修改最大遍历次数

app = Flask(__name__)
# from IpPoolRandom import RandomIp

# ssl_version = self.ssl_module.PROTOCOL_TLSv1,


@app.route('/Test', methods=["POST", "GET"])
def get_qichacha_ShareholderInfo():
    """测试   获取一下请求方给我传递的key参数"""
    companyName = request.args.get("key")
    dict = {"test":companyName}
    return json.dumps(dict, ensure_ascii=False)


if __name__ == '__main__':
    app.run(
        # host='192.168.1.5',
        # port=5000,
        debug=True
    )
