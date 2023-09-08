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
    number_list_2 = number_list

    if mode not in ["Asc", "Desc"]:
        return "Not allowed"
    
    if mode == "Asc":
        while number_list_2:
            for n1 in number_list:
                trues = 0
                for n2 in number_list_2:
                    if n1 < n2:
                        trues += 1

                    if trues == len(number_list) - 1:
                        result.append(n1)
                        number_list_2.remove(n1)


    if mode == "Desc":
        while number_list_2:
            for n1 in number_list:
                trues = 0
                for n2 in number_list_2:
                    if n1 > n2:
                        trues += 1

                    if trues == len(number_list) - 1:
                        result.append(n1)
                        number_list_2.remove(n1)

            

    return result


values = [4, 2, 6, 8, 7, 9, 1]


print(matriz(values, "Desc"))


