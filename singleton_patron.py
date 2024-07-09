"""/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */"""

# metodo comun hecho en java #
class MyClass:
    __instance = None

    @staticmethod
    def __new__(cls):
        if MyClass.__instance is None:
            print('nueva instancia')
            MyClass.__instance = object.__new__(cls)

        return MyClass.__instance
    
user1 = MyClass()
user2 = MyClass()

print(user1 is user2)
"""True""" # Podemos ver que cada instancia es la misma



# Probando con una clase regular #

class RegularClass:
    pass

user3 = RegularClass()
user4 = RegularClass()

print(user3 is user4)
"""False""" # podemos ver que cada instancia es diferente



class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @classmethod
    def ret(cls):
        return cls(name='kenifer', surname='amariles')
    
kenifer = User('alejandro', 'fernandez')



# METODO PYTHONICO #

def singleton(cls):
    instances = dict() # Simple diccionario para guardar la primera instancia.
    # En nuestro caso seria: 'instances = {"Prueba": Prueba("kenifer", 3)} y desde la primera instancia
    # siempre nos va a retornar estos valores.

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs) # Basicamente creando una clave-valor con el nombre
            # de la clase como key y 

        return instances[cls]
    
    return wrap


@singleton
class Prueba:
    def __init__(self, username, age):
        self.username = username
        self.age = age


instancia1 = Prueba('kenifer', 3)
instancia2 = Prueba('alberto', 2)
instancia3 = Prueba('ximena', 31)
instancia4 = Prueba('fabio', 23)
instancia5 = Prueba('gerardo', 13)


print(instancia1 is instancia3)
"""True"""
print(instancia3.username) # Intentamos ejecutar el nombre de la instancia3, el cual es 'ximena'.
"""Kenifer""" # Como podemos ver, aunque la instancia deberia ser 'ximena', tenemos 'kenifer', la primera.


# parentesis con las bases de FUNCIONES COMO DECORADORES #
################################################################
import time

def tiempo_empleado(funcion):

    def funcion_modificada(n): # basicamente esta funcion reemplazaria 'contador'
        inicio = time.time()
        funcion(n)
        fin = time.time()
        print(fin - inicio)

    return funcion_modificada


@tiempo_empleado
def contador(n): # Esta funcion entraria como argumento a 'tiempo_empleador'
    for i in range(n):
        print(i)

################################################################



class Una:
    def __init__(self, name, age):
        self.name = name
        self.age = age

diccionario = {}

diccionario[Una] = Una('alejandra', 30)


print(diccionario)



################################################################

# Otro parentesis con non-keyword arguments y keyword arguments #
def non_keyword_function(*args):
    print(args)

non_keyword_function('carlos', 'balon', 20)
"""('carlos', 'balon', 20)""" # Pasamos los argumentos que deseemos en non-keyword, nos retorna tupla


# Keyword #
def keyword_function(**kwargs):
    print(kwargs)

keyword_function(name='alejandro', age=30, surname='amariles')
"""{'name': 'alejandro', 'age': 30, 'surname': 'amariles'}""" # Nos retorna un diccionario.
################################################################



@singleton
class NoAttributes:
    def __init__(self) -> None:
        pass

instancia6 = NoAttributes()
instancia7 = NoAttributes()

print(instancia6 is instancia7)

