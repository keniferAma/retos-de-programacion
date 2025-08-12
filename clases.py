"""/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */"""


class Exercise:
    counter = 0

    def __init__(self, entry: str):
        self.entry = entry
        Exercise.counter += 1

    def __repr__(self) -> str:
        return f'{self.entry}'
    


prove = Exercise('hello')
print(prove)
         
prove_2 = Exercise('hello_2')
print(prove_2.counter)


# extra #

class Pila:

    def __init__(self):
        self.lista = []

    def adding(self, value):
        self.lista.append(value)

    def substrating(self):
        self.lista.pop()

    def size(self):
        return len(self.lista)

    def __repr__(self):
        return str(self.lista)
    

example_1 = Pila()

example_1.adding(1)
print(example_1)
example_1.adding(3)
print(example_1)
example_1.adding(76)
print(example_1)
example_1.adding(8)
print(example_1)
example_1.adding(90)
print(example_1)
example_1.substrating()
print(example_1)
print(example_1.size())
        


from dataclasses import dataclass

@dataclass
class Account:
    account_holder: str
    deposit: int

    def add_founds(self, amount: int):
        self.deposit += amount

    def withdraw(self, amount: int):
        if amount <= self.deposit:
            self.deposit -= amount
        else:
            f'insuficient founds in deposit'

    def __lt__(self, other: 'Account'):
        return other.deposit > self.deposit # based on the instance position.
    
    def __add__(self, other: 'Account'):
        return other.deposit + self.deposit
    

kenifer = Account(account_holder='kenifer', deposit=250000)
camilo = Account(account_holder='camilo', deposit=300000)


kenifer_n_camilo_total = kenifer + camilo


print(kenifer_n_camilo_total)
print(camilo < kenifer)

kenifer.add_founds(200000)

print(camilo < kenifer)

