import requests

url = "https://www.baidu.com/s?wd=ip"
headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

proxies = {
    "https":"61.145.212.31:3128"
}
resp = requests.get(url=url,headers=headers,proxies=proxies).text
with open("ip.html","w",encoding="utf-8") as f:
    f.write(resp)