#multiple fetch requests

import asyncio
import aiohttp

async def multiple_fetch_function(session, url):
    #make a get request
    async with session.get(url) as response:
        print(f"Fetched {url} with status:{response.status}")
    
async def main():
    urls = ["https://httpbin.org/delay/2"] * 3 #makes it 3 urls.

    #Create a session
    async with aiohttp.ClientSession() as session:
        tasks = [ multiple_fetch_function(session,url) for url in urls]
        #same as , tasks = [ t1, t2, t3 ]

        await asyncio.gather( *tasks )    #we could have used aysncio.gather( f1, f2, f3) and let manually send 
       #await asyncio.gather(             functions, but we used a list of functions, and * operator unpacks the list
        # t1(),                           *operator unpacks lists
        # t2(),                           **operator unpacks dictionary      
        # t3(),
       # )                               

asyncio.run(main())                            