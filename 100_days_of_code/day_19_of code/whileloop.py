######1st While loop 
milk= 2
# milk = 10

while (milk < 10) :
    milk = milk +1
    print(milk)

#The problem is it runs and wastes memory. This can be solved by using a counter variable or adding the budget varible
counter = 5
budget = 13500
savings = 3000

while (budget < 15000 and counter <= 5) :
    savings = savings + 3000
    counter = counter + 1
    print(savings)

########2nd While loop
shopping_bg = 1500
bananas = 0
oranges = 0

while (shopping_bg >= 900) :
    shopping_bg = shopping_bg - 300
    print("The reamining shopping budget is ", shopping_bg)
    bananas = bananas + 20
    print("The bananas are ", bananas)
else:
    oranges = oranges + 20
    print("The oranges are ", oranges)
    
shower = 1
work = 1
laziness = 1
interview = 1
no_of_showers = 0

while(shower == 1 and no_of_showers > 2):
    no_of_showers = no_of_showers + 1
    if(work == 1 and laziness == 1):
        if(interview == 1):
            print("Go take a shower!")
        else:
            print("You can decide not to take a shower")
    else:
        print("Shower and Stay in the house")

else:
    if(laziness == 1 and interview == 1):
        if(shower == 1):
            print("Go take a shower.")
        else:
            print("Stay untidy")
    else:
        print("Become a couch potato")



time = "morning"
bal = 3400
deposit = 2500
max
location = "Nairobi"
withdrwl_amt = 500

while(bal <= 1000 and location == "Nairobi"):
   if(bal < 1000):
      bal = bal + deposit
      print(bal)
   elif (bal > 1000):
      bal = bal - withdrwl_amt
      print(bal)
      print("You have withdrawn.")