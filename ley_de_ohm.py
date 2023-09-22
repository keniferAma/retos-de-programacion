"""/*
 * Enunciado: Crea una función que calcule el valor del parámetro perdido
 * correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 *   el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará
 *   la cadena de texto "Invalid values".
 */"""

def ley_de_ohm(V = None, R = None , I = None):

    if V and R and I:
        return "Los tres valores al tiempo no es posible."
    elif R and I:
        return f"El valor del voltaje es: {R * I}"
    elif V and I:
        return f"El valor de la resistencia es: {V * I}"
    elif V and R:
        return f"El valor de la corriente es: {V / R}"
    else:
        return "Deben haber al menos 2 valores."
    
print(ley_de_ohm(120))