"""/*
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
 */"""



# CODE MADE BY ARTIFICIAL INTELIGENCE:

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

def analyze_board(board):
    # Check if the board is valid
    if len(board) != 3 or any(len(row) != 3 for row in board):
        return "Nulo"
    
    # Check rows
    for row in board:
        if all(cell == "X" for cell in row):
            return "X"
        elif all(cell == "O" for cell in row):
            return "O"
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return "X"
        elif all(board[row][col] == "O" for row in range(3)):
            return "O"
    
    # Check diagonals
    if all(board[i][i] == "X" for i in range(3)) or all(board[i][2-i] == "X" for i in range(3)):
        return "X"
    elif all(board[i][i] == "O" for i in range(3)) or all(board[i][2-i] == "O" for i in range(3)):
        return "O"
    
    # Check if the game is still ongoing
    if any("" in row for row in board):
        return "Empate"
    
    # If none of the above conditions are met, it's a draw
    return "Empate"


print(analyze_board(board))


### SOME PRATICES USING "All" and "Any":

# lista_x = ["x", "x", "x", "x", "x", ""]
# lista_o = ["o", "o", "o", "o", "o", "o"]


# if all(x == "x" for x in lista_x):
#     print("x")
# else:
#     print("no x")
# """no x"""


# if any(o == "o" for o in lista_o):
#     print("o")
# else:
#     print("no o")
# """o"""


# for x in lista_x:
#     print(x == "x")
#     """True
#     True
#     True
#     True
#     True
#     False""" # LOOK AT THIS NEW FEATURE WE LEARNED TODAY