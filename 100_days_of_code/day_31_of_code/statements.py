#combine read, write and append operations
file_write= open("100_days_of_code/day_31_of_code/statements.txt", "w")
file_write.write("The teacher wants us to do this on our own\n")
file_write.write("This is the next statement\n")
file_write.write("Today's lesson was great\n")
file_write.write("It didn't rain today\n")

file_write.close()

#read operation
file_read= open("100_days_of_code/day_31_of_code/statements.txt", "r")
print(file_read.read())

#Append operation
file_add= open("100_days_of_code/day_31_of_code/statements.txt", "a")
file_add.write("This is the final line of code")
file_add.close()

#read operation again
file_read= open("100_days_of_code/day_31_of_code/statements.txt", "r")
# print(file_read.read())

####OR 
for I in file_read:
    print(I)