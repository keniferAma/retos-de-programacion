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


