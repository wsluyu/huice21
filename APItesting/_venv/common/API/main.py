import requests

# https://editor.swagger.io/

# 1、根据宠物状态信息查询
headers = {'user-agen':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
           'accept': 'application/xml'}
response = requests.get(url='https://petstore.swagger.io/v2/pet/findByStatus?status=available', headers=headers)
print(response.status_code)
print(response.text)

# 2、添加宠物，数据类型是Json: {'Content-Type': 'application/json'}
    #实现方式1,数据格式是json
dataS = '''
{
  "id": 0,
  "category": {
    "id": 0,
    "name": "哈巴狗"
  },
  "name": "哈哈哈",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
'''
# datas:json字符串
headers = {'Content-Type': 'application/json'}
response = requests.post(url='https://petstore.swagger.io/v2/pet', data=dataS, headers=headers)

# 实现方式2,数据格式是字典(最常见的方式)

dataD ={
  "id": 0,
  "category": {
    "id": 0,
    "name": "哈巴狗"
  },
  "name": "哈哈哈",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
# dataD:Python字典
headers = {'Content-Type': 'application/json'}
response = requests.post(url='https://petstore.swagger.io/v2/pet', json=dataD, headers=headers)
print(response.text)

# 3、post请求登陆，数据格式是表单 {'Content-Type': 'x-www-form-urlencoded'}
headers = {'Content-Type': 'x-www-form-urlencoded'}
dataD = {'username': 'admin', 'password': 'admin'}
response = requests.post(url='http://flash-admin.enilu.cn/prod-api/account/login', data=dataD, headers=headers)
print(response.text)

# 作业：实现长传图片接口

