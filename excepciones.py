"""/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 */"""

# excepcion #


try:
    result = 10/0

except ZeroDivisionError as message:
    print(message)


try:
    result = 'r'/ 3

except TypeError as message:
    print(message)


try:
    integers = 12345
    print(integers[2])

except TypeError as message:
    print(message)


try:
    lista = [1, 2, 3, 4, 5]
    print(lista[20])

except IndexError as message:
    print(message)



# extra #
    
class MyCustomException(Exception):
    """Making a custom class to raise exceptions"""
    def __init__(self, message):
        super().__init__(message) # inherits *args, from Exception which is a tuple with the information
        self.message = message
        
    def __repr__(self):
        return self.message


dictionary = {'name': 'alberto', 'surname': 'velez', 'age': 23, 'country': 'United States', 
              'more': {'employee': 'yes', 'credit card': 'yes'}
              }


def Example_function(dictionary: dict, index: str):
    if not isinstance(dictionary, dict):
        raise TypeError('TypeError')    
    
    if not index in dictionary:
        raise MyCustomException('The index name is not in the dictionary')
    
    else:
        print(dictionary[index])


try:
   Example_function(dictionary=dictionary, index='more')

except (MyCustomException, TypeError) as message: 
    print(message.args[0]) # accesing to the *args tuple
else:
    print('No errors') # If the except is false, then will print this else.
finally:
    print('Execution has finished.') # Prints yes or yes.







