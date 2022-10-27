import asyncio
import requests
import time


async def counter(until: int = 10) -> None:
    now = time.perf_counter()
    print("Counter started")
    for i in range(0, until):
        last = now
        await asyncio.sleep(0.01)
        now = time.perf_counter()
        print(f"{i}: was asleep for {now - last}s")


def get_status_sync(url: str) -> int:
    print("Sending HTTP request")
    response = requests.get(url)
    return response.status_code


async def get_status_async(url: str) -> int:
    return await asyncio.to_thread(get_status_sync, url)


async def main() -> None:
    # sync
    # status_code = get_status_sync("https://example.com")
    # await counter()

    # sync too
    # task = asyncio.create_task(counter())
    # status_code = await get_status_async("https://example.com")
    # await task

    # async
    status_code, _ = await asyncio.gather(
        get_status_async("https://example.com"),
        counter(),
    )

    print(f"HTTP response with status {status_code}")


asyncio.run(main())
