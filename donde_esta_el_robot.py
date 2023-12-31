"""/*
 * Enunciado: Calcula dónde estará un robot (sus coordenadas finales) que se
 * encuentra en una cuadrícula representada por los ejes "x" e "y".
 * - El robot comienza en la coordenada (0, 0).
 * - Para idicarle que se mueva, le enviamos un array formado por enteros 
 *   (positivos o negativos) que indican la secuencia de pasos a dar.
 * - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene,
 *   luego 5, se detiene, y finalmente 2. 
 *   El resultado en este caso sería (x: -5, y: 12)
 * - Si el número de pasos es negativo, se desplazaría en sentido contrario al
 *   que está mirando.
 * - Los primeros pasos los hace en el eje "y". Interpretamos que está mirando
 *   hacia la parte positiva del eje "y".
 * - El robot tiene un fallo en su programación: cada vez que finaliza una
 *   secuencia de pasos gira 90 grados en el sentido contrario a las agujas
 *   del reloj.
 */"""


def robot(pasos: list) -> str:
    result = [0, 0]
    n = len(pasos)
    count_y = 0
    count_x = 0
    for i in range(0, n):
        if i % 2 == 0:  
            if count_y % 2 == 0:
                result[1] += pasos[i]
                count_y += 1
            else:
                result[1] -= pasos[i]

        else:
            if count_x % 2 == 0:
                result[0] -= pasos[i]
            else:
                result[0] += pasos[i]

    return f"(x: {result[0]}, y: {result[1]})"



sequence = [10, 5, -2, 7, -3, -3]
print(robot(sequence))


# Ahora vamos a ver la version hecha por la inteligencia artificial:

def calcular_posicion_robot(pasos):
    # Inicializamos las coordenadas del robot
    x, y = 0, 0
    # Inicializamos la dirección en la que está mirando el robot
    direccion = 0  # 0: arriba, 1: izquierda, 2: abajo, 3: derecha

    for paso in pasos:
        if direccion == 0:
            y += paso
        elif direccion == 1:
            x -= paso
        elif direccion == 2:
            y -= paso
        elif direccion == 3:
            x += paso

        # El robot gira 90 grados en sentido contrario a las agujas del reloj
        direccion = (direccion + 1) % 4

    return x, y

# Prueba del código
print(calcular_posicion_robot([10, 5, -2]))  # Debería imprimir (-5, 12)
