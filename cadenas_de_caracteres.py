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


palabra_1 = 'murcielagoo'
palabra_2 = 'patria'

def anagrama(palabra_uno: str, palabra_dos: str) -> str:
    if sorted(palabra_uno) != sorted(palabra_dos):
        return 'Las palabras no son anagramas.'
    return 'Las palabras son anagramas.'

print(anagrama(palabra_1, palabra_2)) 


palabra_1 = 'murcielago'

def isograma(palabra_uno: str, palabra_dos: str) -> str:
    letra = ''
    conteo = 0
    resultado_palabra_uno = True
    resultado_palabra_dos = True

    for i in range(len(palabra_uno)):
        for j in range(i + 1 , len(palabra_uno)):
            letra = palabra_uno[i]
            if palabra_uno[j] == palabra_uno[i]:
                conteo += 1

            if conteo == 1:
                resultado_palabra_uno = False
        letra = ''
        conteo = 0
        letra += palabra_uno[i]

    for i in range(len(palabra_dos)):
        if palabra_dos.count(palabra_dos[i]) >= 2: 
            resultado_palabra_dos = False

    if resultado_palabra_uno and resultado_palabra_dos:
        return 'Ambas palabras son isogramas.'
    elif resultado_palabra_uno and not resultado_palabra_dos:
        return 'La palabra uno es isograma, pero no la segunda.'
    elif resultado_palabra_dos and not resultado_palabra_uno:
        return 'La palabra dos es isograma, pero no la primera.'
    else:
        return 'Ninguna de las dos palabras es isograma.'            


    
print(isograma(palabra_1, palabra_2))


# something we learned today # the add function in sets.
letras = set()

letras.add('a')
letras.add('b')
letras.add('a')
letras.add('c')
letras.add('c')

print(letras)




# solution given by bing #
# the AI set a only function to manage whether a word is isogram or not.
def es_isograma(palabra: str) -> bool:
    letras = set()
    for letra in palabra:
        if letra in letras:
            return False
        letras.add(letra)
    return True

def isograma(palabra_uno: str, palabra_dos: str) -> str:
    resultado_palabra_uno = es_isograma(palabra_uno)
    resultado_palabra_dos = es_isograma(palabra_dos)

    if resultado_palabra_uno and resultado_palabra_dos:
        return 'Ambas palabras son isogramas.'
    elif resultado_palabra_uno and not resultado_palabra_dos:
        return 'La palabra uno es isograma, pero no la segunda.'
    elif resultado_palabra_dos and not resultado_palabra_uno:
        return 'La palabra dos es isograma, pero no la primera.'
    else:
        return 'Ninguna de las dos palabras es isograma.'            

print(isograma(palabra_1, palabra_2))
