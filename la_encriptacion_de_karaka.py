"""/*
 * Enunciado: Crea una función que sea capaz de encriptar y desencriptar texto
 * utilizando el algoritmo de encriptación de Karaca 
 * (debes buscar información sobre él).
 */"""

"""Este algoritmo es un ejercicio de programación que consiste en desarrollar una función que es capaz 
de encriptar y desencriptar texto. Aquí están los pasos del algoritmo:

Invertir la entrada: Por ejemplo, si la entrada es “apple”, se invierte para obtener “elppa”.
Reemplazar todas las vocales usando el siguiente esquema: a => 0, e => 1, i => 2, o => 3, u => 4. Entonces 
“elppa” se convierte en “1lpp0”.
Agregar “aca” al final de la palabra: “1lpp0” se convierte en “1lpp0aca”.
Por lo tanto, la salida para “apple” sería “1lpp0aca”. Todos los datos de entrada son cadenas de texto en 
minúsculas y todas las salidas deben ser cadenas de texto1."""



def encrypt(string):
    result = ""
    suma = -1
    iteraciones = 0
    n = len(string)
    while iteraciones < n:
        if string[suma] == "a":
            result += "0"
        elif string[suma] == "e":
            result += "1"
        elif string[suma] == "i":
            result += "2"
        elif string[suma] == "o":
            result += "3"
        elif string[suma] == "u":
            result += "4"
        else:    
            result += string[suma]

        if iteraciones + 1 == n:
            result += "aca"
        suma -= 1
        iteraciones += 1

    return result

string = "verdades"
print(encrypt(string))
    


def desencrypt(string):
    string = string[:-3]
    result = ""
    suma = -1
    iteraciones = 0
    n = len(string)
    while iteraciones < n:
        if string[suma] == "0":
            result += "a"
        elif string[suma] == "1":
            result += "e"
        elif string[suma] == "2":
            result += "i"
        elif string[suma] == "3":
            result += "o"
        elif string[suma] == "4":
            result += "u"
        else:    
            result += string[suma]

        suma -= 1
        iteraciones += 1

    return result

print(desencrypt("s1d0dr1vaca"))



def karaca_encrypt_decrypt(text):
    if not isinstance(text, str):
        return "Error: Input must be a string"
    if text == "":
        return "Error: Input string cannot be empty"
    
    vowels = {'a': '0', 'e': '1', 'i': '2', 'o': '3', 'u': '4'}
    reverse_vowels = {v: k for k, v in vowels.items()}
    
    if text.endswith("aca"):
        # Decrypt
        text = text[:-3][::-1]
        return ''.join([reverse_vowels.get(char, char) for char in text])
    else:
        # Encrypt
        text = text[::-1]
        return ''.join([vowels.get(char, char) for char in text]) + "aca"

print(karaca_encrypt_decrypt("maraca"))


print(string[::-1]) # Por lo menos aprendimos algo. invertir un string. Todo gracias al "rebanado de listas"

"""El "rebanado de listas" es una característica en Python que permite acceder a subconjuntos de una lista 
(o cualquier objeto secuencial, como un string). La sintaxis básica es `lista[inicio:final:paso]`¹²:

- `inicio`: Es el índice donde comienza la rebanada. Si se omite, se asume que es 0.
- `final`: Es el índice donde termina la rebanada. Este índice no se incluye en la rebanada. 
Si se omite, se asume que es el final de la lista.
- `paso`: Es la cantidad de elementos a saltar. Si se omite, se asume que es 1.

Por ejemplo, si tienes una lista `numeros = [0, 1, 2, 3, 4, 5]`, puedes obtener los primeros tres 
elementos con `numeros[0:3]`, que devuelve `[0, 1, 2]`. También puedes obtener los elementos en las 
posiciones pares con `numeros[::2]`, que devuelve `[0, 2, 4]`.

Cuando usas un paso negativo, como en `numeros[::-1]`, la lista se recorre en orden inverso¹². 
Por lo tanto, `numeros[::-1]` devuelve `[5, 4, 3, 2, 1, 0]`, que es la lista original invertida.
"""

diccionario = {"a": 0, "b": 1, "c": 2}
diccionario_al_reves = {value :key for key, value in diccionario.items()}
print(diccionario_al_reves)
print(diccionario.get("g", "j"))
