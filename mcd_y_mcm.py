"""/*
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que 
 *   lo resuelvan directamente.
 */"""

from numeros_primos import is_prime


def mayor(numero1, numero2):
    if numero1 > numero2:
        return numero1
    
    else:
        return numero2

def minimo_comun_multiplo(numero1: int, numero2: int) -> int:
    resultado = 1
    lista = []
    for n in is_prime((mayor(numero1, numero2))):
        while numero1 % n == 0 or numero2 % n == 0:
            match numero1 % n == 0 and numero2 % n == 0:
                case True:
                    numero1 = numero1 // n 
                    numero2 = numero2 // n 
                    lista.append(n)
                    continue

            match numero1 % n == 0:
                case True:
                    numero1 = numero1 // n 
                    numero2 = numero2
                    lista.append(n)
                    continue

            match numero2 % n == 0:
                case True:
                    numero2 = numero2 // n 
                    numero1 = numero1
                    lista.append(n)
                    continue

    while lista:
        ultimo = lista.pop()
        resultado = ultimo * resultado
    
    return resultado




def maximo_comun_divisor(numero1: int, numero2: int) -> int:
    resultado = 1
    lista = []
    for n in is_prime((mayor(numero1, numero2))):
        while numero1 % n == 0 and numero2 % n == 0:
            numero1 = numero1 // n 
            numero2 = numero2 // n 
            lista.append(n)
            continue
    
    while lista:
        ultimo = lista.pop()
        resultado = ultimo * resultado

    return resultado

print(maximo_comun_divisor(64, 34))



# Generado por inteligencia artificial.

def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

def mcm(a, b):
    return (a * b) // mcd(a, b)

a = 64
b = 34
print(f"MCD({a}, {b}) = {mcd(a, b)}")
print(f"mcm({a}, {b}) = {mcm(a, b)}")


print(12 % 20)




