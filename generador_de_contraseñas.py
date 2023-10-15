"""/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */"""


import random
import string



def pasword_generator(amount: int, lower=None, upper=None, numbers=None, characters=None):
    if amount < 8 or amount > 16:
        return "Must be numbers between 8 and 16"
    
    if lower == "y" and upper == "y" and numbers == "y" and characters == "y":
        return "".join(random.choices(string.printable, k=amount))
    
    elif lower == "y" and upper == "n" and numbers == "n" and characters == "n":
        return "".join(random.choices(string.ascii_lowercase, k=amount))
    
    elif lower == "n" and upper == "y" and numbers == "n" and characters == "n":
        return "".join(random.choices(string.ascii_uppercase, k=amount))
    
    elif lower == "n" and upper == "n" and numbers == "y" and characters == "n":
        return "".join(random.choices(string.digits, k=amount))
    
    else:
        "Not allowed"

amount_of_characters = int(input("Amount of characters: "))
lower = input("¿Lowercase? (Y/N): ")
upper = input("¿Uppercase? (Y/N): ")
numbers = input("¿Numbers? (Y/N): ")
characters = input("¿Special characters? (Y/N): ") 
    
print(pasword_generator(amount_of_characters, lower=lower, upper=upper, numbers=numbers, characters=characters))



