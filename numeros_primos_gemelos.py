"""/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */"""



def is_prime(n):
    primes = []
    for number in range(2, n):
        is_divisible = False
        for index in range(2, number):
            if number % index == 0:
                is_divisible = True
        if not is_divisible:
            primes.append(number)
    return primes


def pairs(primes: list):
    result = []
    
    for i in range(1, len(primes)):
        if primes[i] - primes[i - 1]  == 2:
            result.append(str((primes[i - 1], primes[i])))

    return ", ".join(result)


print(pairs(is_prime(1000)))
