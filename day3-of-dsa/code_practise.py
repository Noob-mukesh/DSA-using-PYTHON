class Person:# class name Person
    std="sixth" #class variable

    def __init__(self,name):
        self.name=name # instance variable
    def showdetails(self): #instance method
        
        return f"My name is {self.name} and I`m Studying in {self.std}"
boy1=Person("Mukesh") #objects name boy1
# print(boy1.showdetails())

class Person:# class name Person
    std="sixth" #class variable

    def __init__(self,name):
        self.name=name # instance variable
        
    def showdetails(self): #instance method
        return f"My name is {self.name} and I`m Studying in {self.std}"
    
    @classmethod
    def change_std(cls,std):
        cls.std=std
        
        
boy1=Person("Mukesh") #objects name boy1
#Person.change_std("12th") # by class name 
boy2=Person("himanshu")
boy1.change_std("12th") # by instance  of the class

# print(boy1.showdetails())
# print(boy2.showdetails())


#  STATIC method

class Person:
    std="sixth" 

    def __init__(self,name):
        self.name=name 
        
    def showdetails(mukesh): 
        return f"My name is {mukesh.name} and I`m Studying in {mukesh.std}"
    
    @staticmethod #take no self argumenents
    def knowledge():
        return "Expert in Python"
        
        
boy1=Person("Mukesh") #
#Person.change_std("12th") 
print(Person.knowledge()) # class method
print(boy1.knowledge()) # static method
print(boy1.showdetails())



