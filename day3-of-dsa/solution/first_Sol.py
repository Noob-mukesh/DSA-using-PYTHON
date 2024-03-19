class Person:
    def __init__(self, name, age):
        self.name = name #instance variables
        self.age = age #instance variables
    def show(self): # instance method
        return f"{self.name} is {self.age} years old."
person1 = Person("John", 30)
print(person1.show())