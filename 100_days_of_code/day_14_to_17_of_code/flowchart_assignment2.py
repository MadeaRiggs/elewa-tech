########Question 1
salary= int(input("Enter your salary "))
budget= int(input("Enter your budget "))
expe1= int(input("Enter your expense1 "))
expe2= int(input("Enter your expense2 "))
expe3= int(input("Enter your expense3 "))

total_expe= expe1 + expe2 + expe3
if (total_expe > budget):
    print("Reduce expenses")
else:   
    print("Pay all expenses")
    savings= budget - total_expe
    print(savings)

print("budget= ", budget, "total expenses= ", total_expe, "and savings= ", savings)


#########Question 2
import math

shape = input("Enter shape (rectangle/rectangular tank/circle/cylindrical tank): ")

if shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    perimeter = 2 * (length + width)
    print("The perimeter is:", perimeter)
elif shape == "rectangular tank":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    surface_area = 2 * ((length * width) + (length * height) + (width * height))
    volume = length * width * height
    print("The surface area is:", surface_area)
    print("The volume is:", volume)
elif shape == "circle":
    radius = float(input("Enter radius: "))
    perimeter = 2 * math.pi * radius
    print("The perimeter is:", perimeter)
elif shape == "cylindrical tank":
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))
    surface_area = 2 * math.pi * radius * (radius + height)
    volume = math.pi * radius ** 2 * height
    print("The surface area is:", surface_area)
    print("The volume is:", volume)
else:
    print("Invalid shape.")


#######Question 3
import math

cone_r = 4.9
scoop1_r = 5.6
scoop2_r = 7.0

cone_h = math.sqrt(scoop1_r ** 2 - cone_r ** 2)
cone_v = (1/3) * (22/7) * cone_r ** 2 * cone_h
cone_sa = (22/7) * cone_r * (cone_r + math.sqrt(cone_r ** 2 + cone_h ** 2))

print("Cone Surface area= ", cone_sa, "and the Cone volume= ", cone_v)


##########Question 4
salary = float(input("Enter basic salary: "))
monday_at = input("Enter Monday arrival time (HH:MM): ")
tuesday_at = input("Enter Tuesday arrival time (HH:MM): ")
wednesday_at = input("Enter Wednesday arrival time (HH:MM): ")
thursday_at = input("Enter Thursday arrival time (HH:MM): ")
friday_at = input("Enter Friday arrival time (HH:MM): ")

if monday_at <= "09:30" and tuesday_at <= "09:30" and wednesday_at <= "09:30" and thursday_at <= "09:30" and friday_at <= "09:30":
    raise_amount = 0.55 * salary
    print("The raise amount is:", raise_amount)
else:
    print("No raise")


#########Question 5
basic_needs = ["Food", "Shelter", "Clothing"]
secondary_needs = ["Wi-Fi", "Games"]
salary = 300000
budget = 250000
total_cost = 270000
mysavings = budget - total_cost

if total_cost > budget:
    print("Prioritize basic needs")
    print(basic_needs)
else:
    print("Pay all expenses")
    print("Savings:", mysavings)

print("Budget =", budget, "Total expenses =", total_cost, "and Savings =", mysavings)

