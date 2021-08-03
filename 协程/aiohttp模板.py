import asyncio
import aiohttp
import aiofiles

urls = [
    "https://img.lianzhixiu.com/uploads/allimg/160109/9-160109112514.jpg",
    "https://img.lianzhixiu.com/uploads/allimg/160109/9-160109112511.jpg",
    "https://img.lianzhixiu.com/uploads/allimg/160109/9-160109112516.jpg",
    "https://img.lianzhixiu.com/uploads/allimg/160109/9-160109112519.jpg",
    "https://img.lianzhixiu.com/uploads/allimg/160109/9-160109112520.jpg",
    "https://img.lianzhixiu.com/uploads/allimg/160109/9-160109112523.jpg",
]

headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

async def aioDownLoadPic(url):
    fileName = url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url,headers=headers) as resp:
             async with aiofiles.open("./pic/"+fileName,"wb") as f:
                 await f.write(await resp.content.read())
    await asyncio.sleep(0.5)
    print("over!!!",url)

async def main():
    tasks = [aioDownLoadPic(url)  for url in urls]
    await asyncio.wait(tasks)
if __name__ == '__main__':
    asyncio.run(main())