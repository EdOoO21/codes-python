import aiohttp
import asyncio


async def send_request(session, url):
    try:
        await session.get(url)
    finally:
        return


async def main(url, total_requests, concurrent_requests):
    connector = aiohttp.TCPConnector(limit=concurrent_requests)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [send_request(session, url) for _ in range(total_requests)]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    TOTAL_REQUESTS = 100000
    CONCURRENT_REQUESTS = 3000
    url = "http://localhost:8888/"
    asyncio.run(main(url, TOTAL_REQUESTS, CONCURRENT_REQUESTS))
