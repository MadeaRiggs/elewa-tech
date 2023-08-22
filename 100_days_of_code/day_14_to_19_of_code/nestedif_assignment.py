##########Question 1
account= "existing"
deposit = 500
balance = 800

if (account == "new") :
    print("Create a new account")
    if (deposit >= 500) :
        print("Account created successfully")
    else :
        print("Increase deposit amount")

else :
    print("Accept withdrawal request")
    if (balance > 1000) :
        print("Withdraw money")
    else :
        print("Insufficient funds")


##########Question 2
distance = 1000
level = "high school"
type = "boarding"
budget = 35000


if (level == "primary") :
    if (type == "boarding") :
        shopping_cost= 20000
        if (distance >= 500) :
            transport_cost = 2000
        else :
            transport_cost = 1500
        total_cost = shopping_cost + transport_cost
        print("The level is ", level, "type is ", type, "distance is ", distance, "and total cost is ", shopping_cost)
    else :
        shopping_cost= 10000
        if (distance >= 10) :
            transport_cost = 1200
        else :
            transport_cost = 1000
        total_cost = shopping_cost + transport_cost
        print("The level is ", level, "type is ", type, "distance is ", distance, "and total cost is ", shopping_cost)

elif (level == "high school") :
    if (type == "boarding") :
        shopping_cost= 25000
        if (distance >= 500) :
            transport_cost = 2000
        else :
            transport_cost = 1500
        total_cost = shopping_cost + transport_cost
        print("The level is ", level, "type is ", type, "distance is ", distance, "and total cost is ", shopping_cost)

    else :
        shopping_cost= 10000
        if (distance >= 10) :
            transport_cost = 1200
        else :
            transport_cost = 1000
        total_cost = shopping_cost + transport_cost
        print("The level is ", level, "type is ", type, "distance is ", distance, "and total cost is ", shopping_cost)

else :
    if (type == "boarding") :
        shopping_cost= 30000
        if (distance >= 500) :
            transport_cost = 2000
        else :
            transport_cost = 1500
        total_cost = shopping_cost + transport_cost
        print("The level is ", level, "type is ", type, "distance is ", distance, "and total cost is ", shopping_cost)

    else :
        shopping_cost= 10000
        if (distance >= 10) :
            transport_cost = 1200
        else :
            transport_cost = 1000
        total_cost = shopping_cost + transport_cost
        print("The level is ", level, "type is ", type, "distance is ", distance, "and total cost is ", shopping_cost)


#########Question 3
arrival= "late"
guests = 100
weather = "sunny"

if (weather == "sunny") :
    theme = "outdoors"
    print("Activity will be done ", theme)
    if (guests >= 150):
        print("Buy a large tent")
    else :
        print("Buy a medium tent")
        if (arrival == "early") :
            print("Start and finish event early")
        else :
            print("Start and finish event late")
else :
    theme = "indoors"
    print("Activity will be done ", theme)
    if (guests >= 150):
        print("Use a multipurpose hall")
    else :
        print("Use a normal hall")
        if (arrival == "early") :
            print("Start and finish event early")
        else :
            print("Start and finish event late")
