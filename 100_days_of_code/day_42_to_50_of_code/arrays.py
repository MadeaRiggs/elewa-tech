############ Arrays store data of one data type
#####They are mutable (data items stored can be changed if they are the same data type)
#####Data items are enclosed in curly brackets


####code 1
import array as arr

# arrayA = arr.array('i')
# arrayA.append(4)
# print(arrayA)

# ####### OR
# arrayA = arr.array('i', [2, 3, 4, 5])
# arrayA.append(4)
# print(arrayA)

##to remove the 'i' when printing list
# print(list(arrayA))


#using the insert function
#for characters use 'u' NOT 'c' 
var_a= arr.array('u')
var1= input("Enter the character value: ")

#to use the insert function, specify the index you want the value to be added 
var_a= var_a.insert(0, var1)