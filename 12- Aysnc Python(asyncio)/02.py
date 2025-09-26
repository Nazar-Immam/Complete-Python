import asyncio

async def brew(name):
    print(f"{name} chai is Brewing...")
    await asyncio.sleep(3) #this await will wait here, but the function would continue for further computations
    print(f"{name} chai is ready .")


async def main():
    await asyncio.gather(   #This gathers all the function that are to be called in async manner
        brew("Masala"),
        brew("Ginger"),
        brew("Mint")
    )

asyncio.run(main())