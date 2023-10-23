################HOUSE HUNTING APP
####### INPUT: house(type, number of bedrooms, location, cost)

#######Concepts used: Inheritance and Encapsulation
#base class
class House:
    #creating a constructor
    def __init__(self):
        self._bedrooms= 0
        self._location= " "
        self._cost= 0

    #method to get the house type and number of bedrooms
    def getHouseType(self):
        self._bedrooms= int(input("Enter the number of bedrooms: ", ))
        return self._bedrooms

    #method to get the location
    def getLocation(self):
        while True:
            location = input("Enter the location of the house (rural/urban): ").strip().lower()
            if location in ["rural", "urban"]:
                self._location = location
                break
            else:
                print("Invalid location. Please select 'rural' or 'urban'.")

        self._location= location
        return self._location


#derived class to calculate total cost of the house
class Cost(House):
    #constructor
    def getTotalCost(self):
        if self._bedrooms == 0 :
            if self._location == "rural":
                total_cost= self._cost + 5000
            else: 
                total_cost= self._cost + 8000
            print("The total cost of a bedsitter in the ",  self._location, " area is ksh ", total_cost)    

        elif self._bedrooms == 1:
            if self._location == "rural":
                total_cost= self._cost + 10000
            else :
                total_cost= self._cost + 13000
            print("The total cost of a one-bedroom house in the ", self._location, " area is ksh ", total_cost)

        elif self._bedrooms == 2:
            if self._location == "rural":
                total_cost= self._cost + 18000
            else :
                total_cost= self._cost + 20000
            print("The total cost of a two-bedroom house in the ", self._location, " area is ksh ", total_cost)

        elif self._bedrooms == 3:
            if self._location == "rural":
                total_cost= self._cost + 25000
            else :
                total_cost= self._cost + 30000
            print("The total cost of a three-bedroom house in the ", self._location, " area is ksh ", total_cost)
        
        else:
            if self._location == "rural":
                total_cost= self._cost + 40000
            else :
                total_cost= self._cost + 50000
            print("The total cost of mansionette with ", self._bedrooms, " bedrooms in the ", self._location, " area is ksh ", total_cost)

#create object
house_details= House()
house_details= Cost()

#calling the methods
##ALL REQUIRED METHODS NEED TO BE CALLED FOR THE TOTALCOST() METHOD TO WORK OTHERWISE IT WILL PRINT THE FIRST VALUE BY DEFAULT AND MISS SOME PARAMETERS
print(house_details.getHouseType())
print(house_details.getLocation())
print(house_details.getTotalCost())


