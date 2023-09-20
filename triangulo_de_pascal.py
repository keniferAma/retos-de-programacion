"""/*
 * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal"
 * indicándole únicamente el tamaño del lado.
 *
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
 */"""



# Algoritmo hecho por la inteligencia artificial:

def generar_triangulo_pascal(lado):
    triangulo = [[1] * (i + 1) for i in range(lado)]
    # Primero se multiplica la cantidad de lados * [1] y se crea una especie de matriz 
    # [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1] ...]

    print(triangulo)
    print("////")
    for i in range(2, lado):
        for j in range(1, i):
            triangulo[i][j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            # Luego sumamos los elementos de cada uno de los elementos y los asignamos al siguiente elemento de 
            # elementos. [[1], [1, 1], [1, 2, 1], [1, 1, 1, 1]]
            #            [[1], [1, 1], [1, 2, 1], [1, 3, 1, 1]]
            #            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

            print(triangulo)
    return triangulo

def imprimir_triangulo_pascal(triangulo):
    for row in triangulo:
        print(' '.join(map(str, row)).center(len(triangulo) * 3))

# Tamaño del lado del Triángulo de Pascal
lado = 4

triangulo_pascal = generar_triangulo_pascal(lado)
imprimir_triangulo_pascal(triangulo_pascal)
