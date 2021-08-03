import requests

url="https://www.sogou.com/"
resp=requests.get(url)
respData = resp.text
print(respData)
with open("sougou.html", "w", encoding="utf-8") as f:
    f.write(respData)
print("爬取完毕！")