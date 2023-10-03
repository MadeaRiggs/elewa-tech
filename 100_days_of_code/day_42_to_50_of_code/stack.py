####### A stack has 2 particular methods i.e lists and 
####to remove data from the stack, use the pop function

# mystack= []

# #add data using the append function
# mystack.append("Me")
# mystack.append("Myself")
# mystack.append("and ")
# mystack.append("I")

# print(mystack)

# #remove data using the pop function
# print(mystack.pop())
# print(mystack)

####create stacks using the deque module
from collections import deque

new_stack= deque()
new_stack.append(1)
new_stack.append(2)
new_stack.append(3)
new_stack.append(4)
new_stack.append(5)
new_stack.append(6)

print(new_stack)