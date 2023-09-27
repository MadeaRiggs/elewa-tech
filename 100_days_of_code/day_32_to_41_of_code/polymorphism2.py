##########SECOND EXAMPLE OF POLYMORPHISM

#Base class
class animal:

    #constructor
    def __init__(self):
        self.movement = " "
        self.sound = " "
        self.name = " "

#form 1
class Cat(animal):

    def getName(self):
        name=input("Enter name of cat: ", )
        self.name= name
        return self.name

#form 2  
class Dog(animal):

    def getName_2(self):
        name_2=input("Enter name of dog: ", )
        self.name= name_2
        return self.name
    
#form 3  
class Parrot(animal):

    def getName_3(self):
        name_3=input("Enter name of parrot: ", )
        self.name= name_3
        return self.name
    

#object creation
cat= Cat()
dog= Dog()
parrot= Parrot()

#call method
print(cat.getName())
print(dog.getName_2())
print(parrot.getName_3())