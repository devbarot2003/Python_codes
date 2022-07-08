a = 4
b = 8

print("\nArithmetic Operators\n")
#Arithmetic Operators
print("a + b = ",a+b)
print("a - b = ",a-b)
print("a * b = ",a*b)
print("a / b = ",a/b)

print("\nAssignment operator\n")
#Assignment Operators
c = 0
d = 4
e = 4
f = 9

print("\nShort hand operator\n")
#Short Hand Operators
c += 3
d -= 3
e *= 5
f /=6

print(c)
print(d)
print(e)
print(f)

print("\nComparison operator\n")
#Comparison Operators

a1 = a < b
a2 = c <= d
a3 = e > f
a4 = a >= f

print(a1)
print(a2)
print(a3)
print(a4)

print("\nLogical operator\n")
#Logical Operartors
T = True
F = False

print ("And testing:", (T and F))
print ("Or  testing:", (T or F))
print ("Not testing:", (not F))
print ("Not testing2:", (not T))

print("\nMembership operator\n")
#Membership operator (in, not in)

y = [1,2,3,4,5]
x = 3
z = 9

if x in y:
    print(True)
else:
    print(False)

if z not in y:
    print(True)
else:
    print(False)

print("\nIdentity operator\n")
#Identity operator (is, is not)

n = 7

if n is x:
    print(True)
else:
    print(False)

if n is not x:
    print(True)
else:
    print(False)

#Bitwise operator

# & 	AND	                        Sets each bit to 1 if both bits are 1
# |	    OR	                        Sets each bit to 1 if one of two bits is 1
# ^	    XOR	                        Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	                        Inverts all the bits
# <<	Zero fill left shift        Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift right    Shift by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off