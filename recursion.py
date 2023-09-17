def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

print(factorial(3))


"""Llamamos a factorial(3). Como 3 no es igual a 0, calculamos 3 * factorial(2). Pero para calcular eso, 
primero necesitamos el resultado de factorial(2), así que ponemos en pausa la ejecución de factorial(3) 
y pasamos a calcular factorial(2).

Llamamos a factorial(2). Como 2 no es igual a 0, calculamos 2 * factorial(1). Pero para calcular eso, 
primero necesitamos el resultado de factorial(1), así que ponemos en pausa la ejecución de factorial(2)
 y pasamos a calcular factorial(1).

Llamamos a factorial(1). Como 1 no es igual a 0, calculamos 1 * factorial(0). Pero para calcular eso, 
primero necesitamos el resultado de factorial(0), así que ponemos en pausa la ejecución de factorial(1)
 y pasamos a calcular factorial(0).

Llamamos a factorial(0). Como 0 es igual a 0, retornamos 1. No hay más llamadas a factorial que hacer, 
así que podemos empezar a resolver las operaciones que habíamos dejado en pausa.

Volvemos a la ejecución de factorial(1), que estaba calculando 1 * factorial(0). Ahora que ya sabemos que 
factorial(0) es igual a 1, podemos terminar el cálculo: 1 * 1 = 1. Retornamos ese valor.

Volvemos a la ejecución de factorial(2), que estaba calculando 2 * factorial(1). Ahora que ya sabemos que 
factorial(1) es igual a 1, podemos terminar el cálculo: 2 * 1 = 2. Retornamos ese valor.

Finalmente, volvemos a la ejecución de factorial(3), que estaba calculando 3 * factorial(2). Ahora que ya 
sabemos que factorial(2) es igual a 2, podemos terminar el cálculo: 3 * 2 = 6. Retornamos ese valor.

Así, obtenemos que el factorial de 3 es igual a 6."""

# EN ESTE CASO NO ES POSIBLE QUE SE PRODUZCA UN BUCLE INFINITO AL MOMENTO DE SALIR LA ÚLTIMA FUNCIÓN DE LA PILA DE
# EJECUCION, DEBIDO A QUE ESTA ULTIMA FUNCION NO HACE AUTOLLAMADO, Y AL SER ASI, SE DETIENE LA RECURSIVIDAD, DEJANDO
# SALIR CADA UNA DE LAS FUNCIONES CON SUS RESPECTIVAS VARIABLES.



# vamos a intentar hacer un ejercicio de recursividad contando las páginas de los libros en una lista.



libros = [60, 78, 34, 129, 37, 229]

# de la manera mas tradicional lo que haríamos es un simple bucle for que me recorra toda la lista

conteo_de_libros_mediante_bucle = 0
for l in libros:
    conteo_de_libros_mediante_bucle += l

print(conteo_de_libros_mediante_bucle)


# Ahora vamos a hacerlo de manera recursiva:

def conteo(libro):

    if len(libro) == 1:
        return libro[0]
    
    return libro[0] + conteo(libro[1:])

libros = [60, 78, 34, 129, 37, 229]
print(conteo(libros))


