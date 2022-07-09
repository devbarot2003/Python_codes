#Implicit Type Conversion --> Python automatically converts one data type to another data type.

num1 = 100                  # this is integer data type
num2 = 1.5                  # this is floating data type

num_tot = num1 + num2

print("The type of num1 is: ",type(num1))
print("The type of num2 is: ",type(num2))

print("The type of num_tot is:", type(num_tot))    #Here python automatically converted the data type as, float = (float + int)

#Explicit Type Conversion --> User convert the data type of an object to required data type

num = 100
string = "500"

print("The type of num is: ",type(num))
print("The type of string is: ",type(string))

string = int(string)

print("The summation of num and string is: ", num+string," And the type of string is: ",type(string))
