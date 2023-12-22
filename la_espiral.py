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
    turn_reduction = 0
    turn_reduction_negative = - 1
    while amount > 0:
        if direction == 1 or direction == 2:
            for i in range(1, amount):
                if direction == 1:
                    if i != amount:
                        empty_list[turn_reduction][i] = '═'
                    else:
                        empty_list[turn_reduction][i] = '╗'   
                
                elif direction == 2:
                    if i != amount:
                        empty_list[i][turn_reduction_negative] = '║'
                    else:
                        empty_list[i][turn_reduction_negative] = '╝' 

        else:
            for i in range(amount - 1, -1, -1):
                if direction == 3:
                    if i != 0:
                        empty_list[turn_reduction_negative][i] = '═'
                    else:
                        empty_list[turn_reduction_negative][i] = '╚'   
                
                elif direction == 4:
                    if i != amount:
                        empty_list[i][turn_reduction] = '║'
                    else:
                        empty_list[i][turn_reduction] = '╔' 

        if direction == 4:
            direction = 1
            amount -= 1

        direction += 1
        pares += 1

        if pares % 4 == 0:
            turn_reduction += 1
            turn_reduction_negative -= 1

        if direction % 2 != 0:
            amount -= 1
        

    for m in empty_list:
        print(" ".join(m))


espiral(7)


## probing inmutable data ##
original_number = 1
copy = original_number
for i in range(0, 12):
    original_number += 1

print(original_number)
print(copy)
"""
13
1
"""
"""
A few lines to probe that data as integers are INMUTABLE, that means that once the've created will not change
in a copy variable. In this group are tuples, integers, strings, floats.
On the other hand we have the MUTABLE ones, which can be modified EVEN if they are as a copy. In this 
group are the lists and dictionaries.
"""



class spiral():
    def __init__(self, num: int):
        self.lado = ["═", "╗", "║", "╝", "╚", "╔"]
        self.num = num
        self.mitad = (self.num + 1) // 2

    def inicio(self):
        if self.num > 1:
            for x in range(self.mitad):
                if x == 0:
                    print(f"{self.lado[0] * (self.num - 1)}{self.lado[1]}")
                else:
                    print(f"{self.lado[2] * (x - 1)}{self.lado[5]}{self.lado[0] * (self.num - (x * 2) - 1)}{self.lado[1]}{self.lado[2] * x}")
            for y in range(self.mitad, self.num):
                print(f"{self.lado[2] * (self.num - (1 + y))}{self.lado[4]}{self.lado[0] * ((y * 2) - self.num)}{self.lado[3]}{self.lado[2] * (self.num - (1 + y))}")
        else:
            print("═")

def main():
    try:
        print("Dibujar Espiral")
        numero = int(input("Ingrese el tamaño del lado: "))
        if numero > 0:
            dibujo = spiral(numero)
            dibujo.inicio()
        else:
            print("Ingrese números mayores a 0")
    except:
        print('Ingreses solo números enteros')

if __name__=="__main__":
    main()

print(7//2)