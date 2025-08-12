class ContextManagerExample:
    def __init__(self, content: str) -> None:
        self.content = content

    def __enter__(self):
        print("context manager initilized")
        return self.content

    def __exit__(self, exc_type, exc_val, exc_tb): # El resto de parametros son con fines de atrapar posible excepciones. (parametros necesarios)
        print("context manager closed")


with ContextManagerExample('my file') as context:
    print(context)

"""
context manager initilized
my file
context manager closed
"""

# Basicamente esto es lo que pasa tras bambalinas cuando usamos 'with',
# con el que basicamente estamos creando un context manager.


from contextlib import asynccontextmanager
from asyncio import sleep
import asyncio

@asynccontextmanager
async def context_function(input_message: str, end_message: str, time_between: float):
    print(input_message)
    await sleep(time_between)
    yield 
    print(end_message)


async def prueba():
    async with context_function("hello", "bye", 3.2) as context_f:
        print(context_f)

asyncio.run(prueba())

