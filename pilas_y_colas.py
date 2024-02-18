"""/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */"""


# stacks #
# The last element added will be the first one in being removed.
stack_list = []

stack_list.append('a')
stack_list.append('b')
stack_list.append('c')

print(stack_list)
"""['a', 'b', 'c']"""

stack_list.pop()
stack_list.pop()

print(stack_list)
"""['a']"""

# queue #
# The first element in being added will be the first one removed.

from queue import Queue

# create a queue
q = Queue()

# put elements into the queue
q.put('a')
q.put('b')
q.put('c')

print('Initial queue:', list(q.queue))

# get elements from the queue
print('Elements dequeued from the queue:')
print(q.get())
"""a"""
print(q.get())
"""b"""

print('Queue after elements are dequeued:', list(q.queue))
"""Queue after elements are dequeued: ['c']"""


# extra #

website = ['browser']
counter = 1
location = 0

while True:
    print('Choose: \n1: forward\n2: backward\n3: exit')
    user = int(input())

    match user:
        case 1:
            if location == counter - 1:
                website.append(f'page {counter}')
                location += 1
                counter += 1

            else: 
                location += 1

        case 2:
            if location > 0:
                location -= 1
                

        case 3:
            break

    print(website[location])



back_stack = ['browser']
forward_stack = []

while True:
    print('Current page:', back_stack[-1])
    print('Choose: \n1: forward\n2: backward\n3: new page\n4: exit')
    user = int(input())

    if user == 1:  # forward
        if forward_stack:
            back_stack.append(forward_stack.pop())
        else:
            print("Can't go forward.")
    elif user == 2:  # backward
        if len(back_stack) > 1:
            forward_stack.append(back_stack.pop())
        else:
            print("Can't go back.")
    elif user == 3:  # new page
        page = f'page {len(back_stack)}'
        back_stack.append(page)
        forward_stack.clear()
    elif user == 4:  # exit
        break


    








