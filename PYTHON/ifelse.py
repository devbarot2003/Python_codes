# This is a conditional statement in which we can give multiple conditions and print unique output.

age = int(input("Enter your age: "))

if age<18:
    print("You are not eligible for driving liscence, apply when you are 18 or above.")

elif age >=18 and age<= 70:
    print("You are eligible for driving liscence, good luck for your driving test.")

else:
    print("Not eligible for driving liscence, too old to drive.")