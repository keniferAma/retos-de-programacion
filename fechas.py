"""/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */"""


import datetime


actual_datetime = datetime.datetime.now()
print(actual_datetime)


my_birth_datetime = datetime.datetime(year=1993, month=4, day=8, hour=15, minute=23, second=2, microsecond=123)
print(my_birth_datetime)


difference = actual_datetime - my_birth_datetime
age = difference.days / 365.25
print(age)
"""30.99794661190965"""

print(my_birth_datetime.weekday())
print(my_birth_datetime.date())
print(my_birth_datetime.isoweekday())
print(my_birth_datetime.weekday())
print(my_birth_datetime.day)
print(my_birth_datetime.hour)
print(my_birth_datetime.minute)
print(my_birth_datetime.second)
print(my_birth_datetime.month)
