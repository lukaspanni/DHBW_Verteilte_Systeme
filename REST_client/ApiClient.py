import aiohttp
import asyncio
import json


class ApiClient:

    def __init__(self, endpoint=None):
        self.api_endpoint = "https://pokeapi.co/api/v2/pokemon/" if endpoint is None else endpoint

    async def get_pokemon(self, name):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_endpoint + name) as response:
                if response.status == 404:
                    print("Pokemon not found, try again")

                html = await response.text()
                try:
                    pokemon_object = json.loads(html)
                    return pokemon_object
                except Exception:
                    return None
