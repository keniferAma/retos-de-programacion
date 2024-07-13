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

print_numbers(10)


# EXTRA #

def function_counter_v1(function: Callable[[str], str]) -> Callable:
    counter = []
    
    def wrap(*args, **kwargs) -> str:
        counter.append(function(*args, **kwargs))
        return(f'The function "{function.__name__} is repeated {len(counter)} times')
    
    return wrap
        

@function_counter_v1
def print_message_v1(message: str) -> str:
    return message

print(print_message_v1('This is my message'))
print(print_message_v1('This is my message'))
print(print_message_v1('This is my message'))



from collections import Counter
from typing import Counter

def function_counter_v2(function: Callable[[str], str]):
    counter = dict()

    def wrap(*args, **kwargs) -> dict:
        if function.__name__ not in counter:
            counter[function.__name__] = 1
        else:
            counter[function.__name__] += 1
        return counter
    
    return wrap
        
@function_counter_v2
def print_message_v2(message: str) -> str:
    return message


print(print_message_v2('This is my message'))
print(print_message_v2('This is my message'))
print(print_message_v2('This is my message'))
print(print_message_v2('This is my message'))


