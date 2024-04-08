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
print(my_birth_datetime.strftime('%A'))  # Day of the week
print(my_birth_datetime.strftime('%B'))  # Month name
print(my_birth_datetime.strftime("%b")) 
"""Apr"""


"""%a: Weekday as locale’s abbreviated name. (e.g., Sun, Mon)
%A: Weekday as locale’s full name. (e.g., Sunday, Monday)
%w: Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
%d: Day of the month as a zero-padded decimal number. (e.g., 01, 02)
%b: Month as locale’s abbreviated name. (e.g., Jan, Feb)
%B: Month as locale’s full name. (e.g., January, February)
%m: Month as a zero-padded decimal number. (e.g., 01, 02)
%y: Year without century as a zero-padded decimal number. (e.g., 13 for 2013)
%Y: Year with century as a decimal number. (e.g., 2013)
%H: Hour (24-hour clock) as a zero-padded decimal number. (e.g., 07)
%I: Hour (12-hour clock) as a zero-padded decimal number. (e.g., 07)
%p: Locale’s equivalent of either AM or PM.
%M: Minute as a zero-padded decimal number. (e.g., 06)
%S: Second as a zero-padded decimal number. (e.g., 05)
%f: Microsecond as a decimal number, zero-padded to 6 digits.
%z: UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
%Z: Time zone name (empty string if the object is naive).
%j: Day of the year as a zero-padded decimal number.
%U: Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
%W: Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.
%c: Locale’s appropriate date and time representation.
%x: Locale’s appropriate date representation.
%X: Locale’s appropriate time representation.
%%: A literal ‘%’ character1."""