#Convert the following questions into lines of code:

a= True
b= True
c= False

#1) a and  b ∧ ¬c =  a or (b ∧ (¬c))
neg_c= not c #True

#a and  b ∧ ¬c
left_side= a and b and neg_c
print("left side answer is ", left_side)

#(b ∧ (¬c))
h= b and neg_c
# print("h is ", h) #True

#a or (b ∧ (¬c))
right_side= a or h
print("right side answer is ", right_side)

#2) (p ∧ q) ∨ (¬p ∧ q) ∨ (¬p ∧ ¬q)
p= True
q= False
neg_p= not p
neg_q= not q

#(p ∧ q)
i= p and q
# print("i is ", i) #False

#(¬p ∧ q)
j= neg_p and q
# print("j is ", j) #False

#(¬p ∧ ¬q)
k= neg_p and neg_q
# print("k is ", k) #False

answer= i or j or k
print("final answer is ", answer)