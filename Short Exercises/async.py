import asyncio


async def square(x):
    print('Square', x)
    await asyncio.sleep(1)
    print('End square', x)
    return x * x


# Create an event loop
loop = asyncio.get_event_loop()

# Run async function and wait for completion
results = loop.run_until_complete(asyncio.gather(
    square(3),
    square(4),
    square(9),
    square(13)
))

print(results)

# Close the loop
loop.close()
