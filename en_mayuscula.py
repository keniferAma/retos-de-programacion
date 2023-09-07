"""/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */"""

# The idea was to create it without any function that do the same automatically.
string = "hola mundo, es un placEr "


def in_uppercase(string):
    string = string.lower()
    new_string = ""
    for letra in string.split():
        new_string += " " + letra[0].swapcase() + letra[1:]
   
    return new_string.strip()

print(in_uppercase(string))
    

