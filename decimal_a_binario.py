"""/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */"""


numero = 6
binario = 0
terminal = []
salida = ""
while True:
    resultado = numero // 2 #Al usar doble slash estamos devolviendo el cociente de la division sin decimales, solo entero
    binario = numero % 2
    numero = resultado
    terminal.append(binario) #al usar "int" nos vamos a deshacer de los números después de la coma.
    if numero < 1:
        break


salida = salida.join(str(n) for n in terminal)
print(salida)




## RETO HECHO POR INTELIGENCIA ARTIFICIAL

def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario #RECORDAR QUE LOS STRINGS LOS PODEMOS SUMAR, Y LOS ESTABAMOS USANDO CON join() -.-
        decimal //= 2 # el código equivalente para esta parte es "decimal = decimal // 2", lo cual tiene sentido.
        # el numero que traemos desde un principio lo tenemos guardado todavía en "decimal", luego, al estar esta parte
        # mas abajo del código, simplemente estamos autocambiando la variable por "//2", la cual va a volver al inicio
        # ya que estamos usando un bucle while.
    
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))
numero_binario = decimal_a_binario(numero_decimal)

print(f"El número binario equivalente es: {numero_binario}")











