"""/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */"""

from datetime import date


def viernes_13(*, year: int, month: int):
    date_info = date(year=year, month=month, day=13)
    weekday = date.weekday(date_info)

    if weekday == 4:
        return True
    else:
        return False
    
print(viernes_13(year=2023, month=1))