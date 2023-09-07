"""/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */"""

palabra_1 = "hola como estas"
palabra_2 = "hola.como estas"




### RETO HECHO POR MÍ:

# def infiltrado(palabra1, palabra2):
#     if len(palabra1) == len(palabra2):
#         resultado = []
#         seleccion = list(map(lambda p_1, p_2: p_1 == p_2, palabra_1, palabra_2))

#         if palabra1 == palabra2:
#             return "Ambas palabras son las mismas"

#         for p, l in enumerate(seleccion):
#             if l == False:
#                 resultado.append(palabra_2[p])

#         return f'Estas son los caracteres infiltrados: {resultado}'
    
#     else:
#         return "Las palabras no tienen la misma longitud"
# print(infiltrado(palabra_1, palabra_2))





## RETO HECHO POR CHATGPT:
# Algo que me pareció interesante fué usar el índice de la primera palabra para usarlo en el recorrido de la segunda
# y luego hacer la comparación. DEFINITIVAMENTE MAS CONCISO Y MENOS CÓDIGO.

def obtener_caracteres_diferentes(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        return "Las palabras no tienen la misma longitud"

    caracteres_diferentes = []
    for indice, char_palabra1 in enumerate(palabra1):
        char_palabra2 = palabra2[indice]
        if char_palabra1 != char_palabra2:
            caracteres_diferentes.append(char_palabra2)

    if not caracteres_diferentes:
        return "Ambas palabras son las mismas"

    return f'Caracteres diferentes en la segunda palabra: {caracteres_diferentes}'




        
        


    






    



        



