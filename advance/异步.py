import asyncio


async def func(num):
    print("fuck",num)
    resp = await asyncio.sleep(2)
    print("over!",resp)




asyncio.run(func(1))


