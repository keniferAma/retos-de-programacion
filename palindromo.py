"""/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
 * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */"""



texto = "Anita lava la tina"


def palindromo(texto):
    invertida = ""
    no_invertida = ""

    for palabra in range(1, len(texto) + 1):
        letra = texto[-palabra]
        if letra.isalpha():
            invertida += letra.lower()


    for palabra in texto:
        if palabra.isalpha():
            no_invertida += palabra.lower()

    if invertida == no_invertida:
        return True
    else:
        return False

print(palindromo(texto))
        

    

