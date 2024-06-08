"""/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */"""

def print_callback(result):
    print(f"The result is {result}")

def calculate_sum(x, y, callback):
    result = x + y
    callback(result)

calculate_sum(5, 3, print_callback)  # Output: The result is 8



class CallbackClass:
    def __init__(self):
        self.value = 0

    def update_value(self, new_value):
        self.value = new_value
        print(f"Value updated to {self.value}")


def add_values(x: int, y: int, callback: CallbackClass):
    result = x + y
    callback.update_value(result)

callback_instance = CallbackClass()
add_values(10, 20, callback_instance)  # Output: Value updated to 30



# extra #
import asyncio
from random import randint


def pedido_confirmado(pedido: str) -> str:
    print(f'El pedido ha sido confirmado, su plato es {pedido}')

def pedido_listo(pedido: str) -> str:
    print(f'Su pedido con su plato {pedido} ya se encuentra listo.')

def entregar_pedido(pedido: str) -> str:
    print(f'Su pedido con su plato {pedido} ha sido entregado, !Que lo disfrutes!')


async def pedidos(plato: str, confirmacion: pedido_confirmado, listo: pedido_listo, entrega: entregar_pedido):
    numero_aleatorio = randint(1, 10)
    confirmacion(plato)
    await asyncio.sleep(numero_aleatorio) 
    numero_aleatorio = randint(1, 10)
    listo(plato)
    await asyncio.sleep(numero_aleatorio)
    numero_aleatorio = randint(1, 10)
    entrega(plato)

asyncio.run(pedidos('pasta', pedido_confirmado, pedido_listo, entregar_pedido))
asyncio.run(pedidos('tarta', pedido_confirmado, pedido_listo, entregar_pedido))
asyncio.run(pedidos('sancocho', pedido_confirmado, pedido_listo, entregar_pedido))
asyncio.run(pedidos('arroz con pollo', pedido_confirmado, pedido_listo, entregar_pedido))


