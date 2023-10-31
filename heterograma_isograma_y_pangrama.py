"""/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */"""


def heterograma(string: str) -> str:
    for i in "".join(string.split()):
        word = string.count(i)
        if word > 1:
            return f"La palabra {string} no es una heterograma."
    
    return f"La palabra {string} si es heterograma."

print(heterograma("hola cm est"))





