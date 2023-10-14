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

