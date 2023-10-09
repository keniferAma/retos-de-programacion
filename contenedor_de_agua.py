"""/*
 * Enunciado: Dado un array de números enteros positivos, donde cada uno
 * representa unidades de bloques apilados, debemos calcular cuantas unidades
 * de agua quedarán atrapadas entre ellos.
 *
 * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
 *
 *         ⏹
 *         ⏹
 *   ⏹💧💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹⏹⏹
 *
 *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
 *   de agua. Suponemos que existe un suelo impermeable en la parte inferior
 *   que retiene el agua.
 */"""
import re

array = [1, 0, 0, 0, 0, 4, 0, 1]
n = len(array)
bigger = sorted(array)[-1]
salida = [["⏹︎"] * n for i in range(bigger)]

def rebose(array):
    unidades_de_agua = 0
    for i in range(bigger - 1, -1, -1):
        
        for j in range(0, n):
            key = False
            
            if array[j] <= 0:
                left = False
                right = False
                
                for k in range(0, j): 
                    if array[k] >= 0:
                        left = True

                for h in range(j + 1, n): 
                    if array[h] > 0:
                        right = True

                if left and right:
                    key = True

            if array[j] > 0:
                salida[i][j] = "⏹︎ "
            
            elif key == True:
                salida[i][j] = "💧"
                unidades_de_agua += 1

            else: 
                salida[i][j] = "  "

            array[j] -= 1
    return unidades_de_agua

print(rebose(array))

for i in salida:
    print(" ".join(i))

# Solución hecha por la inteligencia artificial, pero solamente hace el cálculo del agua atrapada, y no su 
# representación.
def calcular_agua_atrapada(bloques):
    agua_atrapada = 0
    max_izq = max_der = 0
    izq = 0
    der = len(bloques) - 1

    while izq <= der:
        if bloques[izq] < bloques[der]:
            if bloques[izq] > max_izq:
                max_izq = bloques[izq]
            else:
                agua_atrapada += max_izq - bloques[izq]
            izq += 1
        else:
            if bloques[der] > max_der:
                max_der = bloques[der]
            else:
                agua_atrapada += max_der - bloques[der]
            der -= 1

    return agua_atrapada

bloques = [4, 0, 3, 6, 1, 3]
print(calcular_agua_atrapada(bloques))













