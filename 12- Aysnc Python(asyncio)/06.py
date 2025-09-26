# Multiprocessing with asyncio

import asyncio
from concurrent.futures import ProcessPoolExecutor  #Executes all the processes in the pool

def encrpt(data):
    return f"🔒{data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrpt , "creditcardno:764323")
        print(result)
    
if __name__ == "__main__":
    asyncio.run(main())


#The whole def encrpt function does is, it takes the hevay cpu task of encription
# and runs in a whole together separate Process, and keeps the main process easy,and event loop working
#not blocking the code, not running in the main processs ,not taking much time, and making it efficient.