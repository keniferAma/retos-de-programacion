"""/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */"""


import re

def url_params(url: str) -> list:
    pattern = r"=[0-9]{1,}"
    result = re.findall(pattern, url)

    return [r[1:] for r in result]


print(url_params("https://retosdeprogramacion.com?year=2023&challenge=9"))