########### IF STATEMENTS
age= 17

if (age >= 18):
    print("You are an adult")

print("You are underage")

############ IF ELSE STATEMENT
hse_a= 10000
hse_b= 15000
budget= 12000

if (budget<= 12000):
    print(hse_a, "House is affordable")
else: 
    print(hse_b, "House is expensive")

#reasons it is not outputing the else statement which is correct logically speaking
#1) The strings have different memory space so in this case, "8 months" is larger than "1 year"
#2) The computer does not understand it logically

age= "8 months"

if (age >= "1 year"):
    print("You can stop breastfeeding")
else :
    print("breast milk is a must")