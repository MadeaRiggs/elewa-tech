############## DATA STRUCTURES IN PYTHON
##########lists in Python

#creating list
fruits=[]

#inserting operations
##hardcoding the values
fa= "apple"
fb= "mangoes"
fc= "banana"
fd= "orange"

fruits.append(fa)
fruits.append(fb)
fruits.append(fc)
fruits.append(fd)

print(fruits)

#input operation
# fe= input("Enter fruit name: ")
# fruits.append(fe)
# print(fruits)

# fg= int(input("Enter a random number: "))
# fruits.append(fg)
# print(fruits)


########CASE STUDY 2
#using the insert function to add which requires you to  specify the index that will be used 
var= "pineapple"
var1= 50
var2= True

fruits.insert(4, var)
fruits.insert(6, var1)
fruits.insert(7, var2)
print(fruits)


########CASE STUDY 3
#concatenating- combining 2 lists to form 1 list
fruit1= ["avocado", "melon", "kiwi"]
new_fruits= fruit1 + fruits 
print(new_fruits)