"""/*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
 */"""

lista = [["0", "0", "0", "0"],
         ["0", "0", "0", "0"],
         ["0", "0", "0", "0"],
         ["0", "0", "0", "0"]]




def espiral(amount: int):
    empty_list = []

    for i in range(amount):
        empty_list.append(amount * ["0"])

    direction = 1
    pares = 0
    while amount > 0:
        if direction == 1 or direction == 2:
            for i in range(1, amount):
                if direction == 1:
                    if i != amount:
                        empty_list[0][i] = '═'
                    else:
                        empty_list[0][i] = '╗'   
                
                elif direction == 2:
                    if i != amount:
                        empty_list[i][-1] = '║'
                    else:
                        empty_list[i][-1] = '╝' 

        else:
            for i in range(amount - 1, -1, -1):
                if direction == 3:
                    if i != 0:
                        empty_list[-1][i] = '═'
                    else:
                        empty_list[-1][i] = '╚'   
                
                elif direction == 4:
                    if i != amount:
                        empty_list[i][0] = '║'
                    else:
                        empty_list[i][0] = '╔' 

        if direction == 4:
            direction = 1

        direction += 1
        pares += 1

        if direction % 2 != 0:
            amount -= 1
        

    for m in empty_list:
        print(" ".join(m))


espiral(7)




def draw_spiral(n):
    # Define the symbols
    symbols = ['═', '║', '╗', '╔', '╝', '╚']
    
    # Initialize the matrix
    matrix = [[' ']*n for _ in range(n)]
    
    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Initialize the variables
    direction = 0
    x, y = 0, 0
    
    # Draw the spiral
    for i in range(n*n):
        matrix[x][y] = symbols[direction % 2]
        
        # Change direction if necessary
        dx, dy = directions[direction % 4]
        if not (0 <= x + dx < n and 0 <= y + dy < n) or matrix[x + dx][y + dy] != ' ':
            direction += 1
            dx, dy = directions[direction % 4]
        
        # Update the position
        x += dx
        y += dy
    
    # Add the corners
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != ' ' and ((i > 0 and matrix[i-1][j] == ' ') or (j > 0 and matrix[i][j-1] == ' ')):
                matrix[i][j] = symbols[2 + (i > j)]
            elif matrix[i][j] != ' ' and ((i < n-1 and matrix[i+1][j] == ' ') or (j < n-1 and matrix[i][j+1] == ' ')):
                matrix[i][j] = symbols[4 + (i < j)]
    
    # Print the spiral
    for row in matrix:
        print(''.join(row))

# Test the function
draw_spiral(5)
