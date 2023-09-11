##################FILE HANDLING
#Read operations

'''
r+-read and write respectively
r+- write and read respectively
a-append and write respectively
'''

#Case study 1

#Reading a file
# var_name = open("100_days_of_code/day_31_of_code/sip.txt",  "r")
# # print(var_name)

# for each in var_name:
#     print(var_name)


#second demo
# file_read= open("100_days_of_code/day_31_of_code/sip.txt", "r")
# print(file_read.read())


#third demo
# with open("100_days_of_code/day_31_of_code/sip.txt") as file_read:
#     text = file_read.read()
#     print(text)

#performing split operation on file
with open("100_days_of_code/day_31_of_code/sip.txt") as data:
    data_1= data.readlines()
    for line in data_1:
        var_a= line.split()
        print(var_a)