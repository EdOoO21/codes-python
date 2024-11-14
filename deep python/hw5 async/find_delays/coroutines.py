import asyncio
import time

# Текущая реализация не проходит тесты! Вам нужно настроить задачи, так чтобы оно проходило тесты!
async def coroutine_1(delay=0.1):
    start = time.time()
    print(f"First message from coroutine 1")
    await asyncio.sleep(delay * 3)
    print(f"Second message from coroutine 1")
    await asyncio.sleep(delay * 2) # 0.5
    print(f"Third message from coroutine 1")
    await asyncio.sleep(delay * 1) # 0.6
    print(f"Forth message from coroutine 1")
    await asyncio.sleep(delay * 4) # 1
    print(f"Fifth message from coroutine 1")


async def coroutine_2(delay=0.1):
    start = time.time()
    print(f"First message from coroutine 2")
    await asyncio.sleep(delay * 2)
    print(f"Second message from coroutine 2")
    await asyncio.sleep(delay * 1) # 0.3
    print(f"Third message from coroutine 2")
    await asyncio.sleep(delay * 5) # 0.8
    print(f"Forth message from coroutine 2")
    await asyncio.sleep(delay * 1) # 0.9
    print(f"Fifth message from coroutine 2")


async def coroutine_3(delay=0.1):
    start = time.time()
    print(f"First message from coroutine 3")
    await asyncio.sleep(delay * 1)
    print(f"Second message from coroutine 3")
    await asyncio.sleep(delay * 3) # 0.4
    print(f"Third message from coroutine 3")
    await asyncio.sleep(delay * 3) # 0.7
    print(f"Forth message from coroutine 3")
    await asyncio.sleep(delay * 4) # 1.1
    print(f"Fifth message from coroutine 3")


async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )


asyncio.run(main())