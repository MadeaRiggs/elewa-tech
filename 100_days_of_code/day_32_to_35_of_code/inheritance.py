##########INHERITANCE IN PYTHON

#########CASE STUDY 1
#creating base class
# class Person:
#     #creating a constructor
#     #the parameters are Attributes but they are initialized to become rules
#     def __init__(self, name, age):
#         self.name= name
#         self.age= age

#     #method to get the name
#     def getName(self):
#         return self.name
    
#     #method to get the age
#     def getAge(self):
#         return self.age 

# #derived class: Education 
# class Education(Person):

#     def isEducated(self):
#         return True

# #create an object
# person_1= Person("Mukami Kami", 20)
# person_1= Education("Mukami Kami", 20)   

# #print statements
# print(person_1.isEducated())
# print(person_1.getAge())
    

###########CASE STUDY 2
# class Electric_shop():

#     #constructor
#     def __init__(self, pd_name, quantity, price) :
#         self.name= pd_name
#         self.quantity= quantity
#         self.price= price

# class Methods(Electric_shop):

#     #method 1
#     def getName(self):
#         return self.name
    
#     def getQuantity(self):
#         Quantity= int(input("Please input quantity: ", ))
#         self.quantity= Quantity
#         return self.quantity
    
#     #method 3
#     def getPrice(self):
#         cost= int(input("Enter the cost: ", ))
#         self.price= self.quantity * cost 
#         return self.price
    
# #object methods
# Laptop= Methods("Hewlett Parker", 0, 0)
# print(Laptop.getQuantity())
# print(Laptop.getPrice())  


########CASE STUDY 3- USING super() class
# class Electric_shop():

#     #constructor
#     def __init__(self, pd_name, quantity, price) :
#         self.name= pd_name
#         self.quantity= quantity
#         self.price= price

# #derived class 1
# class name(Electric_shop):

#     #constructor (s stands for super) Super class is when a child/derived class can be inherited from
#     def __init__(self, pd_name, quantity, price) :
#         self.sname= pd_name
#         self.squantity= quantity
#         self.qprice= price

#     #method 1
#     def getName(self):
#         name= input("Enter the device name: ", )
#         self.name= name
#         return self.name
    
# #derived class 2
# class laptop(name):

#     #method 1
#     def getPrice(self):
#         price= int(input("Enter the price: ", ))
#         self.sprice= price 
#         return self.sprice
    

# #create object
# # lappy= laptop("Asus", 0, 0)

# #####OR 
# #the quotes are just used to show that there is memory allocation for the name attribute
# lappy= laptop(" ", 0, 0)

# print(lappy.getPrice())
# print(lappy.getName())


#########CASE STUDY 3
####Creating a class that holds properties only
#inherit the properties to create methods 
class Fruit:
    def __init__(self, name, color, price):
        self.name= name
        self.color= color
        self.price= price

class info(Fruit):
    
    #method 1
    def getName(self):
        return self.name
    
    #method 2
    def getColor(self):
        color= input("Enter fruit color: ", )
        self.color= color
        return self.color
    
    #method 3
    def totalPrice(self):
        cost= int(input("Enter price of one ", ))
        num= int(input("Enter the total number of fruits bought ", ))
        total= cost * num
        self.price= total
        return self.price
    
# #create an object
# banana= info("Banana", " ", 0)

# print(banana.totalPrice())

#hardcoding the methods
fruit_1= Fruit(" ", " ", 0)
fruit_1_name= input("Enter the name: ", )
fruit_1_name = fruit_1_name

print(fruit_1_name)
