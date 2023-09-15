"""/*
 * Enunciado: Crea un programa se encargue de transformar un número binario
 * a decimal sin utilizar funciones propias del lenguaje que 
 * lo hagan directamente.
 */"""



def binario_a_decimal(numero_binario):

    todos_1_0 = [i for i in numero_binario if i == "1" or i == "0"]
    
    if len(todos_1_0) != len(numero_binario):
        return "Deben ser 1 o 0"
    
    exponente = len(numero_binario) - 1
    resultado = 0

    for n in numero_binario:
        result_exp = int(n) * 2 ** exponente
        resultado += result_exp
        exponente -= 1

    return resultado

numero_binario = "1010100010-0"
print(binario_a_decimal(numero_binario))





