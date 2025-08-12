import os
import time
import enum
from keyboard import add_hotkey




board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]
        

class Buttons(enum.Enum):
    RIGHT = 'right'
    LEFT = 'left'
    UP = 'up'
    DOWN = 'down'
    TURN_RIGHT = 'r'
    TURN_LEFT = 'e'


column_pixel_1 = 3
column_pixel_2 = 4
column_pixel_3 = 4
column_pixel_4 = 4
row_pixel_1 = 2
row_pixel_2 = 2
row_pixel_3 = 1 
row_pixel_4 = 0


class LShape:
    def __init__(
            self, column_pixel_1, column_pixel_2, column_pixel_3, column_pixel_4,
            row_pixel_1, row_pixel_2, row_pixel_3, row_pixel_4
    ):
        self.column_pixel_1 = column_pixel_1
        self.column_pixel_2 = column_pixel_2
        self.column_pixel_3 = column_pixel_3
        self.column_pixel_4 = column_pixel_4
        self.row_pixel_1 = row_pixel_1
        self.row_pixel_2 = row_pixel_2
        self.row_pixel_3 = row_pixel_3
        self.row_pixel_4 = row_pixel_4

        self.position = 0

    def column_forward(self):
            self.column_pixel_1 += 1
            self.column_pixel_2 += 1
            self.column_pixel_3 += 1
            self.column_pixel_4 += 1

    def column_backward(self):
            self.column_pixel_1 -= 1
            self.column_pixel_2 -= 1
            self.column_pixel_3 -= 1
            self.column_pixel_4 -= 1

    def row_backward(self):
            self.row_pixel_1 -= 1
            self.row_pixel_2 -= 1
            self.row_pixel_3 -= 1
            self.row_pixel_4 -= 1

    def row_forward(self):
            self.row_pixel_1 += 1 
            self.row_pixel_2 += 1 
            self.row_pixel_3 += 1 
            self.row_pixel_4 += 1    

    def move_right(self):
        match self.position:
            case 0:
                if self.column_pixel_2 <= len(board[0]) - 2:
                    self.column_forward()
            case 1:
                if self.column_pixel_4 <= len(board[0]) - 2:
                    self.column_forward()
            case 2:
                if self.column_pixel_1 <= len(board[0]) - 2:
                    self.column_forward()
            case 3: 
                if self.column_pixel_1 <= len(board[0]) - 2:
                    self.column_forward()
                
    def move_left(self):
        match self.position:
            case 0:
                if self.column_pixel_1 >= 1:
                    self.column_backward()
            case 1:
                if self.column_pixel_1 >= 1:
                    self.column_backward()
            case 2:
                if self.column_pixel_2 >= 1:
                    self.column_backward()
            case 3:
                if self.column_pixel_4 >= 1:
                    self.column_backward()

    def move_down(self):
        match self.position:
            case 0:
                if self.row_pixel_1 <= len(board) - 2:
                    self.row_forward()
            case 1:
                if self.row_pixel_2 <= len(board) - 2:
                    self.row_forward()
            case 2:
                if self.row_pixel_4 <= len(board) - 2:
                    self.row_forward()
            case 3:
                if self.row_pixel_1 <= len(board) - 2:
                    self.row_forward()


    def turn_right(self):
        match self.position:
            case 0:
                if self.column_pixel_4 <= len(board[0]) - 2:
                    self.row_pixel_1 -= 1
                    self.column_pixel_2 -= 1
                    self.row_pixel_3 += 1
                    self.column_pixel_4 += 1
                    self.row_pixel_4 += 2
                    self.position_up()

            case 1:
                if self.row_pixel_1 >= 1:
                    self.row_pixel_1 -= 1
                    self.column_pixel_1 += 1
                    self.row_pixel_2 -= 2
                    self.column_pixel_3 -= 1
                    self.row_pixel_3 -= 1
                    self.column_pixel_4 -= 2
                    self.position_up()
                
            case 2:
                if self.column_pixel_1 <= len(board[0]) - 2:
                    self.row_pixel_1 += 2
                    self.column_pixel_1 += 1
                    self.column_pixel_2 += 2
                    self.row_pixel_2 += 1
                    self.column_pixel_3 += 1
                    self.row_pixel_4 -= 1
                    self.position_up()
                    
            case 3:
                if self.row_pixel_4 >= 1:
                    self.column_pixel_1 -= 2
                    self.column_pixel_2 -= 1
                    self.row_pixel_2 += 1
                    self.column_pixel_4 += 1
                    self.row_pixel_4 -= 1
                    self.position_up()


    def position_up(self):
        if self.position == 3:
            self.position = 0
        else:
            self.position += 1

    def position_down(self):
        if self.position == 0:
            self.position = 3
        else:
            self.position -= 1


class BoardMechanic:
    def __init__(self):
        self.board = board

    def fill_board(self, row: int, column: int):
        board[row][column] = 1

    


    
movements = LShape(
    column_pixel_1=column_pixel_1, column_pixel_2=column_pixel_2,
    column_pixel_3=column_pixel_3, column_pixel_4=column_pixel_4,
    row_pixel_1=row_pixel_1, row_pixel_2=row_pixel_2, 
    row_pixel_3=row_pixel_3, row_pixel_4=row_pixel_4
)

board_mechanic = BoardMechanic()

add_hotkey(Buttons.DOWN.value, movements.move_down)
add_hotkey(Buttons.RIGHT.value, movements.move_right)
add_hotkey(Buttons.LEFT.value, movements.move_left)
add_hotkey(Buttons.TURN_RIGHT.value, movements.turn_right)
"""IMPORTANT
With parentheses: movements.up_() calls the method immediately and executes its code.
Without parentheses: movements.up_ passes the method as a reference, so it can be called later."""

down_movement = 0

while True:
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear') # 'nt' = windows, 'cls' = clear

    down_movement += 1
    
    for row in range(len(board)):
        for column in range(len(board[row])):
            if row == movements.row_pixel_1 and column == movements.column_pixel_1:
                board[row][column] = '🟩'
            elif row == movements.row_pixel_2 and column == movements.column_pixel_2:
                board[row][column] = '🟩'
            elif row == movements.row_pixel_3 and column == movements.column_pixel_3:
                board[row][column] = '🟩'
            elif row == movements.row_pixel_4 and column == movements.column_pixel_4:
                board[row][column] = '🟩'
            else:
                board[row][column] = '⬜'

    for n in board:
        print(''.join(n))

    if down_movement == 15:
        movements.move_down()
        down_movement = 0

        
    print(movements.position)
    # Add a small delay to make the output readable
    time.sleep(0.1)


