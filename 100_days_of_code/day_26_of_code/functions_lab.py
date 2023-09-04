######Case study 1
def defineOutput():
    print("This is my first function")

#first way to call function: Call by using function name
defineOutput()

#second way to call function: Call by assigning function to variable
x= defineOutput()
print(x)


#######Case study 2: calculate area of triangle
base= 25
height= 16

#function
def triangleArea():
    area = 0.5 * base *height
    print(area)

triangleArea()


#######Case study 3: function that prints 3 statements
statementA= "I'm tired"
statementB= "Take coffee"
statementC= "Go to sleep"
statementD= "The weekend was long"

# function
def statement():
    a= statementA + statementB
    b= statementB + statementC
    c= statementC + statementD

    print(a)
    print(b)
    print(c)

statement()


######Budget tracker project- input, logic, process and output
salary= int(input("Enter your income: "))
side_hustle= int(input("Enter your side hustle income: "))

#Expenses
utility= int(input("Enter your utility bills: "))
grocery= int(input("Enter your grocery bill: "))
allowances= int(input("Enter your allowances: "))

#Goals
goal1= "Improve code setup"
goal2= "Go on a vacation"
goal3= "Start a business"
goal4= "Education bills"
mygoal= goal1

#logic
if (mygoal == goal1):
    new_income= salary + side_hustle

    if (new_income >= 40000):
        expense_net= new_income * 0.5
        allowance_net= new_income * 0.3
        savings_net= new_income * 0.2
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)

    elif (new_income >= 50000):
        expense_net= new_income * 0.3
        allowance_net= new_income * 0.3
        savings_net= new_income * 0.3
        leisure_net= new_income * 0.1
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)

    else:
        print("Sorry, your income category is not listed")

elif (mygoal == goal2):
    new_income= salary + side_hustle

    if (new_income >= 40000):
        expense_net= new_income * 0.5
        allowance_net= new_income * 0.3
        savings_net= new_income * 0.2
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)

    elif (new_income >= 50000):
        expense_net= new_income * 0.3
        allowance_net= new_income * 0.3
        savings_net= new_income * 0.3
        leisure_net= new_income * 0.1
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)

    else:
        print("Sorry, your income category is not listed")

elif (mygoal == goal3):
    new_income= salary + side_hustle

    if (new_income >= 40000):
        expense_net= new_income * 0.5
        allowance_net= new_income * 0.3
        savings_net= new_income * 0.2
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)

    elif (new_income >= 50000):
        expense_net= new_income * 0.3
        allowance_net= new_income * 0.3
        savings_net= new_income * 0.3
        leisure_net= new_income * 0.1
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)

    else:
        print("Sorry, your income category is not listed")

else :
    new_income= salary + side_hustle

    if (new_income >= 40000):
        expense_net= new_income * 0.5
        allowance_net= new_income * 0.3
        savings_net= new_income * 0.2
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)

    elif (new_income >= 50000):
        expense_net= new_income * 0.3
        allowance_net= new_income * 0.3
        savings_net= new_income * 0.3
        leisure_net= new_income * 0.1
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)

    else:
        print("Sorry, your income category is not listed")

print("My goal is ", goal1)
