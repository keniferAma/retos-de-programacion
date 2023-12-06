"""/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */"""

def analizador_de_texto(path: str) -> None:
    file = open(path, "r+", encoding="utf-8")
    texto = file.read()
    numero_total_de_palabras = len(texto.split())
    palabras_individuales = [len(i) for i in texto.split()]
    longitud_palabras_individuales = sum(palabras_individuales) / numero_total_de_palabras
    numero_total_de_oraciones = len([j for j in texto.split(".")])
    palabra_mas_larga = [p for p in texto.split() if len(p) == sorted(palabras_individuales)[-1]]

    
    return (f"numero total de palabras: {numero_total_de_palabras}\n"
            f"numero total de oraciones: {numero_total_de_oraciones}\n"
            f"palabra mas larga: {''.join(palabra_mas_larga)[:-1]}\n"
            f"longitud media de las palabras: {longitud_palabras_individuales}") 


path = "C:/Users/kenifer/Desktop/pruebas-texto/analisis-de-texto-challenge.txt"

print(analizador_de_texto(path=path))  



## now we're gonna try with one only for loop ###

def analizador_de_texto_v2(path: str) -> None:
    try:
        with open(path, "r+", encoding="utf-8") as archivo:
            texto = archivo.read()
    except FileNotFoundError as message:
        raise message
    
    split = texto.split()
    numero_total_de_palabras = len(texto.split())
    longitud_palabras_individuales = []
    
    numero_de_oraciones = len(texto.split("."))
    lista_limpia = []
    palabra_mas_larga = []
    
    
    for i in range(0, len(split)):
        longitud_palabras_individuales.append(len(split[i]))

        if len(palabra_mas_larga) == 0:
            palabra_mas_larga.append(split[i])

        if split[i][-1] in ["!", "'", ".", ","]:
            lista_limpia.append(split[i][:-1])
            
        elif split[i][0] in ["¡", "'"]:
            lista_limpia.append(split[i][1:])
        else:
            lista_limpia.append(split[i])

        if i > 1:
            if len(lista_limpia[i]) > len(palabra_mas_larga[0]):
                palabra_mas_larga.pop(0)
                palabra_mas_larga.append(lista_limpia[i])
            elif len(lista_limpia[i]) == len(palabra_mas_larga[0]):
                palabra_mas_larga.append(lista_limpia[i])
        
    longitud_media_de_las_palabras = sum(longitud_palabras_individuales) / numero_total_de_palabras

    print(palabra_mas_larga)
    
    return numero_total_de_palabras


print(analizador_de_texto_v2(path=path)) 