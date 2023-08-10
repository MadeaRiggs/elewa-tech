#logic operations
p= True
q= False
r= False

#(P V Q)
a= p or q
print("Result of (P V Q) is ", a) #True

#((P V Q) and R)
b= a and r
print("Result of ((P V Q) and R) is ", b) #False

#(P and R)
c= p and r
print("Result of (P and R) is ", c) #False

#(Q and R)
d= q and r
print("Result of (Q and R) is ", d) #False
#((P and R) V (Q and R))
e= c or d
print("Result of ((P and R) V (Q and R)) is ", e) #False

#((P V Q) and R) v ((P and R) V (Q and R))
final_1= b or e
print("Result of ((P V Q) and R) v ((P and R) V (Q and R)) is ", final_1)

#logic_2
neg_p= not p
neg_q= not q
neg_r= not r

#(-P and -Q)
f= neg_p and neg_q
print("Result of (-P and -Q) is ", f) #False

#(Q and -R)
g= q and neg_r
print("Result of (Q and -R) is ", g) #False

#(-P and -Q) V (Q and -R)
final_2= f or g
print("Result of (-P and -Q) V (Q and -R) is ", final_2)