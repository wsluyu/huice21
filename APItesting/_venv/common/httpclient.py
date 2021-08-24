# 封装get、put、 delete、 post
# 代码封装方式：1、直接在模块封装 2、在类中封装
#
import requests

def get():
    requests.get()

def put():
    requests.put()
# 请求是独立的
get()
put()


class HttpClient:
    # 初始化函数，创建session保持一个会话
    def __init__(self):
        self.__session = requests.session()

    def get(self):
        self.__session.get()

    def put(self):
        self.__session.put()

    def post(self):
        self.__session.post()

# 类里面的请求共用一个会话，如一个登陆账号
# 如账号1
client = HttpClient()
client.get()
client.post()
# 账号2
client2 = HttpClient()
client2.get()
client2.post()
