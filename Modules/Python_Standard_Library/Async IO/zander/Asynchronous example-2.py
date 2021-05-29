import asyncio

async def task1():
    print("Send first Email")
    asyncio.create_task(task2())
    await asyncio.sleep(5)
    print("First Email reply")

async def task2():
    print("Second email sent")
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print("Second Email reply")

async def task3():
    print("Third email sent")
    await asyncio.sleep(1)
    print("Third Email reply")

asyncio.run(task1())