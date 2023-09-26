################Perform methods, class operations and constructors

#########CASE STUDY 1
class Person:
    #creating a constructor
    #the parameters are Attributes but they are initialized to become rules
    def __init__(self, name, age, id_number):
        self.name= name
        self.age= age
        self.id_number= id_number

    #method to get the name
    def getName(self):
        return self.name
    
    #method to calculate age
    def getAge(self):
        new_age= self.age + 2
        #print(new_age)
        return new_age
    
    #method to get ID
    def getID(self):
        return self.id_number
    
#create an object
new_person= Person("Mukami Kami", 20, 23456789)
# new_person= Person() It is wrong depending on how you have defined your constructor

#calling onto the object methods
print(new_person.getName())
print(new_person.getAge())
print(new_person.getID())
new_person.getAge() #does NOT work

###########CASE STUDY 2
class Cars:
    def __init__(self, model, color):
        self.model= model
        self.color= color

    #method 1
    def getModel(self):
        return self.model
    
    #method 2
    def getColor(self):
        return self.color
    
#create an object
car_1= Cars("Toyota", "Twilight grey")
car_2= Cars("Audi", "White")
car_3= Cars("Mazda", "Black")

#call the object methods
print(car_1.getModel())
print(car_2.getColor())
print(car_3.getModel())


##########CASE STUDY 3
class Fruits:
    def __init__(self, shape, color, sugar_level, price):
        self.shape= shape
        self.color= color
        self.sugar_level= sugar_level
        self.price= price

    def getShape(self):
        return self.shape
    
    def getColor(self):
        return self.color
    
    def getSugar(self):
        self.sugar_level= 0
        new_level= self.sugar_level + (234/40)
        return new_level
    
    def getPrice(self):
        self.price= 0
        no_of_pieces= self.price + 14
        cost= 15
        total_price= no_of_pieces * cost
        return total_price
    
#create object
fruit_1= Fruits("Cresent", "yellow", 0, 0)
fruit_2= Fruits("Circle", "orange", 0, 0)
fruit_3= Fruits("Oval", "avocado", 0, 0)
fruit_4= Fruits("Oval", "pears", 0, 0)
fruit_5= Fruits("Oval", "yellow", 0, 0)
fruit_6= Fruits("Cylindrical", "yellow", 0, 0)

#call methods
print(fruit_1.getColor())
print(fruit_1.getPrice())
