"""/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */"""

import random


def generador_de_palabras(palabras: list) -> str:
    palabra_seleccionada = random.choice(palabras)

    return palabra_seleccionada


def esconder_palabra(palabra: str) -> str:
    palabra_lista = ""

    n = len(palabra)

    cantidad_de_lineas = n // 2

    ubicacion = []

    
    while len(ubicacion) < cantidad_de_lineas:
        numero = random.randint(0, n - 1)
        if numero not in ubicacion:
            ubicacion.append(numero)
        else:
            continue

    for i in palabra:
        if palabra.index(i) in ubicacion:
            palabra_lista += "_"
        else: 
            palabra_lista += i

    return palabra_lista



lista_de_palabras = [
    "carro", "montaña", "espantapajaros",
    "campeon", "cartas", "espejo", "rinoceronte",
    "escaleras", "arandanos", "cancion", "marea",
    "simulacro", "reinado", "corona", "acueducto", 
    "cerdo", "caballo", "escalera", "crispetas",
    "sanguijuela", "legumbre", "navidad", "carretera", 
    "marioneta", "carreta", "mascara", "botella", "espuma",
    "binoculares", "nevera", "lavadora", "camioneta", "motocicleta",
    "avioneta", "salamandra", "avestruz", "telefono", "advertencia",
    "autopista", "iluminacion", "gasolina", "madera" 
]
        


def solucion(palabra: str, palabra_con_hash: str):
    hash_actualizado = palabra_con_hash
    vidas = 5
    letras = []
    
    
    for i in range(len(palabra_con_hash)):
        if palabra_con_hash[i] == "_":
            letras.append(palabra[i])
   
    while vidas > 0:
        
        print(palabra_con_hash)

        letra_o_palabra = input("Escribe la letra o palabra: ")

        if len(letra_o_palabra) > 1:
            if letra_o_palabra == palabra:
                print(f"{palabra}\nLa palabra es correcta.")
                break

            else:
                vidas -= 1
                print(f"Incorrecto. Te quedan {vidas} vidas.")

        else:    
            if letra_o_palabra in letras:
                for j in range(len(palabra)):

                    if letra_o_palabra == palabra[j]:
                       hash_actualizado = hash_actualizado[:j] + palabra[j] + hash_actualizado[j + 1:]
                    
                
            else:
                vidas -= 1
                print(f"Incorrecto. Te quedan {vidas} vidas.")
                
    

            palabra_con_hash = hash_actualizado

            if palabra == hash_actualizado:
                print(f"{palabra}\nLa palabra es correcta.")
                break


palabra = generador_de_palabras(lista_de_palabras)

palabra_hasheada = esconder_palabra(palabra)

solucion(palabra, palabra_hasheada)
    



#### version hecha por la inteligencia artificial ####

import random

def ocultar_letras(palabra):
    num_letras_ocultas = int(len(palabra) * 0.6)
    indices = random.sample(range(len(palabra)), num_letras_ocultas)
    return "".join("_" if i in indices else letra for i, letra in enumerate(palabra))

def jugar_adivinanza(palabras, intentos):
    palabra = random.choice(palabras)
    palabra_oculta = ocultar_letras(palabra)
    print(f"Palabra a adivinar: {palabra_oculta}")
    print(f"Número de intentos restantes: {intentos}")

    while intentos > 0:
        entrada = input("Introduce una letra o una palabra: ")
        if len(entrada) == 1:
            if entrada in palabra:
                palabra_oculta = "".join(entrada if letra == entrada else palabra_oculta[i] for i, letra in enumerate(palabra))
                print(f"¡Bien hecho! La palabra ahora es: {palabra_oculta}")
            else:
                intentos -= 1
                print(f"¡Lo siento! La letra no está en la palabra. Intentos restantes: {intentos}")
        elif len(entrada) == len(palabra):
            if entrada == palabra:
                print("¡Felicidades! Has adivinado la palabra.")
                return
            else:
                intentos -= 1
                print(f"¡Lo siento! Esa no es la palabra. Intentos restantes: {intentos}")
        else:
            print("Entrada inválida. Por favor, introduce una letra o una palabra de la misma longitud que la palabra a adivinar.")
        if palabra_oculta == palabra:
            print("¡Felicidades! Has adivinado todas las letras de la palabra.")
            return
        if intentos == 0:
            print("¡Lo siento! Has agotado todos tus intentos.")
            return

palabras = ["murcielago", "elefante", "cocodrilo", "hipopotamo"]
intentos = 10
jugar_adivinanza(palabras, intentos)

