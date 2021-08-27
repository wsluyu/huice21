# 封装get、put、 delete、 post
# 代码封装方式：1、直接在模块封装 2、在类中封装
#
import requests

def get():
    requests.get()

def put():
    requests.put()
# 请求是独立的
# get()
# put()


class HttpClient:
    # 初始化函数，创建session保持一个会话
    def __init__(self):
        self.__session = requests.session()

    def get(self, url, params=None, cookies=None, timeout=None):
        response = self.__session.get(url=url, params=params, cookies=cookies, timeout=timeout)
        if response.status_code == 301:
            response = self.__session.get(url=response.headers.get('location'))
        try:

            return response.status_code, response.json()

        except:
            # json解析错误
            pass
            # 写到日志中

    def put(self):
        self.__session.put()

    def post(self):
        self.__session.post()
'''
# 类里面的请求共用一个会话，如一个登陆账号
# 如账号1
client = HttpClient()
client.get()
client.post()
# 账号2
client2 = HttpClient()
client2.get()
client2.post()
'''
if __name__ == '__main__':
    client = HttpClient()
    params = {'status': 'available'}
    s, k = client.get(url='https://petstore.swagger.io/v2/pet/findByStatus', params=params)
    print(s, k)

