import asyncio.runners
import httpx
import asyncio
from bs4 import BeautifulSoup

from contextlib import asynccontextmanager


@asynccontextmanager
async def enjoy_videogames_default_client():
    client = httpx.AsyncClient(base_url='https://enjoyvideogames.com.co')
    try:
        yield client
    finally:
        await client.aclose()

    """tenemos esta asynccontextmanager como practica debido a que el context manager
    de httx.AsyncClient por defecto me cierra el cliente antes de que se ejecute...
    
    OJO, este cliente lo hicimos con el fin de poder reutilizarlo en otras operaciones (get, post etc)
    con fines de practicas"""


async def tiger_computadores(videocard_name: str):
    client = httpx.AsyncClient(base_url='https://tigercomputadores.com/')

    response = await client.get(
        url="/?orderby=price&paged=1&s=rtx+5070+ti&post_type=product&dgwt_wcas=11",
        timeout=10.0
    )

    soup = BeautifulSoup(markup=response.text, features='html.parser')

    product = soup.find(name='div', attrs={
            'class': 'w-vwrapper usg_vwrapper_1 align_center valign_justify'
            }
        )
    
    result = {}

    while True:

        product_name = product.find(
            name='h2',
            attrs={
                'class': 'w-post-elm'
            }
        )
        
        product_price = product.find(
            name='span',
            attrs={
                'class': 'woocommerce-Price-amount amount'
            }
        )

        if product_price is not None:
            result[product_name.get_text()] = product_price.get_text().replace('\xa0', ' ')

        product = product.find_next(name='div', attrs={
            'class': 'w-vwrapper usg_vwrapper_1 align_center valign_justify'
            }
        )

        if product is None:
            break
    
    print('Tiger computadores:')
    for product, price in result.items():
        print(f'{product_name} = {product_price}')
    


# <div class="w-vwrapper usg_vwrapper_1 align_center valign_justify"><h2 class="w-post-elm post_title usg_post_title_1 has_text_color woocommerce-loop-product__title color_link_inherit"><a href="https://tigercomputadores.com/producto/video-geforce-rtx-5070-12gb-pny-overclocked/">VIDEO GEFORCE RTX 5070 12GB PNY OVERCLOCKED</a></h2><div class="w-hwrapper usg_hwrapper_1 align_none valign_middle" style="--hwrapper-gap:1.3rem"><p class="w-post-elm product_field price usg_product_field_3 has_text_color"><del aria-hidden="true"><span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">$</span><span class="woocommerce-Price-amount amount">3.800.000&nbsp;</span></bdi></span></del> <span class="screen-reader-text">El precio original era: $3.800.000&nbsp;.</span><ins aria-hidden="true"><span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">$</span><span class="woocommerce-Price-amount amount">3.280.000&nbsp;</span></bdi></span></ins><span class="screen-reader-text">El precio actual es: $3.280.000&nbsp;.</span></p></div></div>



async def enjoy_videogames(videocard_name: str):
    async with enjoy_videogames_default_client() as client:

        if not isinstance(videocard_name, str):
            return 'Strings only allowed'
        
        videocard_name.replace(' ', '-')

        response = await client.get(
            f'/product-category/hardware/tarjetas-de-video/nvidia/?filter_tarjeta-de-video=geforce-{videocard_name}',
            timeout=10.0
        )


        soup = BeautifulSoup(markup=response.text, features='html.parser')

        product = soup.find(name='div', attrs={'class': 'product-element-bottom'})

        if product == None:
            return 'Videocard name not found'

        result = {}
        
        while True:

            product_name = product.find(
                name='h3',
                attrs={
                    'class': 'wd-entities-title'
                }
            )

            product_price = product.find(
                name='span', 
                attrs={
                    'class': 'price'
                }
            )

            product_stock = product.find(
                name='p',
                attrs={
                    'class': 'wd-style-default'
                }
            )

            if product_stock.get_text() != 'Agotado':
                result[product_name.get_text()] = product_price.get_text().replace('\xa0', ' ')

            
            product = product.find_next(
                name='div', 
                attrs={
                    'class': 'product-element-bottom'
                }
            )

            if product is None:
                break

        print('Enjoy vidogames:')
        for product_name, product_price in result.items():
            print(f'{product_name} = {product_price}') 


async def main(videocard_name: str):
    """
    No se usa 'await' antes de cada una de las funciones asincronas debido a que 'gather' las 
    ejecuta todas al mismo tiempo (por ello no son esperables...), de otro modo estariamos perdiendo 
    las ventajas del asincronismo.
    Lo que si se 'espera' es la ejecucion TOTAL de todas las operaciones dentro de 'gather'.
    """

    result = await asyncio.gather(
        enjoy_videogames(videocard_name=videocard_name),
        tiger_computadores(videocard_name=videocard_name)
    )


    
    return result


print(asyncio.run(main=main(videocard_name='rtx 5070 ti')))










