"""/*
 * Crea una función que imprima los 30 próximos años bisiestos
 * siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.
 */"""


def bisiest(year):
    bisiestos = []
    
    while len(bisiestos) < 30:
        year += 1
        if year % 4 == 0:
            bisiestos.append(year)
        
    return bisiestos
     
    
print(bisiest(2020))