import asyncio
import aiohttp

async def fetchurl(session,url):
    async with session.get(url) as response:
        print(f"fetched {url} with status {response}")

async def main():
    urls=["https://amityonline.com/","https://in.bookmyshow.com/"]  
    async with aiohttp.ClientSession() as session:
        tasks=[fetchurl(session,url) for url in urls]
        await asyncio.gather(*tasks)
asyncio.run(main())        
