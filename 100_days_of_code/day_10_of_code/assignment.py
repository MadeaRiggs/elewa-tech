# Question 1- Write codes to convert the following into Bits

def DecimalToBinary(n):
    return("{0:b}".format(int(n)))

# a) 12
a= DecimalToBinary(12)
print("Binary value of 12 is ", a)

# b) 34
b= DecimalToBinary(34)
print("Binary value of 34 is ", b)

# c) 65
c= DecimalToBinary(12)
print("Binary value of 65 is ", c)

# 4) 456
d= DecimalToBinary(12)
print("Binary value of 456 is ", d)


#Question 2- Write a Python program that will allow you to convert numbers into Bits
# a) 124
e= DecimalToBinary(124)
print("Binary value of 124 is ", e)

# b) 906
f= DecimalToBinary(906)
print("Binary value of 906 is ", f)

# c) 85
g= DecimalToBinary(85)
print("Binary value of 85 is ", g)

# 4) 6703
h= DecimalToBinary(6703)
print("Binary value of 6703 is ", h)

#Question 3- Write a python program using user defined Functions that will allow you to convert the following into Bits and To decimals

#converting binary to decimal
def bin_dec(num):
    return int(num,2)

# a) 110111
i= bin_dec("110111")
print("Decimal value of 110111 is ", i)

# b) 010111100
i= bin_dec("010111100")
print("Decimal value of 010111100 is ", i)

# c) 1001000110
i= bin_dec("1001000110")
print("Decimal value of 1001000110 is ", i)