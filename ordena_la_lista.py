"""/*
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [4, 2, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
 */"""

def matriz(number_list: list, mode: str) -> list:
    result = []


    if mode not in ["Asc", "Desc"]:
        return "Not allowed"
    
    if mode == "Asc":
        while number_list:
            for n1 in number_list:
                trues = 0
                for n2 in number_list:
                    if n1 < n2:
                        trues += 1

                    if trues == len(number_list) - 1:
                        result.append(n1)
                        number_list.remove(n1)


    if mode == "Desc":
        while number_list:
            for n1 in number_list:
                trues = 0
                for n2 in number_list:
                    if n1 > n2:
                        trues += 1

                    if trues == len(number_list) - 1:
                        result.append(n1)
                        number_list.remove(n1)

            

    return result


values = [4, 2, 6, 8, 7, 9, 1]

print(matriz(values, "Desc"))



# opcion hecha por inteligencia artificial:

def ordenar_numeros(lista, orden):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-i-1):
            if (orden == "Asc" and lista[j] > lista[j+1]) or (orden == "Desc" and lista[j] < lista[j+1]):
                # Intercambiar elementos
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista


values = [4, 2, 6, 8, 7, 9, 1, 1]
print(len(values))
print(ordenar_numeros(values, "Asc"))


