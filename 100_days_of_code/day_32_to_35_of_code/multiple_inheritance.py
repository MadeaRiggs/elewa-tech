##########INHERITANCE IN PYTHON
#Multiple inheritance- inheriting from more than 1 base class

########CASE STUDY 1: SHOPPING CENTER
class Supermarket:

    #constructor
    def __init__(self, grocery, detergents, bakery):
        self.grocery= grocery
        self.detergent= detergents
        self.bakery= bakery

    #method to get the name
    def getGrocery(self):
        groc= input("Enter the grocery of your choice: ", )
        self.grocery= groc
        return self.grocery
    
    #method to get the name
    def getDetergent(self):
        deter= input("Enter the detergent of your choice: ", )
        self.detergent= deter
        return self.detergent
    
    #method to get the name
    def getBakery(self):
        bake= input("Enter the confectionary of your choice: ", )
        self.bakery= bake
        return self.bakery
    

#base class 2
class Shop:
    #constructor
    def __init__(self, toiletry, crockery):
        self.toiletry= toiletry
        self.crockery= crockery
        
    #method to get the name
    def getStuff(self):
        toilet_s= input("Enter your toiletries essentials: ", )
        self.toiletry= toilet_s
        
        crock= input("Enter the crockery of your choice: ", )
        self.crockery= crock
        return (self.crockery + self.toiletry)
    

#derived class
class shopping(Supermarket, Shop):
    #constructor
    def __init__(self):
        Supermarket.__init__(self, ' ', ' ', ' ')
        Shop.__init__(self, ' ', ' ')

    #method to get the name
    def getList(self):
        print(self.grocery)
        print(self.detergent)
        print(self.bakery)
        print(self.crockery)
        print(self.toiletry)

#create objects
shopping= shopping()

#call methods
print(shopping.getGrocery())
print(shopping.getDetergent())
print(shopping.getBakery())
print(shopping.getStuff())
print(shopping.getList())