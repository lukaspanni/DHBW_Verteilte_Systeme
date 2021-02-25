import aiohttp
import asyncio
import json


api_endpoint = "https://pokeapi.co/api/v2/pokemon/"


async def get_pokemon(session: aiohttp.ClientSession, name):
    async with session.get(api_endpoint + name) as response:
        if response.status == 404:
            print("Pokemon not found, try again")

        html = await response.text()
        try:
            pokemon_object = json.loads(html)
        except Exception:
            return
        print("Abilities:")
        for ability in pokemon_object["abilities"]:
            if not ability["is_hidden"]:
                print("\tAbility:", ability["ability"]["name"], "\n\t\tMore Info: ", ability["ability"]["url"])
        print("Base Experience", pokemon_object["base_experience"])
        print("Height", pokemon_object["height"])
        print("First 10 Moves")
        for move in pokemon_object["moves"][:10]:
            print("\tMove:", move["move"]["name"], "\n\t\tMore Info", move["move"]["url"])


async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            name = input("Enter pokemon name: ")
            if name == "":
                break
            await get_pokemon(session, name)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
