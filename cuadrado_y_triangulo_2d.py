"""4/*
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
 */"""


def triangle_square(type, side):  

    if type.lower() == "square":
        for n in range(side):
            print(" *" * side)

    elif type.lower() == "triangle":
        side_length = side
        for n in range(side):
            print(" *" * side_length)
            side_length -= 1
    else:
        print("Not supported")

triangle_square("triangle", 6)