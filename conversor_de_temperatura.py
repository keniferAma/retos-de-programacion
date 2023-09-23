"""/*
 * Enunciado: Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°" 
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
 * - ¿Quieres emplear lo aprendido en este reto?
 *   Revisa el reto mensual y crea una App: 
 *   https://retosdeprogramacion.com/mensuales2022
 */"""


grados_centigrados = "23°C"
grados_fahrenheit = "23°F"

def temperature_conversor(grades = None):
    
    if not grades: 
        return "None value to process."

    try:
        type = grades[-2:]
        number = int(grades[:-2])

        if type == "°F":
            return f"{grades}: {(number - 32) * (5 / 9)}°C" 
        
        elif type == "°C":
            return f"{grades}: {(number * 9 / 5) + 32}°F" 
        
    except:
        return "Must be a number."


# Version hecha por la inteligencia artificial:
# Justamente esta relacionada con algo que pensé hacer en un principio, lo cual era usar una expresión regular 
# para filtrar la entrada de la temperatura.
    
import re

def temperature_conversor(grades = None):
    if not grades: 
        return "None value to process."

    # Verificar si la entrada es válida
    if not re.match(r'^\d+°[CF]$', grades):
        return "Invalid input. Must be a number followed by '°C' or '°F'."

    try:
        type = grades[-2:]
        number = int(grades[:-2])

        if type == "°F":
            return f"{grades}: {round((number - 32) * (5 / 9), 2)}°C" 
        
        elif type == "°C":
            return f"{grades}: {round((number * 9 / 5) + 32, 2)}°F" 
        
    except ValueError:
        return "Must be a number."
print(temperature_conversor(grados_fahrenheit))
