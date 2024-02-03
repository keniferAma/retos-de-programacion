"""/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */"""


# lists #
my_list = ['caballo', 'vaca', 'cordero', 'perro']
print(my_list)
my_list.append('lobo')
print(my_list)
my_list[2] = 'leon'
print(my_list)
my_list.remove('perro')
print(my_list)
my_list.sort()
print(my_list)

# tuples #
my_tuple = ('carlos', 'arturo', 'fernando', 'fidel')
print(my_tuple)
#my_tuple[1] = 'alejandro' # It is not possible to modify items
sorted(my_tuple)

# dictionaries #
my_dictionary = {'nombre': 'carlos', 'apellido': 'bedoya', 'estado civil': 'casado'}
print(my_dictionary)
print(my_dictionary.values())
print(my_dictionary.keys())
my_dictionary['nombre'] = 'andres'
print(my_dictionary)
order_dict = dict(sorted(my_dictionary.items()))
print(order_dict)

# sets #
my_set: set = {'abeja', 'zancudo', 'mosca', 'mosca'} # As we can see, dict only allowed.
print(my_set)
my_set.add('pajaro')
print(my_set)
dict_to_set = {'nombre': 'abelardo', 'apellido': 'rua', 'apellido': 'fernandez'}
print(set(dict_to_set))
list_to_set = ['carmen', 'fabiola', 'susana', 'adela', 'adela', 'carmen']
print(set(list_to_set))
"""{'carmen', 'susana', 'fabiola', 'adela'}"""
# sets RETURNS DICTS.




# extra #
from pydantic import BaseModel, Field
entry = input('Describe the operation: ')

db = {}

class Db(BaseModel):
    name: str
    phone_number: int = Field(max_digits=11)


# def excecution(operation: str):
#     match operation:
#         case 'search':
#             for index,  in db.items()





