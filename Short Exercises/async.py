import asyncio


async def square(x):
    print('Square', x)
    await asyncio.sleep(1)
    print('End square', x)
    return x * x


###########################################################################

# Create an event loop
loop = asyncio.get_event_loop()

async def whenDone(tasks):
    for res in asyncio.as_completed(tasks):
        print('Result: ', await res)

# Run async function and wait for completion
loop = asyncio.get_event_loop()
loop.run_until_complete(whenDone([
    square(3),
    square(4),
    square(9),
    square(13)
]))

