import asyncio

iteration_time = [10, 1, 3, 2, 1]

async def a_sleeper(seconds, i=-1):
    if i != (-1):
        print(f"{i}\t{seconds}")
        await asyncio.sleep(seconds)
    
    
async def a_run():
    for i, second in enumerate(iteration_time):
        asyncio.create_task(a_sleeper(second, i=i))

asyncio.run(a_run())