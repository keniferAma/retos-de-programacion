"""/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */"""



# code made bi copilot #

lista = ['cow', 'horse', 'cat', 'dog', 'duck', 'bird']

# add element at end #
lista.append('hen')
print(lista)

# add element at first #
lista.insert(0, 'elephant')
print(lista)

# add block of elements at the end #
block_of_elements = ['monkey', 'donkey', 'sworm']
lista.extend(block_of_elements)
print(lista)

# add block of elements at first #
elements = ['lion', 'tiger', 'jirafe']
lista = elements + lista
print(lista)

# delete an element #
del lista[3]
print(lista)

# update an element at a specific position #
lista[2] = 'giraffe'
print(lista)

# prove if element in lista #
element_to_find = 'horse'
if element_to_find in lista:
    print('Yes, the element is in the list')
else:
    print('No, the element is not in the list')

# delete the entire list #
del lista



# comprobando adicion de bloques de elementos al inicio #
nueva_lista = ['caballo', 'vaca']

extension_de_lista = ['gallina', 'gato']
nueva_lista = extension_de_lista + nueva_lista # by summing we're creating a new list
print(nueva_lista)

# comprobando adicion de bloques de elementos al final #
extension_de_lista = ['aguila', 'cordero']
nueva_lista.extend(extension_de_lista) # by 'extend' we're not creating a new list, but midifying the original list.
print(nueva_lista)

print('////')

# DIFICULTAD EXTRA #
lista_1 = ['caballo', 'vaca', 'cerdo', 'gato', 'perro', 'burro', 'pajaro']
lista_2 = ['elefante', 'jirafa', 'cerdo', 'burro', 'avestruz', 'cisne']

# Union #
lista_1.extend(lista_2)
print(lista_1)

# intersection #
intersection_list = []
for element in lista_2:
    if element in lista_1:
        intersection_list.append(element)

print(intersection_list)

# differency lista_1/lista_2 #
differency_list = []
for element in lista_1:
    if element not in lista_2:
        differency_list.append(element)

print(differency_list)

# differency lista_2/lista_1 #
differency_list = []
for element in lista_2:
    if element not in lista_1:
        differency_list.append(element)

print(differency_list)

# simetric differency #

lista_1.extend(lista_2)
set_list = set(lista_1)


print(set_list)
