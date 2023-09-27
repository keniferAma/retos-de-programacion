"""/*
 * Enunciado: Este es un reto especial por Halloween.
 * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
 * o Trato" y un listado (array) de personas con las siguientes propiedades:
 * - Nombre de la niña o niño
 * - Edad
 * - Altura en centímetros
 *
 * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
 * siguiendo estos criterios:
 * - Un susto por cada 2 letras del nombre por persona
 * - Dos sustos por cada edad que sea un número par
 * - Tres sustos por cada 100 cm de altura entre todas las personas
 * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
 *
 * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
 * siguiendo estos criterios:
 * - Un dulce por cada letra de nombre
 * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
 */"""


import pydantic
import random


class Person(pydantic.BaseModel):
    name: str
    age: int
    size: int


jose = Person(name="jose", age=12, size=156)
alejandro = Person(name="alejandro", age=14, size=134)
fernando = Person(name="fernando", age=15, size=143)


niños = [jose, alejandro, fernando]

def truco_o_trato(*, niños: list, truco_o_trato: str):
    sustos = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
    dulces = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]
    n = len(niños)
    
    if truco_o_trato == "truco": 
        result = [] 
        numero_de_sustos = 0
        altura = 0
        for i in range(n):    
            numero_de_sustos += len(niños[i].name) // 2
            altura += niños[i].size
            if niños[i].age % 2 == 0:
                numero_de_sustos += 2
        numero_de_sustos += 3 * (altura // 100)

        return random.choices(sustos, k=numero_de_sustos)
            

print(truco_o_trato(niños=niños, truco_o_trato="truco"))  


        


    
