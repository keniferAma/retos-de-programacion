"""/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */"""


def retroceso(n):
    if n == 0:
        return 0
    print(n)
    return retroceso(n - 1)


print(retroceso(100))



# factorial #

def factorial(n):
    if n == 1:
        return 1
    print(n)
    return factorial(n - 1) * n


print(factorial(6))
