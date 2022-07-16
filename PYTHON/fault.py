#Design a calculator which will correctly solve all the problems except the following ones:

#50 * 9 = 509, 80 + 56 = 25889, 17 * 98 = 1798

def faulty_calc():
    while True:
        opr = input("Enter the operation you want to perform: ")
        if opr == "exit":
            break
        num1 = int(input("Enter number 1:"))
        num2 = int(input("Enter number 2:"))

        if ((num1 == 50 and num2 == 9) or (num1 == 9 and num2 ==50)) and opr == "*":
            print("Ans: 509")
        
        elif((num1 == 56 and num2 == 80) or (num1 == 80 and num2 ==56)) and opr == "+":
            print("Ans: 25889")
        
        elif((num1 == 98 and num2 == 17) or (num1 == 17 and num2 ==98)) and opr == "/":
            print("Ans: 1798")
        
        if opr == "+":
            print("Ans: ",(num1+num2))
        elif opr == "-":
            print("Ans: ",(num1-num2))
        elif opr == "*":
            print("Ans: ",(num1*num2))
        elif opr == "/":
            print("Ans: ",(num1/num2))
        elif opr == "**":
            print("Ans: ",(num1**num2))
        elif opr == "%":
            print("Ans: ",(num1%num2))
        else:
            print("Operation not found.")

print('''
Welcome to faulty calculator

+ for addition
- for substration
* for multiplication
/ for division
** for power
"%" for modulo
"exit" to stop calculator
''')

faulty_calc()