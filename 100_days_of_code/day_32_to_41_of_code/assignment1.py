########OOP QUESTION 4
#Imagine you are a new programmer in a company. The department you have been hired to work at is the human resource department. 
#Using OOP concepts to write code on how you will be managing the Employee details.

#creating class
class Employee:

    #constructor
    def __init__(self):
        self.name= " "
        self.age= " "
        self.department= " "
        self.salary= 0
    
    #method 1
    def getName(self):
        name= input("Enter your name: ", )
        self.name= name
        return self.name

    #method 1
    def getName(self):
        name= input("Enter your name: ", )
        self.name= name
        return self.name
    
    #method 2
    def getAge(self):
        age= int(input("Enter your age: ", ))
        self.age= age
        if (age > 60):
            status= print("It is time to retire")
        else:
            status= print("You can continue to work")

        print(self.age, status)
    
    #method 3
    def getDepartment(self):
        dept= input("Enter the department you work in: ", )
        self.department= dept
        return self.department
    
    #method 4
    def getSalary(self):
        experience= int(input("Enter years of experience: ", ))
        if (experience <= 2):
            sal= 50000
        elif (experience > 2 and experience <= 5 ):
            sal= 70000
        else:
            sal= 100000
        self.salary= sal
        print("The salary due is ", self.salary)
    

#creating object
emp_details= Employee()

#calling methods
print(emp_details.getName())
print(emp_details.getAge())
print(emp_details.getDepartment())
print(emp_details.getSalary())