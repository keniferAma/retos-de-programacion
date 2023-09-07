"""/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
 */"""

from random import choice



def combinations(moves: list):
    """creating a function that defines a winner"""

    player_1 = 0
    player_2 = 0
    for c in moves:
        if c[0] == "R" and c[1] == "S":
            player_1 += 1
        elif c[0] == "P" and c[1] == "R":
            player_1 += 1
        elif c[0] == "S" and c[1] == "P":
            player_1 += 1
        else:
            player_2 += 1

    if player_1 == player_2:
        return "Tie"
    elif player_1 > player_2:
        return "Player 1"
    else:
        return "player 2"
    
    
print(combinations([("R","S"), ("S","R"), ("P","S"), ("P", "R")]))
    




