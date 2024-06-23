"""/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */"""


# filter #
def function(numero: int) -> list:
    return numero % 2 == 0


filter_lambda = list(filter(lambda n: n % 2 == 0, range(1, 20)))
filter_function = list(filter(function, range(1, 20))) # with function

print(filter_lambda)
"""[2, 4, 6, 8, 10, 12, 14, 16, 18]"""
print(filter_function)
"""[2, 4, 6, 8, 10, 12, 14, 16, 18]"""


# map #
map_lambda = list(map(lambda n: n % 2 == 0, range(1, 20)))
map_function = list(map(function, range(1, 20)))

print(map_lambda)
print(map_function)
"""[False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False]"""


# reduce #
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce((lambda x, y: x * y), range(1, 20))
print(product)  # Output: 120


def reduce_function(n1, n2) -> int:
    return n1 * n2

reduce_result = reduce(reduce_function, range(1, 20))

print(reduce_result)
"""121645100408832000"""


# extra challenge #

estudiantes = {
    'alejandro': {
        'calificaciones':{
            'matematicas': 6.0,
            'ingles': 2.9,
            'sociales': 4.3,
            'filosofia': 4.8
            },
        'fecha de nacimiento': '12/14/2000'
    },
    'felipe': {
        'calificaciones':{
            'matematicas': 9.0,
            'ingles': 2.0,
            'sociales': 5.3,
            'filosofia': 1.8
            },
        'fecha de nacimiento': '12/22/1993'
    },
    'carlos': {
        'calificaciones':{
            'matematicas': 9.0,
            'ingles': 8.9,
            'sociales': 6.3,
            'filosofia': 7.8
            },
        'fecha de nacimiento': '11/30/1987'
    },
    'fernando': {
        'calificaciones':{
            'matematicas': 6.0,
            'ingles': 9.8,
            'sociales': 2.3,
            'filosofia': 4.2
            },
        'fecha de nacimiento': '02/10/2003'
    },
}


def puntajes(estudiante: str):
    puntaje = []
    for key, value in estudiantes[estudiante]['calificaciones'].items():
        puntaje.append(value)

    resultado = reduce(lambda v1, v2: v1 + v2, puntaje) / len(puntaje)
    return resultado


def promedio(diccionario: dict):
    for estudiante in diccionario:
        promedio_calificaciones = puntajes(estudiante)
        print(f'{estudiante}, promedio de sus materias: {promedio_calificaciones}')


promedio(estudiantes)


# opcion de copilot para el primer punto #

# Algo para destacar con respecto al mio, es que en la funcion 'promedio' estamos usando la clave, valor 
# del diccionario en cuestion.

def promedio_calificaciones(estudiante: dict) -> float:
    calificaciones = estudiante['calificaciones'].values()
    return sum(calificaciones) / len(calificaciones)

def promedio(diccionario: dict):
    for nombre, estudiante in diccionario.items():
        promedio_estudiante = promedio_calificaciones(estudiante)
        print(f'{nombre}, promedio de sus materias: {promedio_estudiante:.2f}')

# promedio(estudiantes)

