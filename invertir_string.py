# invertir string #

def invertir_string(palabra):
    convertir = []
    invertir = []
    final = ""
    for p in palabra:
        convertir.append(p)
    for n in range(len(convertir) - 1, -1, -1): # aquí tambien aprendimos que range() tambien cuenta 
                                                # hacia atras.
        mientras = convertir.pop(n)
        invertir.append(mientras)
    for f in invertir:
        final += f

    print(final)

invertir_string("murcielago")


def invertir_string_2(palabra):
    inversion = []
    salida = ""
    for n in palabra:
        inversion.append(n)
    inversion.reverse()
    for p in inversion:
        salida += p
    print(salida)

invertir_string_2("veneno")

#By Brais:

def invertir(texto):
    len_text = len(texto)
    texto_invertido = ""
    for index in range(0, len_text):
        texto_invertido += texto[len_text - index - 1] #-1 porque len() me empieza a contar la cantidad 
        # desde 1, es decir en "hola" tenemos como resultado 4, entonces al restar 4 - 0 que
        # es donde comienza la iteración, se nos sale del rango de la estructura texto[4], la cual
        # nos ubica su indice contando desde 0.
    return texto_invertido

print(invertir("hola"))
"""aloh"""

prueba = "hola"
print(len(prueba))











        
