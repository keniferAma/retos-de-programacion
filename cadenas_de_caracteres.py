"""/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos # se lee en el mismo sentido de un lado que del otro.
 * - Anagramas # las mismas letras en 2 palabras.
 * - Isogramas # la misma cantidad de letras en una sola palabra o frase.
 */"""

# string procedures #

my_string = 'this is my string'
my_string_2 = 'this is the second string'
print(my_string)
print(my_string.capitalize())
print(my_string.upper())
print(my_string.endswith('j'))
print(my_string.title())
print(my_string.find('hs'))
print(f'concatenate {my_string} plus {my_string_2}')
print(my_string.replace('s', 'j'))
print(my_string.encode('utf-8'))

my_string = 'anita lava la tina'

def palidrome(palabra_uno: str, palabra_2: str) -> str:
    palabra_uno = palabra_uno.replace(' ', '')
    palabra_2 = palabra_2.replace(' ', '')

    result = palabra_uno[::-1]
    result2 = palabra_2[::-1]

        
    if palabra_uno == result and palabra_2 == result2:
        return 'Both words are palindromes.'      
    elif palabra_uno != result and palabra_2 == result2:
        return 'The word 2 is palidnrome but not the word 1'
    elif palabra_uno == result and palabra_2 != result2:
        return 'The word 1 is palindrome but not the word 2'
    else:
        return 'None of the words are palindrome'
    

print(palidrome(my_string, my_string_2))


palabra_1 = 'pirata'
palabra_2 = 'patria'

def anagrama(palabra_uno: str, palabra_dos: str) -> str:
    if sorted(palabra_uno) != sorted(palabra_dos):
        return 'Las palabras no son anagramas.'
    return 'Las palabras son anagramas.'

print(anagrama(palabra_1, palabra_2)) 







