# 封装get、put、 delete、 post
# 代码封装方式：1、直接在模块封装 2、在类中封装
#
import json

import requests

def get():
    requests.get()

def put():
    requests.put()
# 请求是独立的
# get()
# put()

# 封装response返回数据
class Response:
    def __init__(self, response):
        self.__response = response

    @property
    def data(self):
        try:
            d = {'code': self.__response.status_code, 'data': self.__response.json()}
        except json.decoder.JSONDecodeError as e:
            d = {'code': self.__response.status_code, 'data': e.msg}
        return d

class HttpClient:
    # 初始化函数，创建session保持一个会话
    def __init__(self):
        self.__session = requests.session()

    def get(self, url, params=None, cookies=None, timeout=None):
        """
        get请求
        :param url: 地址
        :param params: dictionary,请求地址?后的参数列表
        :param cookies: dict,cookie信息
        :param timeout: 请求超时时间
        :return: 请求的数据
        """
        response = self.__session.get(url=url, params=params, cookies=cookies, timeout=timeout)
        if response.status_code == 301:
            response = self.__session.get(url=response.headers.get('location'))
        try:

            # return response.status_code, response.json()
            return Response(response).data
        except:
            # json解析错误
            pass
            # 写到日志中

    def put(self):
        self.__session.put()

    def post(self, url, data=None, headers=None, cookies=None, timeout=None, verify=False):
            response = self.__session.post(url=url, data=data, headers=headers, cookies=cookies, timeout=timeout, verify=verify)
            return Response(response).data
            # return response.status_code


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

dataS = '''
{
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2021-08-30T10:28:22.824Z",
  "status": "placed",
  "complete": false
}
'''

if __name__ == '__main__':
    client = HttpClient()
    # params = {'status': 'available'}
    # s, k = client.get(url='https://petstore.swagger.io/v2/pet/findByStatus', params=params)
    # print(s, k)

    # headers = {'content-type': 'application/json'}
    # a = client.post(url='https://petstore.swagger.io/v2/store/order', data=dataS, headers=headers, verify=False)
    # print(a)


    # 获取登录Token
    user = {'username': 'admin', 'password': 'admin'}
    response = client.post(url='http://flash-admin.enilu.cn/prod-api/account/login', data=user, verify=False)

    print(response)
    # 获取返回的字典中的，token数据
    token = response.get('data').get('data').get('token')
    print(token)

    # 部门管理添加部门（需要登录）
    headers = {'Authorization': token}
    d = client.post(url='http://flash-admin.enilu.cn/prod-api/dept?simplename=xxx&fullname=xy&num=123&pid=1', headers=headers)
    print(d)
#  问题：post请求，传参是json数据，为什么要用data而不用json??? #

