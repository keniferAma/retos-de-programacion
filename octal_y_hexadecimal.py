"""/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */"""


def decimal_a_octal_y_hexadecimal(decimal: int) -> str:
    decimal_1 = decimal
    decimal_2 = decimal

    if decimal_1 == 0 or decimal_2 == 0:
        return "0"

    hexadecimal = []
    octal = []

    while decimal_1> 0:
        residuo = decimal_1 % 16

        if residuo == 10:
            hexadecimal.append("A")
        elif residuo == 11:
            hexadecimal.append("B")
        elif residuo == 12:
            hexadecimal.append("C")
        elif residuo == 13:
            hexadecimal.append("D")
        elif residuo == 14:
            hexadecimal.append("E")
        elif residuo == 15:
            hexadecimal.append("F")
        else:
            hexadecimal.append(str(residuo))
        

        decimal_1 //= 16 

    while decimal_2 > 0:
        residuo = decimal_2 % 8
        octal.append(str(residuo))
        decimal_2 //= 8


    return f'Hexadecimal= {"".join(hexadecimal[::-1])}, Octal={"".join(octal[::-1])}'

print(decimal_a_octal_y_hexadecimal(10))



# IA version (version con 2 funciones por separado)#

def decimal_to_octal(decimal):
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    return octal

def decimal_to_hexadecimal(decimal):
    hex_digits = '0123456789ABCDEF' # notese como se ahorra las condicionales mediante la búsqueda de su residuo
    hexadecimal = ''
    while decimal > 0:
        hexadecimal = hex_digits[decimal % 16] + hexadecimal
        decimal = decimal // 16
    return hexadecimal


# IA version (version con una funcion) #

def decimal_to_octal_hexadecimal(decimal):
    def decimal_to_octal(decimal):
        octal = ''
        while decimal > 0:
            octal = str(decimal % 8) + octal
            decimal = decimal // 8
        return octal

    def decimal_to_hexadecimal(decimal):
        hex_digits = '0123456789ABCDEF'
        hexadecimal = ''
        while decimal > 0:
            hexadecimal = hex_digits[decimal % 16] + hexadecimal
            decimal = decimal // 16
        return hexadecimal

    return decimal_to_octal(decimal), decimal_to_hexadecimal(decimal)
