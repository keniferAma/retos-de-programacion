"""/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */"""

# patron = input("Escribe la combinación de letras: ")
# resultado = []
# salida = ""

# def decodificador(numero):
#     match numero:
#         case "2":
#             resultado.append("a")
#         case "22":
#             resultado.append("b")
#         case "222":
#             resultado.append("c")
#         case "3":
#             resultado.append("d")
#         case "33":
#             resultado.append("e")
#         case "333":
#             resultado.append("f")
#         case "4":
#             resultado.append("g")
#         case "44":
#             resultado.append("h")
#         case "444":
#             resultado.append("i")
#         case "5":
#             resultado.append("j")
#         case "55":
#             resultado.append("k")
#         case "555":
#             resultado.append("l")
#         case "6":
#             resultado.append("m")
#         case "66":
#             resultado.append("n")
#         case "666":
#             resultado.append("o")
#         case "7":
#             resultado.append("p")
#         case "77":
#             resultado.append("q")
#         case "777":
#             resultado.append("r")
#         case "7777":
#             resultado.append("s")
#         case "8":
#             resultado.append("t")
#         case "88":
#             resultado.append("u")
#         case "888":
#             resultado.append("v")
#         case "9":
#             resultado.append("w")
#         case "99":
#             resultado.append("x")
#         case "999":
#             resultado.append("y")
#         case "9999":
#             resultado.append("z")


# for p in patron.split("-"):
#     decodificador(p)
    

# print(f"Salida: {salida.join(f for f in resultado)}")


### AHORA VAMOS A INTENTAR RESOLVERLO MEDIANTE UN DICCIONARIO QUE ME ALMACENE LOS PATRONES:

numero_a_interpretar = "55-33-66-444-333-33-777"

resultado = ""

t9_prototipe = { 
    "1": ".,!?", "2": "abc", "3": "def",
    "4": "ghi", "5": "jkl", "6": "mno",
    "7": "pqrs", "8": "tuv", "9": "wxyz"
}

for n in numero_a_interpretar.split("-"): #"n" va a llevar la información de la cantidad de pulsos.(pero también el valor)
    numero = [] # Esta variable va a llevar el valor del número, con 1 sola cantidad
    numero.append(n[0])
    resultado += t9_prototipe[numero[0]][len(n) - 1] # Algo interesante acerca de los diccionarios; no sabía que se podía
    # acceder al índice de los valores del diccionario agregando corchetes con la posición en la clave...

print(resultado)




    


    




