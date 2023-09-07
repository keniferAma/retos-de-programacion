"""/*
 * Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
 */"""

vector_1 = [-1, 1]
vector_2 = [3, 1]



def ortogonal(vector_1: list, vector_2: list) -> str:
    result = 0

    for v1 in vector_1:
        for v2 in vector_2:
            result += v1 * v2

    return result == 0
    
print(ortogonal(vector_1, vector_2))


