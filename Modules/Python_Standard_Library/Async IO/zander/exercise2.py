import asyncio

async def fetch_data():
    await asyncio.sleep(3)
    print({"data": 100})

async def counter():

    for i in range(10, 0, -1):
        await asyncio.sleep(2)
        print(i)

async def main():

    await asyncio.wait([
        fetch_data(),
        counter()
    ])

asyncio.run(main())