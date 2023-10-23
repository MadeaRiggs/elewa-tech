


#######CASE STUDY 1
class Shape:

    #constructor
    def __init__(self):
        self.name= " "

    #method 1
    def perimeter(self):
        #statements
        pass
    
    #method 2
    def area(self):
        #statements
        pass

    #method 3: print statements
    def fact(self):
        #statements
        pass


#Real classes
class Circle(Shape):

    #constructor
    def __init__(self):
        self.name= " "
        self.radius= 0

    #method 1
    def CPerimeter(self):
        radius= int(input("Enter radius of circle: ", ))
        self.radius=radius
        perimeter= 3.142 * (self.radius * 2)
        print("The perimeter is: ", perimeter)

    #method 2
    def CArea(self):
        radius= int(input("Enter radius of circle: ", ))
        self.radius=radius
        area= 3.142 * self.radius *  self.radius
        print("The area is: ", area)
    
    #method 3
    def CFact(self):
        name_c= input("Enter the shape name : ", )
        self.name= name_c
        print("The shape name is: ", self.name)


#second shape
class Rectangle(Shape):

    #constructor
    def __init__(self):
        self.name= " "
        self.length= 0
        self.width= 0

    #method 1
    def RPerimeter(self):
        len= int(input("Enter length of rectangle: ", ))
        wid= int(input("Enter width of rectangle: ", ))
        self.length= len
        self.width= wid
        perimeter_r= 2 * (self.length + self.width)
        print("The perimeter is: ", perimeter_r)


    #method 1
    def RArea(self):
        len= int(input("Enter length of rectangle: ", ))
        wid= int(input("Enter width of rectangle: ", ))
        self.length= len
        self.width= wid
        area_r= self.length * self.width
        print("The area is: ", area_r)

    #method 1
    def RFact(self):
        name_r= input("Enter the shape name : ", )
        self.name= name_r
        print("The shape name is: ", self.name)


#create objects
rectangle= Rectangle()
circle= Circle()

#call method
print(rectangle.RFact())
print(rectangle.RArea())