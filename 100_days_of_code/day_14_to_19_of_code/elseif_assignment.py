##########Question 1
budget = 1500

supper = "pilau"
ingredients_cost= int(input("Enter cost of ingredients "))
remaining_budget= budget - ingredients_cost

if ingredients_cost < budget:
    print("You can add other ingredients")

elif ingredients_cost == budget:
    print("Buy all the selected ingredients")
     
else:
    print("Remove some ingredients or increase budget")

print("Remaining Budget: ", remaining_budget)


########Question 2
total_budget = 1100
activity = input("Do you want to attend the movies or go for sports? ")
cost= int(input("Enter ticket cost "))

if (activity == "movies" and cost <= total_budget):
    print("Purchase movie ticket", cost)
    total_budget -= 1000

elif (activity == "sports" and cost <= total_budget):
    print("Purchase sports ticket", cost)
    total_budget -= 1500
else:
    print("Select different activity or increase your budget")

print("Cost of ", activity, " ticket is", cost)


######Question 3
floor_state= input("Enter state of house floor whether dry, wet or clean ")

if (floor_state == "wet"):
    order= "Mop the house first, then do dishes and laundry"

elif (floor_state == "dry"):
    order= "Do the dishes first then laundry and mop house"

else :
    order= "No need to mop floor, Do the dishes first then laundry"

print("The current house floor state is ", floor_state, "and the order of chores to be done is ", order)