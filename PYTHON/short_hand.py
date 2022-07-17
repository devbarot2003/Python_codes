maths = int(input("Enter marks of maths: "))
chem = int(input("Enter marks of chemistry: "))
phy = int(input("Enter the marks of Physics: "))

per = float((maths+chem+phy)/3)

print("Your total percentage is: ", per)

print("A+") if per >= 85 else print("B+") if per >= 75 and per < 85 else print("C")
