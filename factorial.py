"""/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */"""

def factorial(numero):
    resultado = 1
    for valor in range(1, numero + 1):
        resultado *= valor
        
    return resultado

print(factorial(5))