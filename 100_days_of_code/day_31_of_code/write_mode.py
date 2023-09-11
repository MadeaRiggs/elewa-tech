##################FILE HANDLING
#Write operations

#Write mode case study 1
var_name = open("100_days_of_code/day_31_of_code/sip.txt",  "w")

#writing operation
var_name.write("Hello world")
var_name.write("My name is Kami")
var_name.write("Today is Monday")
var_name.write("I check my emails daily")

var_name.close()