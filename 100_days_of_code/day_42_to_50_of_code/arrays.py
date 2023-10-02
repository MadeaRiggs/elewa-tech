############ Arrays store data of one data type

####code 1
import array as arr

arrayA = arr.array('i')
arrayA.append(4)
print(arrayA)

####### OR
arrayA = arr.array('i', [2, 3, 4, 5])
arrayA.append(4)
print(arrayA)

##to remove the 'i' when printing list
# print(list(arrayA))