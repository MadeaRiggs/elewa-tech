#########Question 2
target_savings = 5000
savings = 0

# a)Saving money
while savings < target_savings:
    savings += 500  # Save a fixed amount each iteration
else:
    print("Congratulations! You've saved enough to purchase electronics which is ", savings)

    # b)Choosing electronics
    if savings >= 6000:  # Savings for 3 electronics
        print("You can purchase 3 electronics")
    elif savings >= 4000:  # Savings for 2 electronics
        print("You can purchase 2 electronics")
    else:
        print("You can't afford to purchase any electronics with your savings.")

print("End of the process")
