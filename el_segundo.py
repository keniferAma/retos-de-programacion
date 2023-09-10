"""/*
 * Dado un listado de números, encuentra el SEGUNDO más grande.
 */"""

def segundo_mas_grande(numeros):
    if len(numeros) < 2:
        return "La lista debe contener por lo menos 2 elementos."
    numeros_organizados = sorted(set(numeros))
    if len(numeros_organizados) < 2:
        return "No hay segundo numero mas grande."
    else:
        return numeros_organizados[1]


print(segundo_mas_grande([1,3,77,8,9,0,2,4,5]))