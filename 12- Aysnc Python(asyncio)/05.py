#Mixing Threads with asyncio in python.
#concurrent.futures = it executes computations ASYNCHRONOUSLY using threads or processes
#and in concurrent.futures we have ThreadPoolExecutor, this takes all threads in the pool and executes it, very
#similar to asyncio.gather() method, in which it executes all the async functions in the pool.

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking in store...")
    time.sleep(3) # blocking code
    return f"{item} stock no: 42"

async def main():
    loop = asyncio.get_running_loop()  # like an event loop but for threads.
    with ThreadPoolExecutor() as pool:
         #run_in_executor constantly runs the threads
        result = await loop.run_in_executor(pool, check_stock , "Nike Shoes 12")  
        print(result)
    
asyncio.run(main())

#run_in_executor takes the threads and run in another thread , therefore not blocking the code
#it takes the blocking code out of the main thread , and runs it in another thread. 
# therefore making it efficient, that even though we have blocking code , then also we can run fast 