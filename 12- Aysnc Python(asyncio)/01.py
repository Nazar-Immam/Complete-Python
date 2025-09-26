import asyncio

async def chai():
    print("Chai Brewing...")
    await asyncio.sleep(2)
    print("Chai is ready")


asyncio.run(chai())
