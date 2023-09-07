"""/*
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */"""

def common_values(boolean: bool, array_1: list, array_2: list) -> list:
    result = []
    if boolean == True:
        for element in array_1:
            if element in array_2:
                result.append(element)
    
    else:
        for element in array_1:
            if not element in array_2:
                result.append(element)

    return result




array1 = [1, "b", "c", "d"]
array2 = ["a", "b", "c", "a"]
print(common_values(False, array1, array2))
