"""/*
 * Enunciado: Crea un función que reciba un texto y retorne la vocal que
 * más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío. 
 */"""

import re

def vocal_repeated(string: str) -> str:
    pattern_a = r"[Aaá]"
    pattern_e = r"[Eeé]"
    pattern_i = r"[Iií]"
    pattern_o = r"[Ooó]"
    pattern_u = r"[Uuú]"

    a = re.findall(pattern_a, string)
    e = re.findall(pattern_e, string)
    i = re.findall(pattern_i, string)
    o = re.findall(pattern_o, string)
    u = re.findall(pattern_u, string)
    
    result = sorted([len(a), len(e), len(i), len(o), len(u)])
    output = ""

    if len(a) == result[-1]:
        output += "a" + ","
    if len(e) == result[-1]:
        output += "e" + ","
    if len(i) == result[-1]:
        output += "i" + ","
    if len(o) == result[-1]:
        output += "o" + ","
    if len(u) == result[-1]:
        output += "u" + ","
    
    return output[:-1]

string = "aberlardoAiii"
print(vocal_repeated(string))


# Ahora vamos a pegar la version hecha por la inteligencia artificial:

import re

def vocal_repeated(string: str) -> str:
    # Definir las vocales y sus patrones
    vocales = {'a': r"[Aaá]", 'e': r"[Eeé]", 'i': r"[Iií]", 'o': r"[Ooó]", 'u': r"[Uuú]"}
    
    # Inicializar un diccionario para almacenar los conteos
    conteos = {vocal: 0 for vocal in vocales}
    
    # Contar las ocurrencias de cada vocal
    for vocal, patron in vocales.items():
        conteos[vocal] = len(re.findall(patron, string))
    
    # Encontrar la vocal con el mayor conteo
    max_conteo = max(conteos.values()) # Interesante el uso de "max". Para tenerlo en cuenta.
    vocales_maximas = [vocal for vocal, conteo in conteos.items() if conteo == max_conteo]
    
    return ','.join(vocales_maximas)








