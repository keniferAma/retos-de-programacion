# programa que me identifique anagramas #

def anagrama(palabra1, palabra2):
    mientras = []
    concuerdan = [] 
    no_concuerdan = []
    for segunda in palabra2.lower():
        mientras.append(segunda)
    for definicion in palabra1.lower():
        if definicion in mientras:
           concuerdan.append(definicion)
        else:
            no_concuerdan.append(definicion)
    if len(concuerdan) == len(mientras) and len(no_concuerdan) == 0 and palabra1 != palabra2:
        return True
    else:
        return False
     
            
print(anagrama("Amor", "Roma"))

#hecho de manera mas simple:

def es_anagrama(palabra_1, palabra_2):
    if palabra_1.lower() == palabra_2.lower():
        return False
    return sorted(palabra_1.lower()) == sorted(palabra_2.lower()) 
    # en este punto podemos ver que ordenamos las palabras y simplemente si son iguales ordenadas
    # entonces arrojara true o false, es decir un bool. ya que no pusimos condicionales.
    # Ademas, al arrojar sorted() una lista, debíamos insertar lower() dentro de este 
    # igualmente no podiamos usar sort() ya que solo se usa directamente en una lista...

print(es_anagrama("amore", "Roma"))


lista_de_prueba = "carlos"
print(type(sorted(lista_de_prueba))) #sorted() nos arroja una lista -.-
"""<class 'list'>"""
print(sorted(lista_de_prueba))


