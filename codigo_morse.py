"""/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */"""


morse_code = { 
    'A': '·-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----','2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '"': '.-..-.', 'espacio': ' ', ' ': '', '': ' '
}


def conversor_a_morse(entrada):
    resultado_morse = ""
    match entrada.isupper():
        case True:
            for palabra in entrada:
                resultado_morse += morse_code[palabra] + morse_code['espacio']

        case False:
            for codigo in entrada.split():
                for k, v in morse_code.items():
                    if v == codigo:
                        resultado_morse +=  k
                    

    return resultado_morse


entrada = "HOLA COMO  ESTAS"
entrada_morse = ".... --- .-.. ·-  -.-. --- -- ---  . ... - ·- ..."




print(conversor_a_morse(entrada_morse))

def espacios(entrada):
    espacios_list = []
    while True:
        varios_espacios = entrada.find("  ")
        if varios_espacios == -1:
            break
        un_espacio = entrada[0: varios_espacios].count(" ")
        espacios_list.append(un_espacio)
        entrada = entrada[varios_espacios:].strip()

    return espacios_list
        
print(espacios(entrada_morse))


entrada_junta = "holacomovas"

entrada_correjida = ""
lista = [3,3]
suma_de_lista = 0

for indice, letra in enumerate(entrada_junta):
    entrada_correjida += letra
    if indice == lista[0]:
        entrada_correjida += " "
        lista 
        del lista[0]




print(entrada_correjida)



# PROTOTIPO HECHO POR INTELIGENCIA ARTIFICIAL:

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

def morse_code(text): # al parecer éste es el selector de encode morse y encode texto.
    if '.' in text or '-' in text:
        return decode_morse(text)
    else:
        return encode_morse(text)

def encode_morse(text): # Esta función se encarga de transformar texto a morse.
    encoded_text = ''
    for char in text:
        if char != " ":
            encoded_text += MORSE_CODE_DICT[char.upper()] + " "
        else:
            encoded_text += " "
    return encoded_text

def decode_morse(text):
    decoded_text = '' # vamos reiniciando valores.
    text += " "
    morse_word = "" #.... # borraso y luego el siguiente patrón, es decir "---" y suscesivamente.
    space_count = 0 #1
    for char in text: #".... --- .-.. .-  -.-. --- -- ---  . ... - .- ... "
        if char != " ":
            space_count = 0 
            morse_word += char
        else:
            space_count += 1
            if space_count == 2: #La única manera que este valor sea igual a 2 es cuando hallan 2 espacios seguidos.
                decoded_text += " " # Y se agregan a la variable de salida.
            else:
                decoded_text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_word)]
                # Algo bien interesante en la lógica de este código radica en el uso de listas para poder usar
                # una de sus propiedades, el index:
                # al pasar el valor de la variable "morse_word", en el cual, en su primer valor es "....",
                # mediante la propiedad index, busca la ubicacion en la lista de los values, al encontrarla
                # nos retorna un número, el cual le vamos a pasar a la lista con las keys, el cual también 
                # transformamos en una lista, para de este modo acceder a su valor en índice.
                # todo esto es posible ya que agrupar todos los valores de "values" y "keys" en listas separadas,
                # al ser parte de un diccionario, van a tener la misma cantidad de elementos en cada lista
                # y por consiguiente van a coincidir unos con otros.
                morse_word = "" # Luego de procesar la primera letra, reiniciamos este valor
    return decoded_text


#print(morse_code(".... --- .-.. .-  -.-. --- -- ---  . ... - .- ..."))



# EN ESTE EJEMPLO TRATAMOS DE REPLICAR LA MANERA DE HALLAR keys DE UN DICCIONARIO POR MEDIO DE LISTAS Y SUS
# RESPECTIVOS INDICES, PASANDO SUS values.
# Y ESTO DEBIDO A QUE AMBOS ELEMENTOS DE UN DICCIONARIO VAN A TENER LA MISMA CANTIDAD DE ELEMENTOS,
# PRIMERO IDENTIFICAMOS EL INDEX DEL value QUE QUEREMOS, Y ESE MISMO INDEX LO PASAMOS AL BUSCADOR DE INDICES
# DE LA LISTA DE keys. ALGO A DESTACAR, ES QUE TIPAMOS COMO list, SOLAMENTE PARA PODER USAR ALGUNAS DE LAS 
# PROPIEDADES DE LAS LISTAS.
diccionario_de_prueba = {
    "a": ".",
    "b": "-",
    "c": "$"
}

print(list(diccionario_de_prueba.keys())[list(diccionario_de_prueba.values()).index("$")])




# OTRO ENFOQUE MÁS HECHO POR LA INTELIGENCIA ARTIFICIAL:
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

def morse_code(text):
    if '.' in text or '-' in text:
        return decode_morse(text)
    else:
        return encode_morse(text)

def encode_morse(text):
    encoded_text = []
    for word in text.split(): #hola
        encoded_word = [MORSE_CODE_DICT[char.upper()] for char in word] 
        # este "list comprehension" nos itera por cada letra de cada palabra y la pasa al indice del
        # diccionario "MORSE_CODE_DICT" en letra mayúscula. Basicamente sería con el propósito solamente
        # de poder buscar en letra mayúscula. posteriormente guarda su resultado en la variable.
        encoded_text.append(" ".join(encoded_word)) # Aquí les damos de a un espacio a cada value.
        print(encoded_text)
        """['.... --- .-.. .-']
           ['.... --- .-.. .-', '-.-. --- -- ---']
           ['.... --- .-.. .-', '-.-. --- -- ---', '...- .- -- --- ...']"""
    return "  ".join(encoded_text) # Aquí les damos doble espacio a cada elemento de la lista "encoded_text"
    # tengamos en cuenta que join() nos funciona pasando una lista sin la necesidad de iterar a traves de ella.

def decode_morse(text):
    decoded_text = []
    for encoded_word in text.split("  "):
        decoded_word = [key for code in encoded_word.split() for key, value in MORSE_CODE_DICT.items() if value == code]
        # Aquí podemos observar una list comprenhesion con un bucle for anidado en otro bucle for.
        # Podemos apreciar que "key", al inicio de la lista, es el valor que va a quedar como elemento de la lista.
        # "for code in encoded_word.split()" es el bucle padre.

        decoded_text.append("".join(decoded_word))
    return " ".join(decoded_text)



# ESTE CÓDIGO SERÍA SU EQUIVALENTE AL ANTERIORMENT MENCIONADO COMO list_comprenhension:

# def decode_morse(text):
#     decoded_text = []
#     for encoded_word in text.split("  "):
#         decoded_word = []
#         for code in encoded_word.split():
#             for key, value in MORSE_CODE_DICT.items():
#                 if value == code:
#                     decoded_word.append(key)

#         decoded_text.append("".join(decoded_word))
#     return " ".join(decoded_text)

print(morse_code("hola como vamos"))
print(morse_code(".... --- .-.. .-  -.-. --- -- ---  ...- .- -- --- ..."))



