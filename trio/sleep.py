import trio


async def message(sleep_for: int) -> None:
    print(f"Sleeping for {sleep_for}s")
    await trio.sleep(sleep_for)
    print(f"Slept for {sleep_for}s")


async def main() -> None:
    print("Starting...")
    async with trio.open_nursery() as nursery:
        for n in range(1, 6):
            nursery.start_soon(message, n)
    print("Done")


trio.run(main)
