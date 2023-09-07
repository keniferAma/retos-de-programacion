"""/*
 * Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección
 * del producto.
 * - El programa retornará el nombre del producto y un array con el dinero
 *   de vuelta (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe,
 *   deberá indicarse con un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas
 *   de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
 */"""

products = {"beer": 20, "potatoes": 12, "soda": 15, "chocolate": 14, "penauts": 6}


def machine(product, cash):
    change = []
    change_operation = 0
    change_types = [200, 100, 50, 10, 5]

    if product not in products:
        return f"Product is not available. {[cash]}"
    
    if cash not in change_types:
        return "Not supported cash."
    
    if cash < products[product]:
        return f"Insufficient cash. {[cash]}"
    else:
        change_operation = cash - products[product]
        for c in change_types:
            while change_operation >= c:
                change.append(c)
                change_operation -= c
                    
            print(change_operation)


    return f"{product} {change}"

print(machine("potatoes", 50))


