import requests

kw = input("请输入要搜索的内容:")
url = 'https://www.sogou.com/web?'

headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

params = {
    'query':kw
}

resp = requests.get(url=url,headers=headers,params=params).text
fileName = kw + ".html"
with open("./" + fileName,'w',encoding='utf-8') as f:
    f.write(resp)
print('爬取完毕')