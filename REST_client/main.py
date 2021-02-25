import asyncio

from REST_client.ApiClient import ApiClient

api_endpoint = "https://pokeapi.co/api/v2/pokemon/"


async def print_waiting(name):
    while True:
        print("Waiting for Response for Pokemon", name, "...")
        await asyncio.sleep(0.5)


async def main():
    client = ApiClient()
    while True:
        name = input("Enter pokemon name: ")
        if name == "":
            break
        finished, pending = await asyncio.wait([client.get_pokemon(name), print_waiting(name)],
                                               return_when=asyncio.FIRST_COMPLETED)
        pokemon = finished.pop().result()
        for task in pending:
            task.cancel()
        if pokemon is None:
            continue
        print("Abilities:")
        for ability in pokemon["abilities"]:
            if not ability["is_hidden"]:
                print("\tAbility:", ability["ability"]["name"], "\n\t\tMore Info: ", ability["ability"]["url"])
        print("Base Experience", pokemon["base_experience"])
        print("Height", pokemon["height"])
        print("First 10 Moves")
        for move in pokemon["moves"][:10]:
            print("\tMove:", move["move"]["name"], "\n\t\tMore Info", move["move"]["url"])


if __name__ == "__main__":
    asyncio.run(main())
