import asyncio

async def getNum(num):
    print(num)
    await asyncio.sleep(2)
    print(num,"over!")

taskList=[getNum(i) for i in range(1,100)]
asyncio.run(asyncio.wait(taskList))


# async def main():
#     taskList=[]
#     for i in range(1,100):
#         taskList.append(asyncio.create_task(getNum(i)))
#     await asyncio.wait(taskList)
#     # await asyncio.sleep(5)
#
# asyncio.run(main())