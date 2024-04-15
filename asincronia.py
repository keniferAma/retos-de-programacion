"""/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 */"""


# Exercise #
import asyncio

async def sumar(number1, number2):
    print(f'executing "sumar" function {number1} + {number2}...')
    print('This will take 3 seconds.')
    await asyncio.sleep(3)
    print(f'Result = {number1 + number2}')
    return 'Operation finished.'

def main():
    return asyncio.run(sumar(1, 2))


#print(main())


# exercise IA version #

import asyncio
import time

async def delay_func(name, delay):
    print(f'Starting function "{name}"...')
    print(f'This will take {delay} seconds.')
    start_time = time.time()
    await asyncio.sleep(delay)
    end_time = time.time()
    print(f'Function "{name}" finished. Start time: {start_time}, End time: {end_time}')

def main():
    return asyncio.run(delay_func("delay", 3))

#print(main())



# extra challenge #


async def delay_function(name, delay):
    print(f'Starting function "{name}"...')
    print(f'This will take {delay} seconds.')
    start_time = time.time()
    await asyncio.sleep(delay)
    end_time = time.time()
    print(f'Function "{name}" finished. Start time: {start_time}, End time: {end_time}')
    return end_time - start_time



async def main():
    await asyncio.gather( # The 'await' force this 'gather' function to finishes to continue the function process
        delay_function('function A', 1),
        delay_function('function B', 2),
        delay_function('function C', 3),
    )
        
    return await delay_function('function D', 1)    


if __name__ == '__main__':
    print(asyncio.run(main()))
    