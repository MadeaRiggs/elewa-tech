#Convert the following questions into lines of code:

p= True
q= True
r= False

# 1) (p∨¬q) and q
neg_q= not q

#(p∨¬q)
a= p or neg_q
#print("a is ", a) #True

answer1= a and q
print("answer 1 is ", answer1)

#2) (p or q) not (¬q and ¬p)
#(p or q)
b= p or q
# print("b is ", b) #True

#(¬q and ¬p)
neg_p= not p
c= neg_q and neg_p
# print("c is ", c) #False

#**********EITHER
# answer2 = b and (not c)
#*************OR
answer2 = b; (not c)
print("answer 2 is ", answer2) 

#3) (p ∨ q) ∧ (p or  ¬ q)

#(p or  ¬ q)
d= p or neg_q
# print("d is ", d) #True

answer3= b and d
print("answer 3 is ", answer3)

#4) p ∨ (q ∧ r) 

#(q ∧ r) 
e= q and r
#print("e is ", e) #False

answer4= p or e
print("answer 4 is ", answer4)

#5) ¬(p ∧ q) ∨ (p ∨ q) 

#(p ∧ q)
f= p and q
#print("f is ", f) #True

#¬(p ∧ q)
g= not f
#print("g is ", g) #False

answer5= g or b
print("answer 5 is ", answer5)