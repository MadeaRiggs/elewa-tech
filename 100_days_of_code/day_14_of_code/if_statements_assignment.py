# Question 1
milk= int(input("Milk packets are "))
flour= int(input("Flour packets are "))
oil= int(input("Cooking oil bottles are "))

milk_cost= float(input("The cost of milk is "))
flour_cost= float(input("The cost of flour is "))
oil_cost= float(input("The cost of oil is "))

total_cost= (milk * milk_cost) + (flour * flour_cost) + (oil * oil_cost)
budget= 12000
if (total_cost > budget):
    print("Return some items to the shelf")
else:   
    print("Purchase all the items")


# Question 2
factor1 = input("Factor 1 that influences your career ")
factor2 = input("Factor 2 that influences your career ")

if (factor1.lower() == "interest" or factor2.lower() == "skills"):
    print("Career influencer")
else:
    print("Career demoralizer")


# Question 3
reason = input("What impressed you or made you want to gift someone? ")

if "birthday" in reason.lower():
    print("Consider giving them a thoughtful birthday gift.")
elif "achievement" in reason.lower():
    print("A congratulatory gift could be a great choice.")
elif "help" in reason.lower():
    print("Show your gratitude with a thank-you gift.")
else:
    print("Select a gift that aligns with the occasion or reason.")
