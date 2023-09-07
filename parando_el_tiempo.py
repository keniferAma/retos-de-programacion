"""/*
 * Crea una función que sume 2 números y retorne su resultado pasados
 * unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que
 *   debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
 *   asíncrona, es decir, sin detener la ejecución del programa principal.
 *   Se podría ejecutar varias veces al mismo tiempo.
 */"""


from datetime import datetime, timedelta, time


def tiempo(n1: int, n2: int, seconds: int):
    suma = n1 + n2
    time_added = datetime.now() + timedelta(seconds=seconds)
    seconds_added = str(time_added)[17:19]

    while True:
        time_now = datetime.now()
        second_now = str(time_now)[17:19] 
        if second_now == seconds_added:
            return suma
        


print(tiempo(2, 20, 2))



## CODE MADE BY ARTIFICIAL INTELIGENCE:

import asyncio

async def async_sum(n1: int, n2: int, seconds: int) -> int:
    await asyncio.sleep(seconds)
    return n1 + n2


async def main():
    result = await async_sum(2, 3, 5)
    print(result)

asyncio.run(main())





