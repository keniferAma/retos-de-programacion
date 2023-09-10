"""/*
 * Dado un listado de números, encuentra el SEGUNDO más grande.
 */"""

def segundo_mas_grande(numeros):
    numeros_organizados = sorted(numeros)
    return numeros_organizados[1]


print(segundo_mas_grande([1,3,77,8,9,0,2,4,5]))