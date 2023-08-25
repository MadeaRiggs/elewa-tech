#########Example 1

fruits = ['Mangoe', 'orange', 'pawpaw', 'apple', 'avocado', 'melon']

for fruit in fruits:
    print(fruit)

for index in range(3):
    print(fruits[index])

########Example 2: Creating a pyramid of numbers
num = 5

for i in range(num) :
    print(i)

########Example 3: Printing each letter in the string
chart= "Pythonista"

for i in chart :
    print(i)

########Example 4: Printing each word in the string
my_str = "i love to code"
words = my_str.split()

for i in words:
    print(i)


my_sent= '''i love to code
            We love to code
            She loves to code
            You love to code '''
sentence = my_sent.split('\n')

for i in sentence:
    print(i)
