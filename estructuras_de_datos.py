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




# EXTRA #
from pydantic import BaseModel, Field


db = []

class Db(BaseModel):
    name: str
    cell_number: int = Field(lt=(11))




def search(name: str):
    """searching the current users"""
    user_name = [n for n in db if n['name'] == name]
    if not user_name:
        return {'message': 'The user was not found.'}
    return db[0]

def insert(name: str, cell_phone: int):
    if not search(name=name) == {'message': 'The user was not found.'}:
        return {'message': 'The user is currently registered.'}
    
    db.append({'name': name, 'cell_number': cell_phone})
    return {'message': 'user added correctly'}




# by brais #
def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(
                        f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")


my_agenda()