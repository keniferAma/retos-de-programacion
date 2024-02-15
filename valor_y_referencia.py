"""/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */"""

# By Value (using immutable data type)
def updateNumber(num):
    print("id before modification inside function: ", id(num))
    num += 10
    print("id after modification inside function: ", id(num))
    return num

n = 5
print("id before modification: ", id(n))
print("Updated number: ", updateNumber(n))
print("id after modification: ", id(n))
print("Number after function call: ", n)


print('//////')

# By Reference (using mutable data type)
def updateList(myList):
    print("id before modification inside function: ", id(myList))
    myList.append([1, 2, 3, 4])
    print("id after modification inside function: ", id(myList))
    print("List inside function: ", myList)

lst = [10, 20, 30]
print("id before modification: ", id(lst))
updateList(lst)
print("id after modification: ", id(lst))
print("List after function call: ", lst)



# summarizing #
"""
Immutable objects (passed ‘by value’) can be thought of as ‘read-only’. You can’t make changes to the original object inside a function.
Mutable objects (passed ‘by reference’) can be thought of as ‘read-write’. You can make changes to the original object inside a function.
"""

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)
"""[10, 20, 30]
[10, 20, 30]"""

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)
"""10
20"""