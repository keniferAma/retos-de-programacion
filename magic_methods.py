
class MyClass:
    def __init__(self, string_value, int_value):
        self.string_value = string_value
        self.int_value = int_value

    def __add__(self, other_value):
        if isinstance(other_value, MyClass):
            return self.string_value + ' ' + other_value.string_value # the __add__ method is activated with '+' automatically
                                                  # if there are conditions
    def __len__(self):
        return len(self.string_value)
    
    def __repr__(self) -> str:
        return str(self.string_value) # Remember __repr__ should return str type.
    
    def __lt__(self, other_value):
        if isinstance(other_value, MyClass):
            return self.int_value < other_value.int_value

    
        
myclass_instance1 = MyClass('hello', 1)
myclass_instance2 = MyClass('world', 3)

print(myclass_instance1 + myclass_instance2) # Basically the __add__ is activated with '+'
"""hello world"""

print(len(myclass_instance1)) # Here takes in action __len__ when we use len(<instance>)


print(myclass_instance1 < myclass_instance2)
"""TypeError: '<' not supported between instances of 'MyClass' and 'MyClass'""" # with __lt__ not implemented (<, >, are the trigger)
"""False""" # when __lt__ is implemented


class AnotherClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, another_value):
        return another_value
    
    def __repr__(self):
        return str(self.value)
    

anotherclass_instance1 = AnotherClass(1)
anotherclass_instance2 = AnotherClass(2)

print(anotherclass_instance2 + anotherclass_instance1) # The position in which we operate is REELEVANT
