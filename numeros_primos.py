#primo o no primo:
def iterador_de_primos(n_inicio, n_fin):
    for n in range(n_inicio, n_fin):
        if (n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0
         or n == 2 or n == 3 or n == 5 or n == 7):
            print(n) # dato curioso, no me muestra la ieracion poniendo "return" aqui y 
            # "print" en el llamado a la funcion. ESTO SE DEBE A QUE RETURN NOS FINALIZA LA FUNCIÓN.
            

def es_primo(numero):
    if (numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0
         or numero == 2 or numero == 3 or numero == 5 or numero == 7):
        print("es primo")     
    else:
        print("no es primo")

es_primo(4)

#By Brais:

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

print(is_prime(20))








    