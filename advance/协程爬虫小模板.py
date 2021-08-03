import asyncio
import time


async def downLoad(url):
    print("正在下载%s！" %url)
    await asyncio.sleep(3)
    print("%s下载完毕！" %url)


async def main():
    urls = [
        "http://www.baidu.com/",
        "http://www.163.com/",
        "http://www.qq.com/",
        "http://www.sougou.com/",
        "http://www.google.com/",
    ]

    tasks = [downLoad(url) for url in urls]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print("总耗时%f秒" %(t2 - t1))
