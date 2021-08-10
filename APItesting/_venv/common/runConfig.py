import configparser
import json

def readIni():
    config = configparser.ConfigParser()
    config.read('/Users/renren/PycharmProjects/APItesting/_venv/config/config.ini')
    host = config.get('database', 'host')
    path = config.get('log', 'path')
    print(host)
    print(path)

# 别处引用时，也会执行
# readIni()

# 只有run当前文件时才会执行
if __name__ == '__main__':      # 输入main，按tab键
    readIni()

def readJson():
    # 字典单引号，字符串双引号
    j = '{"username":"huice","pwd":"123456"}'

    d = json.loads(j)  # 将json字符串转换成Python字典
    print(d)
    d = {'username': 'huice', 'pwd': '123456'}
    j = json.dumps(d)  # 将字典转换成json
    print(j)

if __name__ == '__main__':
    readJson()
