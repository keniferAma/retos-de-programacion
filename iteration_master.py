"""/*
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
 */"""

def iterator_range():
    for n in range(101):
        print(n)

def iterator_add():
    numeros = [1]
    for n in numeros:
        numeros.append(n + 1)
        print(n)
        if n == 100:
            break

def iterator_while():
    numbers = 0
    while numbers <= 99:
        numbers += 1
        print(numbers)








    
    