############3Methods of Bit Operations

# 1)iUser Defined functions
def DecimalToBinary(n):
    return("{0:b}".format(int(n)))

d= DecimalToBinary(9)
print("User Defined function value is ", d)


# 2) Inbult function(Quick Ninja Method)
t= bin(9)
print("Inbuilt function value is ", t)

#converting binary to decimal
def bin_dec(num):
    return int(num,2)

f= bin_dec("11110")
print(f)