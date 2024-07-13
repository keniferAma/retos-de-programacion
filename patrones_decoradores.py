"""/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */"""


import time
from typing import Callable

def time_counter(function: Callable[[int], None]) -> Callable[[int], None]:
    # Callable: (functions, classes, callables) FIRST VALUE THE CALLABLE TYPE AND SECOND THE CALLABLE RETURN
    # On our case, the Callable receives an int type and returns None, same for the returns.

    def wrap_function(limit: int) -> None: # In our specific case we're using the exact parameter instead of
                                           # *args and **kwargs which gives us advantages but also const
                                           # such as confuse the user if the paramter needs the exact type 
                                           # In case where we espect any value *args and **kwargs would be better 
        start = time.time()
        function(limit)
        finish = time.time()
        print(f'The function took {finish - start} seconds to execute')

    return wrap_function

    
@time_counter
def print_numbers(limit: int) -> None:
    for n in range(limit + 1):
        print(n)

print_numbers(100000)