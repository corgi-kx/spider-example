import json

import requests

url = 'https://fanyi.baidu.com/sug'

headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
kw = input('请输入要搜索的单词:')
data = {
    'kw':kw
}

resp = requests.post(url=url,data=data)
print(resp.text.encode('utf-8').decode('unicode_escape'))


