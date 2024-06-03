"""/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */"""


import httpx
import requests
import asyncio

url = 'https://developer.mozilla.org'

client = requests.Session()

response = client.get(url=url)

print(response.status_code)




class Client:
    def __init__(self, url: str) -> None:
        self.client = httpx.AsyncClient(base_url=url)


    async def fetch_cors_information(self):
        response = await self.client.get('/en-US/docs/Web/HTTP/CORS#what_requests_use_cors')
        print(response.status_code)

    async def fetch_authentication(self):
        response = await self.client.get('/en-US/docs/Web/HTTP/Authentication')
        print(response.status_code)


default_client = Client(url)


async def main():
    await asyncio.gather( # gather must be AWAITED.
        default_client.fetch_authentication(),
        default_client.fetch_cors_information()
    )

asyncio.run(main())



# Extra challenge #
import httpx

class PokemonException(Exception):
    """Exception raised for errors in the Pokemon API."""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.args = args

    def __repr__(self):
        return self.args


def find_key(nested_dict: dict, target_key: str, found_values=None):
    if found_values is None:
        found_values = []
    if isinstance(nested_dict, dict):
        for key, value in nested_dict.items():
            if key == target_key:
                found_values.append(value)
            elif isinstance(value, (dict, list)):
                find_key(value, target_key, found_values)
    elif isinstance(nested_dict, list):
        for item in nested_dict:
            if isinstance(item, (dict, list)):
                find_key(item, target_key, found_values)
    return found_values



class PokeClient:
    def __init__(self, base_url: str) -> None:
        self.client = httpx.AsyncClient(base_url=base_url)

    async def fetch(self, pokemon_name: str):

        response = await self.client.get(url=f'/api/v2/pokemon/{pokemon_name}')
        if response.status_code == 404:
            raise PokemonException('Pokemon name not found.') # REMEMBER FIRST RAISE THE ERROR.
        
        data = response.json()

        height = data['height']
        pokemon_id = data['id']
        weight = data['weight']

        specie_response = await self.client.get(url=f'/api/v2/pokemon-species/{pokemon_name}')
        evolution_url = specie_response.json()["evolution_chain"]["url"] # guaranting pokemon id
        evolution_response = await self.client.get(evolution_url)

        if evolution_response.status_code != 200:
            raise PokemonException('Error getting the evolution')
        
        evolution_result = find_key(evolution_response.json()["chain"], 'species')

        print(f'{pokemon_name} information: height: {height}, id: {pokemon_id}, weight: {weight}')
        print(f'Evolution chain: {' -> '.join([evolution['name'] for evolution in evolution_result[::-1]])}')


default_client = PokeClient('https://pokeapi.co')
pokemon_input = str(input('Write the pokemon name: ').lower())

try:
    asyncio.run(default_client.fetch(pokemon_input))

except PokemonException as msg:
    print(msg)



