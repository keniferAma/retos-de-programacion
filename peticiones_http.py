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