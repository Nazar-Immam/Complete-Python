#aiohttp - asynchornous HTTP client server library , built on top of aysncio-
#Concepts of aiohttp - aiohttp.ClientSession() - creates a session, opens a connection with the browser,
# we use it with 'async with' so that the session automatically gets closed after use

import asyncio
import aiohttp

async def main():
    #create a session
    async with aiohttp.ClientSession() as session:

        #make a get request
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:

            #save the response in a variable, maybe as json, as text , as raw, anything 
            data = await response.json()
            print(f"Data fetched: {data}, and status: {response.status}")
        
#run it
asyncio.run(main())