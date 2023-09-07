"""/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */"""

## RESOLVIENDO EL RETO PERO CON UNA FUNCIÓN PROPIA DEL SISTEMA QUE ME CUENTA LA CANTIDAD DE PALABRAS.
# frase = input("Escribe la palabra: ")
# lista = []
# resultado = {}

# def contador_repetidas(frase: str):
#     for palabra in frase.split():
#         lista.append(palabra.lower())

#     for palabra in frase.split():
#         resultado[palabra] = lista.count(palabra)

    
# contador_repetidas(frase)
# print(f"Estas son las palabras encontradas y sus cantidades: {resultado}")


## INTENTANDO RESOLVERLO PERO SIN FUNCIONES DEL SISTEMA:

frase = "van a pasar los años y sin a embargo no hemos hecho nada productivo"


def contador_repetidas(frase: str):
    lista = frase.split()
    resultado = {}

    for palabra in lista:
        if palabra in resultado: # Si la palabra no se encuentra en el diccionario, entonces solamente le damos valor de 1.
            resultado[palabra] += 1# No nos funcionaba debido a que necesitabamos un numero antes de sumarle otro.
        else:
            resultado[palabra] = 1# El número que necesitabamos antes de sumarle los siguientes.

    return resultado

    
print(contador_repetidas(frase))

### CONCLUSIONES:
# La conclusión que podemos sacar de este ejercicio es que no podemos sumar un numero a un valor de diccionario, sin antes
# tener algun int en dicho campo.

# Otra de las conclusiones es que "split()" nos retorna directamente una lista con los elementos sin la necesidad
# de iterar a traves del string en este caso.

# La lógica en la que fallamos es que teníamos que buscar si en el diccionario ya estaba o no la palabra, si no estaba
# debíamos agregar "1" a esa palabra, y si si estaba ahí si le sumábamos un valor más.






### UN PEQUEÑO RECORDATORIO: CUANDO USAMOS EL PREFIJO "in" EN UN DICCIONARIO, ESTAMOS APUNTANDO A BUSCAR LA "key"
# Y NO EL "value".
lista_de_prueba = {'nombre': 'alejandro', 'apellido': 'salamanca'}

if 'apellido' in lista_de_prueba:
    print('yes')
else:
    print('no')















