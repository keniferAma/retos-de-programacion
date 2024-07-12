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
