"""/*
 * Crea una función que reciba un texto y muestre cada palabra en una línea,
 * formando un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
 */"""


def framework(word: str):
    if not isinstance(word, str) or not word:
        return "Must be a string and a not-empty string"
    
    sizes = [len(f"* {i} *") for i in word.split()]

    bigger = sorted(sizes)[-1]
    
    print("*" * bigger)

    for j in word.split():
        print("* "+ j + " " * (bigger - len(j) - 4) + " *")
    
    print("*" * bigger)

framework("¿Qué te pareció el reto?")
    