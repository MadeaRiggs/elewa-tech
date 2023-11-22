#### Here Inheritance and Polymorphism will be used 

# base class
class Triangle:
    def __init__(self):
        self.base = 0
        self.base_height = 0
        self.slant_height = 0
        self.base_area = 0
        self.perimeter = 0

    def get_Base(self):
        self.base = int(input("Enter the base: "))
        return self.base

    def get_BaseHeight(self):
        self.base_height = int(input("Enter the height of base triangle: "))
        return self.base_height

    def get_SlantHeight(self):
        self.slant_height = int(input("Enter the slant height: "))
        return self.slant_height

    def get_Area(self):
        self.base_area = 0.5 * self.base * self.base_height
        return self.base_area

    def get_Perimeter(self):
        self.perimeter = 3 * self.base
        return self.perimeter

# derived class
class Pyramid(Triangle):
    def __init__(self, base, base_height, slant_height):
        super().__init__()
        self.base = base
        self.base_height = base_height
        self.slant_height = slant_height

    def render(self):
        lateral_surface_area = 0.5 * self.get_Perimeter() * self.slant_height
        print("The lateral surface area is: ", lateral_surface_area)

        total_surface_area = lateral_surface_area + self.get_Area()
        print("The total surface area is: ", total_surface_area)

        volume = 1/3 * self.get_Area() * self.base_height
        print("The volume is: ", volume)

# create objects
triangle1 = Triangle()
print(triangle1.get_Base())
print(triangle1.get_BaseHeight())
print(triangle1.get_SlantHeight())

pyramid1 = Pyramid(triangle1.base, triangle1.base_height, triangle1.slant_height)
pyramid1.render()
