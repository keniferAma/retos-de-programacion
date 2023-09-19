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

# Vamos a intentar traer la lógica para explicar el funcionamiento de este ejercicio de recursividad.


# En el primer guardado de la función tendremos 60 + [78, 34, 129, 37, 229] 
# ALGO MUY IMPORTANTE ES TENER EN CUENTA QUE LO QUE ESTÁ DENTRO DE LA FUNCIÓN NO ES UN RESULTADO DEFINITIVO.
# ES DECIR, NO ES EL VALOR QUE SE QUEDARA EN ESA FOTOGRAFIA.

# En el segundo guardado de la función tendremos return 78 + [34, 129, 37, 229]

# En el tercer guardado de la función tendremos return 34 + [129, 37, 229]

# En el cuarto guardado de la función tendremos return 129 + [37, 229]

# En el quinto guardado de la función tendremos return 37 + [229]

# En el sexto guardado de la funcion el condicional nos da return 229:
# es decir, que la función se transforma en 229 y sale de la pila.

# Volvemos al quinto guardado, el cual tenemos 37 + el return de 229, lo sumamos y sale la función. es decir 266.

# Volvemos al cuarto guardado, el cual tenemos return 129 + [37, 229], el return anterior nos dio 266 entonces lo sumamos
# y nos da 395 (recordar que todo esto es return)

# Volvemos al tercer guardado, el cual tenemos return 34 + [129, 37, 229], estos de la lista ya estan resueltos 
# con la funcion saliente anterior mas libro[0], que en su caso QUEDAN SI O SI EN LA FOTOGRAFIA, AL NO PERTENERCER 
# DIRECTAMENTE A LA FUNCIÓN.

# y asi nos vamos sucesivamente.



# Factorial recursivo
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))


# Fibonacci recursivo
def fibonacci(n):
    if n <= 0:
        return "El input debe ser un número entero positivo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))



# Algoritmo recursivo para sumar:
def suma(n):
    if n == 0:
        return 0
    return n + suma(n - 1)

print(suma(2))




# Ahora vamos a intentar crear un algoritmo de ordenamiento por recursividad.

lista = [2, 4, 5, 6, 1, 9, 0]

def merge_sort(lista):
    if len(lista) == 1:
        return lista
    
    division = len(lista) // 2
    lista_izquierda = lista[:division]
    lista_derecha = lista[division:]

    organizar_izquierda = merge_sort(lista_izquierda)
    organizar_derecha = merge_sort(lista_derecha)
    

    print(organizar_izquierda)
    print(organizar_derecha)

    return merge(organizar_derecha, organizar_izquierda)


def merge(l_derecha, l_izquierda):
    merge_organizado = []

    while len(l_derecha) > 0 and len(l_izquierda) > 0:
        if l_izquierda[0] > l_derecha[0]:
            merge_organizado.append(l_derecha[0])
            l_derecha.pop(0)
        else:
            merge_organizado.append(l_izquierda[0])
            l_izquierda.pop(0)

    while len(l_izquierda) > 0:
        merge_organizado.append(l_izquierda[0])
        l_izquierda.pop(0)

    while len(l_derecha) > 0:
        merge_organizado.append(l_derecha[0])
        l_derecha.pop(0)

    return merge_organizado


print(merge_sort(lista))
















