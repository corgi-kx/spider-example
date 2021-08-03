import asyncio
import os
import aiofiles
import aiohttp
import requests
from lxml import etree

bookDir = "./三国"

urlMain = "http://sanguo.5000yan.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}


def mkDir():
    if not os.path.exists(bookDir):
        os.mkdir(bookDir)


async def getPageUrl(urlMain):
    resp = requests.get(url=urlMain, headers=headers)
    resp.encoding = "utf-8"
    # resp.text.encode('utf-8').decode('unicode_escape')
    # with open("sanguo.html","w",encoding="utf-8") as f :
    #     f.write(resp)
    et = etree.HTML(resp.text)
    liList = et.xpath('//div[@class="sidamingzhu-list-mulu"]/ul/li')
    print(liList)
    tasks = []
    for li in liList:
        tittle = li.xpath('./a/text()')[0]
        urlDetail = li.xpath('./a/@href')[0]
        print("tittle:%s  url:%s" % (tittle, urlDetail))
        tasks.append(asyncDownLoad(urlDetail, tittle))

    await asyncio.wait(tasks)


async def asyncDownLoad(url, fileName):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as resp:
            # print(await resp.text())
            et = etree.HTML(await resp.text())
            divList = et.xpath('//div[@class="grap"]/div')
            async with aiofiles.open(bookDir + "/" + fileName + ".txt", "w", encoding="utf-8") as f:
                for div in divList:
                    article = div.xpath('./text()')[0]
                    # print(article)
                    if str(article).find(" ") > 0:
                        # print("sssss")
                        continue
                    await f.write(article)


if __name__ == '__main__':
    mkDir()
    asyncio.run(getPageUrl(urlMain))
