"""/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */"""


class Animal:
    def sound(self):
        return "Generic sound"
    
class Dog(Animal):
    def sound(self):
        return "guau"
    
class Cat(Animal):
    def sound(self):
        return "miau"

animal = Cat() # The methods have the same name, so the child will override the father class method that has the same name. THAT IS POLIMORPHISM.
animal_2 = Dog()
animal_3 = Animal()

print(animal.sound())
print(animal_2.sound())
print(animal_3.sound())


# Optional #

class Person:
    def __init__(self, name: str, surname: str, age: int, email: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email


class Employee(Person):
    def __init__(self, name, surname, age, email, carnet_number: int):
        super().__init__(name, surname, age, email)
        self.carnet_number = carnet_number

    def role(self):
        return "managing the machines"
    
    def register_entrance(self):
        return "entrance"
    
    def register_exit(self):
        return "exit"
    
class BusinessManager(Employee):
    def __init__(self, name, surname, age, email, carnet_number, employees=False):
        super().__init__(name, surname, age, email, carnet_number)
    
        if employees:
            self.lista = []

    def add_employee(self, employee: Person):
        self.lista.append(employee)
        return "employee added correctly"


    def delete_employee(self, employee_name: str):
        for index, item in enumerate(self.lista):
            if item == employee_name:
                del self.lista[index]


    def display_employees(self):
        return self.lista

    def role(self): # with this class the role has been overwritten. that is polymorphism.
        return "leadering the company"
    
    
class Developer(Employee):
    def __init__(self, name, surname, age, email, carnet_number):
        super().__init__(name, surname, age, email, carnet_number)

    def role(self):
        return "develop the company systems"
    
class Owner(Person):
    def __init__(self, name, surname, age, email):
        super().__init__(self, name, surname, age, email)
    


Juan = Developer('Juan', 'Hetfield', 45, 'james@hotmail.com', 1234)
print(Juan.role())
print(Juan.register_entrance())

Alejandro = Employee('Alejandro', 'Carmona', 23, 'alecar@gmail.com', 1432)
print(Alejandro.role())

Carlos = BusinessManager('Carlos', 'hortua', 34, 'Carlos@gmail.com', 786, True)
print(Carlos.add_employee('fidel'))