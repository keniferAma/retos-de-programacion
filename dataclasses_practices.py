from dataclasses import dataclass


@dataclass(order=True) #Allows the order 'magic' methods __lt__, __gt__, __ge__ ...but comparing all the attributes
# if we needed to compare only the age for example, we're gonna need to set the magics methods for
# the specific field we want to compare.
class Person:
    name: str
    age: int

kenifer = Person(name='kenifer', age=32)
alejandro = Person(name='alejandro', age=53)


print(kenifer > alejandro)
