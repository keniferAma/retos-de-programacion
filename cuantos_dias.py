"""/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 */"""


import re
from datetime import date

entrance1 = "12/04/1997"
entrance2 = "12/04/1998"
def contador_de_dias(string1, string2):
    pattern = r"[0-9]{2}/[0-9]{2}/[0-9]{4}"
    correct_format_1 = re.match(pattern, string1)
    correct_format_2 = re.match(pattern, string2)
    if not correct_format_1:
        return "the first format is wrong."
    if not correct_format_2:
        return "the second format is wrong."
    
    str1_day = string1[0:2]
    str1_month = string1[3:5]
    str1_year = string1[6:]

    str2_day = string2[0:2]
    str2_month = string2[3:5]
    str2_year = string2[6:]

    result = str(date(day=int(str1_day), month=int(str1_month), year=int(str1_year)) -
               date(day=int(str2_day), month=int(str2_month), year=int(str2_year)))
    if result[0] == "-":
        return f"{result[1:result.find(',')]} of difference between both dates."
    else:
        return f"{result[:result.find(',')]} of difference between both dates."
    # as curiosity, the result from operations in date, datetime are in days. That was an advantage.
    
print(contador_de_dias(entrance1, entrance2))
        



