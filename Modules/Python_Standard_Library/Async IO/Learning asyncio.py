import asyncio

def is_prime(x: int) -> bool:
    """Returns True if x is prime"""

    return not any(x//y == x/y for y in range(x-1, 1, -1))

# creating a corutine_________________________#
async def highest_prime_below(x: int) -> None:

    print(f"Highest prime below {x}")

    for y in range(x-1, 0, -1):
        if is_prime(y):
            print(f"Highest prime number below {x} is {y}")
            return y
        await asyncio.sleep(0.01)           # suspention point
    return None                                     # If no prime number found.

async def main():

    #_________This will not work_________#
    # await highest_prime_below(100000)
    # await highest_prime_below(10000)
    # await highest_prime_below(1000)

    #________Use this Insted_____________#
    await asyncio.wait([
        highest_prime_below(100000),
        highest_prime_below(10000),
        highest_prime_below(1000) ], return_when=asyncio.ALL_COMPLETED)

loop = asyncio.get_event_loop()
# Programs entry point.
loop.run_until_complete(main())
loop.close()
