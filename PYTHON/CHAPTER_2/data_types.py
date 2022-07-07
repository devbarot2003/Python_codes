#We do not need to specify a data type of a variable while assigning value to that variable.


a = 4                   #Integer
b = 'DEV Barot'         #String
c = 9.3                 #Float
d = [2,"Hello",{1:2}]   #List
e = {
    "Hello":"Hey",
    "Never":"No",       #Dictionary
    "Can I?":"May I?"
}
f = (1,4,6,8)           #Tuple

print(type(a))
print(type(c))
print(type(b))
print(len(b))        #It will display the length of the value assigned to variable b
print(type(d))
print(type(e))
print(type(f))