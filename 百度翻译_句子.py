import json

import requests

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
kw = input('请输入要搜索的单词:')
data = {
    'query':kw,
    'from':'en',
    'to':'zh',
    'transtype':'realtime',
    'domain':'common',
    'simple_means_flag':3,
    'sign':559503.813758,
    'token':'6d53fc05aa68ffc35b4c9d9da6daddab'
}

resp = requests.post(url=url,data=data)
print(resp.text.encode('utf-8').decode('unicode_escape'))


