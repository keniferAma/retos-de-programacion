"""/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */"""

import re

string = 'ase2sor93i0a d1e personas'
pattern = r'[0-9]'
string_only = r'[a-zA-Z\s]{1,}'

concurrences = re.findall(pattern, string)
string_concurrences = re.findall(string_only, string)

print(concurrences)
print(string_concurrences)
print(''.join(string_concurrences))

