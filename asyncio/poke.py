import asyncio
import requests
from time import perf_counter
from random import randint

MAX_ID = 300
API_URL = "https://pokeapi.co/api/v2/pokemon"


def http_get_sync(url: str):
    response = requests.get(url)
    return response.json()


async def http_get_async(url: str):
    return await asyncio.to_thread(http_get_sync, url)


def get_random_pokemon_sync() -> str:
    url = f"{API_URL}/{randint(1, MAX_ID)}"
    pokemon = http_get_sync(url)
    return pokemon["name"]


async def get_random_pokemon_async() -> str:
    url = f"{API_URL}/{randint(1, MAX_ID)}"
    pokemon = await http_get_async(url)
    return pokemon["name"]


async def main() -> None:
    # sync
    print("--- Start sync")
    before = perf_counter()
    result = [get_random_pokemon_sync() for _ in range(20)]
    print(result)
    after = perf_counter()
    print(f"--- Time (sync): {after - before}")

    # async
    print("--- Start async")
    before = perf_counter()
    result = await asyncio.gather(*[get_random_pokemon_async() for _ in range(20)])
    print(result)
    after = perf_counter()
    print(f"--- Time (async): {after - before}")


asyncio.run(main())
