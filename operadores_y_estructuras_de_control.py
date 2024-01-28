"""/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */"""

print(1 + 1)
print(4 * 8)
print('string numero uno' + ' ' + 'string numero dos')
print(4 - 2)
print(int(23 / 2))
print(4 > 2)
print(2 == 1)
print('string_' > 'string')
print(12 >= 12)

# Operadores de asignacion #
my_assigned_number = 0
my_assigned_number -= 2
print(my_assigned_number)
my_assigned_number **= 2
print(my_assigned_number)
my_assigned_number += 20
print(my_assigned_number)
my_assigned_number *= 3
print(my_assigned_number)
my_assigned_number /= 2
print(my_assigned_number)

# Operadores de identidad #

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y) # True
print(x is y) # False 
# Este es el verdadero uso de los operadores de identidad, nos dicen si dichos objetos son los mismos
# en memoria.
print(z == y)
print(z is not x) # False.


# Operadores de pertenencia #
print(2 in x) # True
print(4 in y) # False
print([1, 2] in x )


def extra():
    resultado = []
    for i in range(10, 56):
        if not i % 3 == 0 and i != 16 and i % 2 == 0:
            resultado.append(i)

    print(resultado)
    

extra()