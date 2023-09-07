"""/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información 
 * al respecto.
 */"""


# def numero_armstrong(numero):
#     resultado = 0
#     cantidad_de_numeros = len(numero)
#     for valor in numero:
#         resultado += valor ** cantidad_de_numeros


#     return resultado


# print(numero_armstrong(str(5)))


def numero_armstrong(numero):
    resultado = 0
    cantidad_de_numeros = len(numero)
    for valor in range(0, cantidad_de_numeros):
        resultado += int(numero[valor]) ** cantidad_de_numeros


    if resultado == int(numero):
        return f"{resultado} es un numero armstrong"
    else:
        return f"{resultado} no es un numero armstrong"



print(numero_armstrong(str(1634)))
