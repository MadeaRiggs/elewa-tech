# 1) What is the output of the following code?
x = 50
def fun1():
    x = 25
    print(x)
    
fun1()
print(x)
# Output is 25, 50

#2) What is the output of the following variable assignment?
# x = 75
# def myfunc():
#     #x = x + 1
#     print(x)

# myfunc()
# print(x)

#It results in an error

#3) What is the output of the following code
print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

#output is False True True True

#4) What is the data type of print(type(0xFF))
print(type(0xFF))

#output is <class 'int'>