"""/*
 * Enunciado: Dado un array de enteros ordenado y sin repetidos, 
 * crea una función que calcule y retorne todos los que faltan entre
 * el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
 */"""

def lost_numbers(numbers: list) -> list:
    lost = []

    if numbers != sorted(set(numbers)):
        return "the number list must be organized and non-repeated."
    
    min_num, max_num = numbers[0], numbers[-1]

    if numbers[0] > 0: 
        for n in range(min_num - 1, max_num):
            if n not in numbers:
                lost.append(n)
    
    else:   
        for n in range(numbers[0] + 1, numbers[-1]):
            if n not in numbers:
                lost.append(n)


    return lost


# Version made by artificial inteligence:
# Made a susbstract of the list organized and provided by the range, and the organized numbers entrance. 
# By doing it this way we're not wasting sources in large lists. (for bucle won't work too much)

def lost_numbers(numbers: list) -> list:
    if numbers != sorted(set(numbers)):
        raise ValueError("La lista de números debe estar ordenada y no debe tener repetidos.")
    
    min_num, max_num = numbers[0], numbers[-1]
    full_set = set(range(min_num, max_num + 1))
    numbers_set = set(numbers)
    
    return list(full_set - numbers_set)


list_of_numbers = [2, 5, 6, 7, 8, 9, 51]

print(lost_numbers(list_of_numbers))

