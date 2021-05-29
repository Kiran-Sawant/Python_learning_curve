import asyncio

async def send_mail(msg:str, delay:float)->None:
    print(msg)
    await asyncio.sleep(delay)
    print("awake now" + msg)

# asyncio.run(send_mail(2))
asyncio.run(asyncio.wait([send_mail('mail_1', 1), 
                            send_mail('mail_2', 3), 
                            send_mail('mail_3', 4)]))