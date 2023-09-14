"""/*
 * Enunciado: Crea un programa que calcule el daño de un ataque durante
 * una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
 *   (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100.
 */"""

from dataclasses import dataclass

 
@dataclass
class Pokemon:
    ataque: int
    defensa: int


@dataclass(init=False)
class Fuego(Pokemon):
    f_contra_fuego: int = 1 
    f_contra_agua: float = 0.5
    f_contra_planta: int = 2
    f_contra_electrico: int = 1 
        

@dataclass(init=False)
class Agua(Pokemon):
    f_contra_fuego: float = 0.5
    f_contra_agua: int = 1
    f_contra_planta: int = 2
    f_contra_electrico: int = 1


@dataclass(init=False)
class Planta(Pokemon):
    f_contra_fuego: int = 0.5 
    f_contra_agua: float = 1
    f_contra_planta: int = 1
    f_contra_electrico: int = 2


@dataclass(init=False)
class Electrico(Pokemon):
    f_contra_fuego: int = 1 
    f_contra_agua: float = 2
    f_contra_planta: int = 0.5
    f_contra_electrico: int = 1


def pelea(atacante: str, defensor: str):
    tipo = 0
    match type(defensor).__name__:
        case "Electrico":
            tipo = atacante.f_contra_electrico
        case "Fuego":
            tipo = atacante.f_contra_fuego
        case "Planta":
            tipo = atacante.f_contra_planta
        case "Agua":
            tipo = atacante.f_contra_agua

    if tipo == 0:
        return "No fue posible realizar la batalla, verifica que los pokemon esten presentes"

    resultado = 50 * (atacante.ataque / defensor.defensa) * tipo

    return int(resultado)




pikachu = Electrico(50, 60)
squartul = Agua(43, 78)
charizard = Fuego(90, 50)
butterfly = Planta(49, 30)


print(pelea(charizard, butterfly))


# solucion hecha por la inteligencia artificial de bing.

def calcular_dano(tipo_atacante, tipo_defensor, ataque, defensa):
    
    efectividad = {
        'Agua': {'Fuego': 2, 'Planta': 0.5, 'Eléctrico': 1, 'Agua': 1},
        'Fuego': {'Agua': 0.5, 'Planta': 2, 'Eléctrico': 1, 'Fuego': 1},
        'Planta': {'Agua': 2, 'Fuego': 0.5, 'Eléctrico': 1, 'Planta': 1},
        'Eléctrico': {'Agua': 2, 'Fuego': 1, 'Planta': 0.5, 'Eléctrico': 1}
    }

    if tipo_atacante not in efectividad or tipo_defensor not in efectividad[tipo_atacante]:
        raise ValueError("Tipo de Pokémon no válido")

    if not (1 <= ataque <= 100) or not (1 <= defensa <= 100):
        raise ValueError("Ataque y defensa deben estar entre 1 y 100")

    dano = 50 * (ataque / defensa) * efectividad[tipo_atacante][tipo_defensor]
    return dano

# Ejemplo de uso
dano = calcular_dano('Fuego', 'Planta', 80, 50)
print(dano)
   




