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



# artificial version #

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    primes_only = [p for p in range(2, n) if primes[p]]
    return primes_only

def prime_pairs(primes):
    return [(primes[i], primes[i+1]) for i in range(len(primes)-1) if primes[i+1] - primes[i] == 2]

print(prime_pairs(sieve_of_eratosthenes(1000)))

