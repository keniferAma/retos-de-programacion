"""/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */"""


cadena_1 = "hola como vas"
cadena_2 = "soy alejandro"


def eliminador_de_caracteres(str1, str2):
    salida_1 = ""
    salida_2 = ""

    for caracter in str1:
        if not caracter in str2:
            salida_1 += salida_1.join(caracter)

    for caracter in str2:
        if not caracter in str1:
            salida_2 += salida_2.join(caracter)

    return f"{salida_1, salida_2}"


print(eliminador_de_caracteres(cadena_1, cadena_2))







