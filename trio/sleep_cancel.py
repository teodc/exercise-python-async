import trio


async def message(sleep_for: int) -> None:
    with trio.move_on_after(3) as status:
        print(f"Sleeping for {sleep_for}s")
        await trio.sleep(sleep_for)
        print(f"Slept for {sleep_for}s")
    if status.cancelled_caught:
        print("Cancelled")


async def main() -> None:
    print("Starting...")
    async with trio.open_nursery() as nursery:
        for n in range(1, 6):
            nursery.start_soon(message, n)
    print("Done")


trio.run(main)
