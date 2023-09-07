########Using try-exception statements

a= 34
b= "daisies" # old variable is b= 23

try:
    calc= a + b
    print(calc)

except:
    print("An error has occurred")

#######Second demo
length= 14
height= 13
width= 8

try:
    perimeter= 2*(length + width)
    area= length * width
    volume= length * width * height
    print(perimeter)
    print(area)
    print(volume)

except:
    print("The operations has an error")


########Third demo- control structure
# variables
situation= "Home alone"

try:
    if (situation == "Home alone"):
        dec_1= "Go out and wear some nice shoes"
        dec_2= "Stay at home and wear flops"
        final= dec_1 or dec_2
        print(final)
    
    else:
        print("You are stuck at work! dress decent")

except:
    print("There is an error")

######3 decisions logical control structure
#The Try-Exception block DOES NOT catch Syntax errors...only Runtime Error
sugar= 1
milk= 1
teabags=0
heat= 1
sufuria= 1
water= 1
seive= 1

try:
    if (seive == 1 & sufuria == 1 & heat == 1):
        try:
            if (water == 1 & milk ==1):
                try:
                    if(sugar ==1 | teabags ==1):
                        try:
                            print("You can cook tea")
                        except:
                            print("An error has occurred")
                    
                    else:
                        try:
                            print("Buy more necessities")
                        except:
                            print("Error 1 has occured")
                except:
                    print("Error 2 has occurred")
        except:
            print("Error 3 has occurred")
except:
    print("Error 4 occurred")


