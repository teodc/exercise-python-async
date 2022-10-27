import trio
import random


async def producer(sending_channel: trio.MemorySendChannel) -> None:
    async with sending_channel:
        for i in range(5):
            await trio.sleep(random.randint(1, 3))
            print(f"Send value {i}")
            await sending_channel.send(i)


async def consumer(receiving_channel: trio.MemoryReceiveChannel) -> None:
    async with receiving_channel:
        async for value in receiving_channel:
            print(f"Got value {value}")


async def main() -> None:
    async with trio.open_nursery() as nursery:
        sending_channel, receiving_channel = trio.open_memory_channel(0)
        nursery.start_soon(producer, sending_channel)
        nursery.start_soon(consumer, receiving_channel)


trio.run(main)
