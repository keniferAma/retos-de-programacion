"""/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */"""

# for loop #
for i in range(1, 11):
    print(i)

print('///')

# while loop #
number = 1
while number < 11:
    print(number)
    number += 1

# filter iteration #
filter_result = filter(lambda n: n <= 10, range(1, 20))
print(list(filter_result))

# map iteration #
map_result = map(lambda n: n <= 10, range(1, 20))
print(list(map_result))

# yield out of iterator #
def yielding_no_iteration():
    result = 0
    for i in range(1, 10):
        
        result += i
    yield result 

yield_result = yielding_no_iteration()

print(next(yield_result))
"""45"""

# yield inside iterator #
def yielding_iteration():
    result = 0
    for i in range(1, 10):
        yield result 

        result += i
    

yield_result = yielding_iteration()

print(next(yield_result))
print(next(yield_result))
print(next(yield_result))
print(next(yield_result))
print(next(yield_result))
print(next(yield_result))
print(next(yield_result))
print(next(yield_result))
print(next(yield_result))
"""0
1
3
6
10
15
21
28
36"""

# recursividad #

def count_ten(i=1):
    if i <= 10:
        print(i)
        count_ten(i + 1)

print(count_ten())