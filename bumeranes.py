"""/*
 * Enunciado: Crea una función que retorne el número total de bumeranes de 
 * un array de números enteros e imprima cada uno de ellos.
 * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
 *   seguidos, en el que el primero y el último son iguales, y el segundo
 *   es diferente. Por ejemplo [2, 1, 2].
 * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] 
 *   y [4, 2, 4]).
 */"""

def boomerang(array: list):
    n = len(array)
    result = []
    for i in range(n - 2):
        if array[i + 2] == array[i] and array[i + 1] < array[i]:
            result.append(array[i: i + 3])

    return result

array = [2, 1, 2, 3, 3, 4, 2, 4, 2, 4, 5]
print(boomerang(array))
