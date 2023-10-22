"""/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */"""

def fibonacci(n):
    if n <= 0:
        return "El número ingresado debe ser mayor que cero"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(5))

# HORA VAMOS A PROCEDER A TRATAR DE EXPLICAR PASO A PASO LA RECURSIVIDAD EN FIBONACCI:

#-> Asignamos un valor que queremos buscar. En nuestro caso vamos a usar 5
#-> Luego ese 5 ingresa al stack, esperando que resolvamos, primero que todo "fibonacci(n-1)", por consiguiente
# se realizar la respectiva resta solamente en esta primera recursividad. fibonacci(n-2) espera.
#-> Luego seguimos así consecutivamente hasta que llegamos a nuestro caso base de la primera recursividad, el cual 
# es 2.
#-> Una vez llegamos a este caso, nos retorna 1, por una de las condicionales.
#-> Ya habiendo obtenido este valor, necesitamos resolver su pareja de suma, es decir fibonacci(n-2), el cual 
# en nuestro caso sería 1, debido a que estamos en el stack 3 (o llamada 3 o fibonacci(3)).
#-> Esta llamada de fibonacci(1) nos retorna 0, por consiguiente ya tenemos nuestra suma en fibonacci(3) lista
# para ser ejecutada. La ejecutamos y esos van a ser sus respectivos valores mientras sacamos las demás funciones
# del stack.
#-> Ahora vamos a ejecutar la siguiente recursividad, es decir la de fibonacci(4) que en fibonacci(n-1) nos da 3
# y por fibonacci(n-2) nos da 2.
#-> Ingresamos a la función con 3, no está en condicionales, entonces creamos de nuevo recursividad y llegamos de
# nuevo a 2, el cual nos retorna 1.
#-> Estando aquí ya teníamos el resultado de fibonacci(n-2) de este nivel de stack, el cual es 0. Sumamos y ese es 
# el resultado de nuestro nivel fibonacci(4): 1.
#-> ya tenemos 1 en nuestro fibonacci(n-1), intentamos sumar con su compañero el cual es 2 (debido a que estamos
# en el stack 4 y su funcion recursiva en fibonacci(n-2)), y nos retorna 1, por una de sus condicionales.
# Sumamos este nivel y nos da 2. (debemos estar atentos los resultados previos individuales, ya que en este tipo de
# recursividades tenemos que estar recurriendo bien sea a una o a la otra).
# Ejecutamos nuestro base del stack, el cual es 4 para fibonacci(n-1). Operamos y debemos crear una nueva recursion.
#-> En esta nueva recursion llegamos a 2, donde nos retorna 1 y sumamos con su recursion compañera, la cual
# previamente teníamos en 0 y 1, y su resultado, que es igual a 2 sería el resultado de la base de nuestro stack 
# para la primera recursividad.
#-> Debemos continuar con nuestra recursividad compañera de nuestra base, la cual es 3 para fibonacci(n-2) la cual
# nos retorna por una de sus condicionales 1 y sumamos con su primera recursividad, lo cual nos da un resultado
# de 3. Este sería nuestro resultado final para la secuencia #5 de la secuencia de fibonacci.  
# PARA TENER BIEN EN CUENTA: SIEMPRE EN CADA STACK, SE CONSERVAN SUS ARGUMENTOS LOCALES Y SU CANTIDAD DE 
# RECURSIVIDADES. QUEDAN ESTÁTICOS HASTA LA ESPERA DE SU TURNO Y SU CONSGUIENTE SALIDA.



def prime(number: int) -> bool:
    output = True
    for i in range(2, number):
        if number % i == 0:
            output = False

    return output


def par(number: int) -> bool:
    
    if number % 2 == 0:
        return True
    else:
        return False

    

def main(num: int):
    if (fibonacci(num) == num and
        prime(num) and par(num)):
        return f"{num} is fibonacci, prime and par" 
    
    elif (fibonacci(num) != num and
        prime(num) and par(num)):
        return f"{num} is prime, par and not fibonacci"

    elif (fibonacci(num) != num and
        not prime(num) and par(num)):
        return f"{num} is not fibonacci, not prime and par" 
    
    elif (fibonacci(num) == num and
        not prime(num) and par(num)):
        return f"{num} is fibonacci, not prime and par"
    
    elif (fibonacci(num) != num and
        not prime(num) and not par(num)):
        return f"{num} is not fibonacci, not prime and impar"

    elif (fibonacci(num) != num and
        prime(num) and not par(num)):
        return f"{num} is not fibonacci, prime and impar"
    
print(main(7)) 