"""/*
 * Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales
 * a Sauron contra otras bondadosas que no quieren que el mal reine
 * sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
 *   Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
 *   Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre
 * los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate.
 *   Dependiendo de la suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable
 *   de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco
 *     2 Pelosos empatan contra 1 Orco
 *     3 Pelosos ganan a 1 Orco
 */"""


razas_bondadosas = {
    "pelosos": 1, "sureños_buenos": 2, "enanos": 3, "numenoreanos": 4, "elfos": 5
}

razas_malvadas = {"sureños_malos": 2, "orcos": 2, "goblins": 2, "huargos": 3, "trolls": 5 
}

lista_buenos = ["pelosos", "pelosos", "sureños_buenos", "elfos", "enanos", "enanos"]
lista_malos = ["sureños_malos", "sureños_malos", "huargos", "trolls"]


def batalla(bondadosas: list, malvadas: list):
    """develping a battle and defining a winner"""

    valor_total_bondadosas = 0
    valor_total_malvadas = 0
    personajes_bondadosas = []
    personajes_malvadas = []
    
    if not bondadosas or not malvadas:
        return "Bondadosas o malvadas sin personajes."

    for n in bondadosas:
        valor_total_bondadosas += razas_bondadosas[n]
        personajes_bondadosas.append(f" {bondadosas.count(n)} {n}".strip())

    for g in malvadas:
        valor_total_malvadas += razas_malvadas[g]
        personajes_malvadas.append(f" {malvadas.count(g)} {g}".strip())

    if valor_total_bondadosas > valor_total_malvadas:
        return ("Gana el bien,\n" + ", ".join(set(personajes_bondadosas)) + " ganan contra " + 
                 ", ".join(set(personajes_malvadas)))
    
    elif valor_total_bondadosas == valor_total_malvadas:
        return ("Empate,\n" + ", ".join(set(personajes_malvadas)) + " empatan contra " + 
                 ", ".join(set(personajes_bondadosas)))
    
    else:
        return ("Gana el mal,\n" + ", ".join(set(personajes_malvadas)) + " ganan contra " + 
                 ", ".join(set(personajes_bondadosas)))
    


print(batalla(bondadosas=lista_buenos, malvadas=lista_malos))